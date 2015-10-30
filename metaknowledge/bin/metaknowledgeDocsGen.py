#!/usr/bin/env python3

"""This is intended for metaknowledge only and may not work with anything else"""

import inspect
import argparse
import os
import time
import metaknowledge
import importlib
import re

documentedModules = ['tagProcessing', 'visual', 'journalAbbreviations']

docsPrefix = time.strftime("%Y-%m-%d-")

blurbDict = {
    'visual' : "A nicer matplotlib graph visualizer and contour plot",
    'tagProcessing' : "All the tags and how they are handled",
    'journalAbbreviations' : "Look here to get your J9 database",
    'Citation' : "Citation are special, here is how they are handled",
    'Record' : "What RecordCollections are made of",
    'RecordCollection' : "Where all the stuff happens, look here if you want to make things",
}

singleFileYAML = """---
layout: page
title: "metaknowledge: A Python3 library for bibliometrics and quantitative sociology of knowledge"
author:
- name: Reid McIlroy-Young
  department:
  affiliation: University of Waterloo, Waterloo ON, Canada
  email: rmcilroy@uwaterloo.ca
- name: John McLevey
  affiliation: University of Waterloo, Waterloo ON, Canada
  email: john.mclevey@uwaterloo.ca
shorttitle: metaknowledge
search_omit: true
---
"""

def makeBlurb(name):
    if name in blurbDict:
        return blurbDict[name]
    else:
        raise RuntimeError("{} needs a blurb".format(name))


def makeHeader(title, excerpt, tags = (), weight = 10, layout = "doc", singleFile = False):
    if singleFile:
        s = """\n---\n<a name="{0}"></a>\n""".format(title)
    else:
        s = """---
layout: {4}
title: {0}
categories: docs
excerpt: {1}
tags: [{2}]
weight: {3}
---
<a name="{0}"></a>
""".format(title, excerpt, ', '.join(tags), weight, layout)
    return s

def argumentParser():
    parser = argparse.ArgumentParser(description="A simple script to genrate docs for metaknowledge")
    parser.add_argument("-dir", "-d", default = os.path.normpath('.') ,nargs='?', help = 'Directory to write files to')
    parser.add_argument("-single", "-s", action = 'store_true', default = False ,help = 'Write to only one file.')
    return parser.parse_args()

def getLineNumber(objTuple):
    try:
        ln = str(inspect.getsourcelines(objTuple[1])[1])
        fl = inspect.getfile(objTuple[1])
    except (OSError, TypeError):
        return '-1' #Because
    else:
        return fl + ln

def cleanargs(obj, basic = False):
    argStr = inspect.formatargspec(*inspect.getfullargspec(obj))
    argStr =  argStr.replace(", *args", '').replace(", **kwargs", '').replace('self, ', '').replace('self', '')[1:-1]
    if len(argStr) > 0:
        argStr = ', '.join([a for a in argStr.split(', ') if a[0] != '_'])
        if basic:
            return "(<i>{0}</i>)".format(argStr)
        else:
            return "(_{0}_)".format(argStr)
    else:
        return '()'

def makeUrls(s):
    return "[{0}]({{{{ site.baseurl }}}}{{% post_url /docs/{1}{2} %}}#{3})".format(s.group(1), docsPrefix, s.group(2), s.group(3))

def makeSingleFileUrls(s):
    return "[{0}](#{1})".format(s.group(1), s.group(3))

def cleanedDoc(obj, lvl, singleFile = False):
    ds = inspect.getdoc(obj)
    lns = ds.split('\n')
    nds = ''
    for line in lns:
        if singleFile:
            line = re.sub(r"\[(\S+)\]\(\#(\S+)\.(\S+)\)", makeSingleFileUrls, line, count = 99)
        else:
            line = re.sub(r"\[(\S+)\]\(\#(\S+)\.(\S+)\)", makeUrls, line, count = 99)
        if len(line) < 1:
            nds += '\n'
        elif line[0] == '#':
            nds += '#' * (lvl + 1) + line[1:] + '\n'
        elif line[0:4] == '    ':
            nds += '    ' + line[4:] + '\n'
        elif line[0] == '>':
            if line[1] != '>':
                nds += line[1:] + '\n'
            else:
                nds += "> " +  line[2:] + '\n'
        else:
            nds += line + '\n'
    return '{}\n\n'.format(nds)

