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

def makeHeader(title, excerpt, tags = (), weight = 10, layout = "doc"):
    return """---
layout: {4}
title: {0}
categories: docs
excerpt: {1}
tags: [{2}]
weight: {3}
---
<a name="{0}"></a>
""".format(title, excerpt, ', '.join(tags), weight, layout)

def argumentParser():
    parser = argparse.ArgumentParser(description="A simple script to genrate docs for metaknowledge")
    parser.add_argument("-dir", "-d", default = os.path.normpath('.') ,nargs='?', help = 'Directory to write files to')
    return parser.parse_args()

def getLineNumber(objTuple):
    try:
        ln = inspect.getsourcelines(objTuple[1])[1]
    except (OSError, TypeError):
        return -1
    else:
        return ln

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
    return "[{0}]({{{{ site.baseurl }}}}{{% post_url /docs/{1}{2} %}}#{3})".format(s.group(1), docsPrefix, s.group(2), s.group(2))

def cleanedDoc(obj, lvl):
    ds = inspect.getdoc(obj)
    lns = ds.split('\n')
    nds = ''
    for line in lns:
        line = re.sub(r"\[(\S+)\]\(\#(\S+)\.(\S+)\)", makeUrls,line, count = 99)
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

def makeTitle(module, name, args = ''):
    s = '<a name="{0}{1}"></a><small>{0}</small>**[<ins>{1}</ins>]({{{{ site.baseurl }}}}{{{{ page.url }}}}#{0}{1})**{2}:\n\n'.format(module, name, args)
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

def makeTable(entries, header = '', prefix = ''):
    ents = []
    if prefix:
        prefix = prefix + '.'
    for e in entries:
        ents.append("""<li><article><a href="#{2}{0}"><b>{0}</b>{1}</a></article></li>""".format(e[0], cleanargs(e[1], basic = True), prefix))
    s = """{}\n\n<ul class="post-list">\n{}\n</ul>\n""".format(header,'\n'.join(ents))
    return s

def writeFunc(fn, f, prefix = '', level = 5):
    f.write(makeLine() + "\n\n")
    f.write(makeTitle(prefix, fn[0], cleanargs(fn[1])))
    try:
        f.write(cleanedDoc(fn[1], lvl = level))
    except AttributeError:
        f.write("# Needs to be written\n\n")
        print("\033[93m{0}{1} had no docs\033[0m".format(prefix, fn[0]))

def writeClass(cl, f, prefix = '', level = 4):
    f.write(makeTitle(prefix, cl[0], cleanargs(cl[1].__init__)))
    try:
        f.write(cleanedDoc(cl[1], lvl = level))
    except AttributeError:
        f.write("# Needs to be written\n\n")
        print("\033[93m{0}{1} had no docs\033[0m".format(prefix, cl[0]))

def proccessClass(cl, f):
    writeClass(cl, f)
    baseMems = inspect.getmembers(cl[1].__bases__[0])
    funcs = []
    for m in sorted(inspect.getmembers(cl[1]), key = getLineNumber):
        if m[0][0] == '_' or m in baseMems:
            pass
        elif inspect.isfunction(m[1]):
            funcs.append(m)
    f.write(makeTable(funcs, prefix = cl[0], header = "The {} class has the following methods:".format(cl[0])))
    for m in funcs:
        writeFunc(m, f, prefix = '{}.'.format(cl[0]))

def writeClassFile(name, typ):
    fname = docsPrefix + "{}.md".format(name)
    f = open(fname, 'w')
    f.write(makeHeader(name, "The {} Class".format(name), tags = ["class"], weight = 2))
    proccessClass((name, typ), f)
    f.write("\n{% include docsFooter.md %}")
    f.close()

def writeModuleFile(mod):
    fname = docsPrefix + "{}.md".format(mod)
    f = open(fname, 'w')
    f.write(makeHeader(mod, "The {} Module".format(mod), tags = ["module"], weight = 3))
    f.write('\n# [{0}]({{{{ site.baseurl }}}}{{{{ page.url }}}}#{0})\n\n'.format(mod))
    module = importlib.import_module('metaknowledge.{}'.format(mod))
    f.write(cleanedDoc(module, 3) + '\n\n')
    funcs = []
    for m in sorted(inspect.getmembers(module, predicate = inspect.isfunction), key = getLineNumber):
        if inspect.isbuiltin(m[1]) or m[0][0] == '_':
            pass
        elif inspect.isfunction(m[1]):
            funcs.append(m)
    if mod != "tagProcessing":
        f.write(makeTable(funcs, prefix = mod ,header = "The {} modlue provides the following functions:".format(mod)))
    for fn in funcs:
        writeFunc(fn, f, prefix = "{}.".format(mod))
    f.write("\n{% include docsFooter.md %}")
    f.close()

def writeMainBody(funcs, vrs, exceptions):
    f = open(docsPrefix + "overview.md", 'w')
    f.write(makeHeader("Overview", "The metaknowledge Package", tags = ["main"], weight = 0, layout = "doc"))
    f.write(cleanedDoc(metaknowledge, 3) + '\n\n')
    f.write("\n{% include docsFooter.md %}")
    f.close()
    f = open(docsPrefix + "metaknowledge.md", 'w')
    f.write(makeHeader("Functions", "The metaknowledge Functions", tags = ["functions"], weight = 1, layout = "doc"))
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
    writeMainBody(funcs, vrs, exceptions)
    for cls in classes:
        writeClassFile(*cls)
    for mod in documentedModules:
        writeModuleFile(mod)

def mkDocs():
    args = argumentParser()
    main(args)

if __name__ == '__main__':
    mkDocs()