def makeTitle(module, name, args = '', singleFile = False):
    if singleFile:
        s = '<a name="{1}"></a><small>{0}</small>**[<ins>{1}</ins>](#{1})**{2}:\n\n'.format(module, name, args)
    else:
        s = '<a name="{1}"></a><small>{0}</small>**[<ins>{1}</ins>]({{{{ site.baseurl }}}}{{{{ page.url }}}}#{1})**{2}:\n\n'.format(module, name, args)
    return s

def makeLine():
    style = [
    "padding: 0;",
    "border: none;",
    "border-width: 3px;",
    "height: 20px;",
    "color: #333;",
    "text-align: center;",
    "border-top-style: solid;",
    "border-bottom-style: solid;",
    ]
    return('<hr style="{}">'.format(''.join(style)))

def makeTable(entries, header = '', prefix = '', withBlurbs = False):
    ents = []
    if prefix:
        prefix = prefix + '.'
    for e in entries:
        if withBlurbs:
            ents.append("""<li><article><a href="#{0}"><b>{0}</b><span class="excerpt">{1}</span></a></article></li>""".format(e, blurbDict[e]))
        else:
            ents.append("""<li><article><a href="#{0}"><b>{0}</b>{1}</a></article></li>""".format(e[0], cleanargs(e[1], basic = True), prefix))
    s = """{}\n\n<ul class="post-list">\n{}\n</ul>\n""".format(header,'\n'.join(ents))
    return s

def writeFunc(fn, f, prefix = '', level = 5, singleFile = False):
    f.write(makeLine() + "\n\n")
    f.write(makeTitle(prefix, fn[0], cleanargs(fn[1]), singleFile = singleFile))
    try:
        f.write(cleanedDoc(fn[1], lvl = level, singleFile = singleFile))
    except AttributeError:
        f.write("# Needs to be written\n\n")
        print("\033[93m{0}{1} had no docs\033[0m".format(prefix, fn[0]))

def writeClass(cl, f, prefix = '', level = 4, singleFile = False):
    f.write(makeTitle(prefix, cl[0], cleanargs(cl[1].__init__), singleFile = singleFile))
    try:
        f.write(cleanedDoc(cl[1], lvl = level, singleFile = singleFile))
    except AttributeError:
        f.write("# Needs to be written\n\n")
        print("\033[93m{0}{1} had no docs\033[0m".format(prefix, cl[0]))

def proccessClass(cl, f, singleFile = False):
    writeClass(cl, f, singleFile = singleFile)
    baseMems = inspect.getmembers(cl[1].__bases__[0])
    funcs = []
    for m in sorted(inspect.getmembers(cl[1]), key = getLineNumber):
        if m[0][0] == '_' or m in baseMems:
            pass
        elif inspect.isfunction(m[1]):
            funcs.append(m)
    f.write(makeTable(funcs, prefix = cl[0], header = "The {} class has the following methods:".format(cl[0])))
    for m in funcs:
        writeFunc(m, f, prefix = '{}.'.format(cl[0], singleFile = singleFile))

def writeClassFile(name, typ, targetFile = None, singleFile = False):
    fname = docsPrefix + "{}.md".format(name)
    if targetFile is not None:
        f = targetFile
    else:
        f = open(fname, 'w')
    f.write(makeHeader(name, makeBlurb(name), tags = ["class"], weight = 2, singleFile = singleFile))
    proccessClass((name, typ), f, singleFile = singleFile)
    if targetFile is None:
        f.write("\n{% include docsFooter.md %}")
        f.close()

def writeModuleFile(mod, targetFile = None, singleFile = False):
    fname = docsPrefix + "{}.md".format(mod)
    if targetFile is not None:
        f = targetFile
    else:
        f = open(fname, 'w')
    f.write(makeHeader(mod, makeBlurb(mod), tags = ["module"], weight = 3, singleFile = singleFile))
    f.write('\n# [{0}]({{{{ site.baseurl }}}}{{{{ page.url }}}}#{0})\n\n'.format(mod))
    module = importlib.import_module('metaknowledge.{}'.format(mod))
    f.write(cleanedDoc(module, 3, singleFile = singleFile) + '\n\n')
    funcs = []
    for m in sorted(inspect.getmembers(module, predicate = inspect.isfunction), key = getLineNumber):
        if inspect.isbuiltin(m[1]) or m[0][0] == '_':
            pass
        elif inspect.isfunction(m[1]):
            funcs.append(m)
    if mod != "tagProcessing":
        f.write(makeTable(funcs, prefix = mod, header = "The {} module provides the following functions:".format(mod)))
    for fn in funcs:
        writeFunc(fn, f, prefix = "{}.".format(mod))
    if targetFile is None:
        f.write("\n{% include docsFooter.md %}")
        f.close()

def writeMainBody(funcs, vrs, exceptions, targetFile = None, singleFile = False):
    if targetFile:
        f = targetFile
    else:
        f = open(docsPrefix + "overview.md", 'w')
        f.write(makeHeader("Overview", "The metaknowledge Package, a quick tour", tags = ["main"], weight = 0, layout = "doc"))
    f.write(cleanedDoc(metaknowledge, 3, singleFile = singleFile) + '\n\n')
    if targetFile is None:
        f.write("\n{% include docsFooter.md %}")
        f.close()
        f = open(docsPrefix + "metaknowledge.md", 'w')
    f.write(makeHeader("Functions", "The metaknowledge functions, for filtering reading and writing graphs", tags = ["functions"], weight = 1, layout = "doc", singleFile = singleFile))
    f.write(makeTable(funcs, header = "The functions provided by metaknowledge are:"))
    for fnc in funcs:
        writeFunc(fnc, f)
    first = True
    for excpt in exceptions:
        if first:
            first = False
        else:
            f.write(makeLine() + "\n\n")
        proccessClass(excpt, f)
    if targetFile is None:
        f.write("\n{% include docsFooter.md %}")
        f.close()

def main(args):
    wDir = os.path.expanduser(os.path.normpath(args.dir))
    if not os.path.isdir(wDir):
        try:
            os.mkdir(wDir)
        except OSError:
            print('Creating the directory {} failed'.format(wDir))
            return 1
    os.chdir(wDir)
    classes = []
    funcs = []
    vrs = []
    exceptions = []
    builtins = []
    for m in sorted(inspect.getmembers(metaknowledge), key = getLineNumber):
        if inspect.isbuiltin(m[1]) or m[0][0] == '_':
            builtins.append(m)
        elif inspect.isclass(m[1]):
            if issubclass(m[1], Exception):
                exceptions.append(m)
            else:
                classes.append(m)
        elif inspect.isfunction(m[1]):
            funcs.append(m)
        else:
            vrs.append(m)
    if args.single:
        f = open("metaknowledgeFull.md",'w')
        f.write(singleFileYAML)
        f.write(makeTable([c[0] for c in classes] + documentedModules, header = "The classes and modules of metaknowledge are:", withBlurbs = True))
        single = True
    else:
        single = False
        f = None
    writeMainBody(funcs, vrs, exceptions, targetFile = f, singleFile = single)
    for cls in classes:
        writeClassFile(*cls, targetFile = f, singleFile = single)
    for mod in documentedModules:
        writeModuleFile(mod, targetFile = f, singleFile = single)
    if args.single:
        f.write("\n{% include docsFooter.md %}")
        f.close

def mkDocs():
    args = argumentParser()
    main(args)

if __name__ == '__main__':
    mkDocs()
