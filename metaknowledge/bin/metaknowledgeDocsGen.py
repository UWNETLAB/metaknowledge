#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
"""This is intended for metaknowledge only and may not work with anything else"""

import inspect
import argparse
import os
import time
import metaknowledge
import metaknowledge.WOS.tagProcessing
import importlib
import re

documentedModules = ['contour', 'WOS', 'medline', 'proquest', 'scopus', 'journalAbbreviations']

docsPrefix = time.strftime("%Y-%m-%d-")

funcCounter = 0
undocumented = 0

blurbDict = {
    #modules
    'contour' : "A nicer matplotlib graph visualizer and contour plot",
    'WOS' : "The backend functions and classes associated with the Web of Science",
    'journalAbbreviations' : "Handles the abbreviated journal names used by WOS",
    'medline' : "The backend functions and classes associated with Medline, the format used by Pubmed",
    'scopus' : "The backend functions and classes associated with records from scopus",
    'proquest' : "The backend functions and classes associated with ProQuest",

    #Classes

    'Citation' : "Citation are special, here is how they are handled",
    'WOSCitation' : "A Citation that supports the WOS journal abbreviations",

    'Record' : "The base of all the other Records, basically a dict",
    'ExtendedRecord' : "A Record the processes its contents before returning them",
    'WOSRecord' : "The object for containing and processing WOS entries",
    'ProQuestRecord' : "The object for containing and processing ProQuest entries",
    'MedlineRecord' : "The object for containing and processing Medline entries",
    'ScopusRecord' : "The object for containing and processing Scopus entries",

    'Grant' : "The base for all the other Grants",
    'FallbackGrant' : "The Grant used if a file was not identifiable",
    'CIHRGrant' : "The container for CIHR grant entries",
    'NSERCGrant' : "The container for NSERC grant entries",
    'MedlineGrant' : "The container for grants derived from Medline Records entries",
    'NSFGrant' : "The container for NSF grant entries",

    'Collection' : "The base of all other Collections, basically a set",
    'CollectionWithIDs' : "A Collection that only holds <i>metaknowledge</i> objects",
    'RecordCollection' : "A Collection of Records, this is what does most of the stuff on Records",
    'GrantCollection' : "A Collection of Grants, this is what does most of the stuff on Grants",

    #Deprecated
    'tagProcessing' : "All the tags and how they are handled",
}

singleFileYAML = """---
layout: page
title: Full Documentation {}
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
""".format(metaknowledge.__version__)

def makeBlurb(name):
    if name in blurbDict:
        return blurbDict[name]
    else:
        print("\033[94m{} had no blurb\033[0m".format(name))
        return 'BLURB NEEDED FOR {}'.format(name)
        #raise RuntimeError("{} needs a blurb".format(name))

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
    parser = argparse.ArgumentParser(description="A simple script to generate docs for metaknowledge")
    parser.add_argument("-dir", "-d", default = os.path.normpath('.') ,nargs='?', help = 'Directory to write files to')
    parser.add_argument("-single", "-s", action = 'store_true', default = False, help = 'Write to only one file.')
    return parser.parse_args()

def getLineNumber(objTuple):
    try:
        ln = str(inspect.getsourcelines(objTuple[1])[1])
        fl = inspect.getfile(objTuple[1])
    except (OSError, TypeError):
        return '-1' #Because
    else:
        return fl + ln

def cleanargs(obj, basic = False, isClass = False):
    if isClass:
        argClasses = []
        for c in obj.__bases__:
            n = c.__name__
            if n in blurbDict:
                n = '<a href="#{0}"><u style="border-bottom: .5px dashed gray;">{0}</u></a>'.format(n)
            argClasses.append(n)
        argStr = ', '.join(argClasses)
    else:
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
    return "[{0}]({{{{ site.baseurl }}}}{{{{ page.url }}}}#{3})".format(s.group(1), docsPrefix, s.group(2), s.group(3))

def makeSingleFileUrls(s):
    return "[{0}](#{1})".format(s.group(1), s.group(3))

def cleanedDoc(obj, lvl, singleFile = False):
    ds = inspect.getdoc(obj)
    if not isinstance(ds, str):
        raise AttributeError("'{}' on line {} of '{}' is missing its docstring".format(obj, inspect.getsourcelines(obj)[1], inspect.getfile(obj)))
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
    return '<hr style="{}">'.format(''.join(style))

def makeTable(entries, header = '', prefix = '', withBlurbs = False, bigTable = False, simple = False, areClasses = False):
    ents = []
    if prefix:
        prefix = prefix + '.'
    for e in entries:
        if withBlurbs:
            if areClasses:
                ents.append("""<li><article><a href="#{0}"><b>{0}</b></a>{1}<span class="excerpt">{2}</span></article></li>""".format(e[0], cleanargs(e[1], basic = True, isClass = areClasses), makeBlurb(e[0])))
            else:
                ents.append("""<li><article><a href="#{0}"><b>{0}</b><span class="excerpt">{1}</span></a></article></li>""".format(e, makeBlurb(e)))
        elif bigTable:
            if e[2] is None:
                ents.append("""<li><article><a href="#{0}"><b>{0}</b>{1}</a></article></li>""".format(e[0], cleanargs(e[1], basic = True, isClass = areClasses), prefix))
            else:
                ents.append("""<li><article><a href="#{0}"><small>{2}</small>.<b>{0}</b>{1}</a></article></li>""".format(e[0], cleanargs(e[1], basic = True, isClass = areClasses), e[2]))
        elif simple:
            ents.append("""<li><article><b>{0}</b>{1}</article></li>""".format(e[0], cleanargs(e[1], isClass = areClasses, basic = True)))
        else:
            ents.append("""<li><article><a href="#{0}"><b>{0}</b>{1}</a></article></li>""".format(e[0], cleanargs(e[1], basic = True, isClass = areClasses), prefix))
    s = """<h3>{}</h3>\n\n<ol class="post-list">\n{}\n</ol>\n""".format(header,'\n'.join(ents))
    return s

def writeFunc(fn, f, prefix = '', level = 5, singleFile = False):
    global funcCounter
    funcCounter += 1
    f.write(makeLine() + "\n\n")
    f.write(makeTitle(prefix, fn[0], cleanargs(fn[1]), singleFile = singleFile))
    try:
        f.write(cleanedDoc(fn[1], lvl = level, singleFile = singleFile))
    except AttributeError:
        f.write("# Needs to be written\n\n")
        global undocumented
        undocumented += 1
        print("\033[93m{0}{1} had no docs\033[0m".format(prefix, fn[0]))

def writeClass(cl, f, prefix = '', level = 4, singleFile = False, exceptMode = False):
    f.write(makeTitle(prefix, cl[0], cleanargs(cl[1], isClass = True), singleFile = singleFile))
    if not exceptMode:
        f.write(makeTitle(prefix, "{}.__init__".format(cl[0]), cleanargs(cl[1].__init__), singleFile = singleFile))
    try:
        f.write(cleanedDoc(cl[1], lvl = level, singleFile = singleFile))
    except AttributeError:
        f.write("# Needs to be written\n\n")
        global undocumented
        undocumented += 1
        print("\033[93m{0}{1} had no docs\033[0m".format(prefix, cl[0]))

def proccessClass(cls, f, singleFile = False, exceptMode = False):
    writeClass(cls, f, singleFile = singleFile, exceptMode = exceptMode)
    baseMems = [ i for c in cls[1].__bases__ for i in inspect.getmembers(c)]
    if singleFile:
        f.write(makeLine())
    try:
        documented = cls[1]._documented
    except AttributeError:
        documented = []
    funcs = []
    for m in sorted(inspect.getmembers(cls[1]), key = getLineNumber):
        if m[0][0] == '_' or m in baseMems or m[0] == 'with_traceback':
            if m[0] in documented:
                funcs.append(m)
        elif inspect.isfunction(m[1]):
            funcs.append(m)
    if len(funcs) > 0 and not exceptMode:
        f.write(makeTable(funcs, prefix = cls[0], header = "\nThe {} class has the following methods:".format(cls[0])))
        for m in funcs:
            writeFunc(m, f, prefix = '{}.'.format(cls[0], singleFile = singleFile))

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
    print("Starting {}".format(mod))
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
        f.write(makeTable(funcs, prefix = mod, header = '<a name="{0}">The <a href="#{0}"><u>{0}</u></a> module provides the following functions:</a>'.format(mod)))
        for fn in funcs:
            writeFunc(fn, f, prefix = "{}.".format(mod))
    else:
        for fn in metaknowledge.WOS.tagProcessing.tagToFunc.items():
            writeFunc((metaknowledge.tagToFull(fn[0]), fn[1]), f, prefix = "{}.".format(mod))
    if targetFile is None:
        f.write("\n{% include docsFooter.md %}")
        f.close()

def writeMainBody(funcs, vrs, exceptions, targetFile = None, singleFile = False):
    if targetFile:
        f = targetFile
    else:
        f = open(docsPrefix + "overview.md", 'w')

    f.write(makeHeader("Overview", "The <i>metaknowledge</i> Package, a quick tour", tags = ["main"], weight = 0, layout = "doc", singleFile = singleFile))
    f.write(cleanedDoc(metaknowledge, 3, singleFile = singleFile) + '\n\n')
    if targetFile is None:
        f.write("\n{% include docsFooter.md %}")
        f.close()
        f = open(docsPrefix + "metaknowledge.md", 'w')
    f.write(makeHeader("Base Functions", "The <i>metaknowledge</i> functions, for filtering reading and writing graphs", tags = ["functions"], weight = 1, layout = "doc", singleFile = singleFile))
    f.write(makeTable(funcs, header = "The functions provided by <i>metaknowledge</i> are:"))
    f.write(makeTable(exceptions, header = "The Exceptions defined by <i>metaknowledge</i> are:", simple = True, areClasses = True))
    for fnc in funcs:
        writeFunc(fnc, f)
    first = True
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
        single = True
        f = open("metaknowledgeFull.md",'w')
        f.write(singleFileYAML)

        f.write(makeTable(documentedModules, header = '<a name="objlist"></a>The modules of <i>metaknowledge</i> are:', withBlurbs = True))

        f.write(makeTable(classes, header = '<a name="objlist"></a>The classes of <i>metaknowledge</i> are:', withBlurbs = True, areClasses = True))

        bigTableEntries = [(f[0], f[1], None) for f in funcs]

        for cls in classes:
            baseMems = inspect.getmembers(cls[1].__bases__[0])
            for m in sorted(inspect.getmembers(cls[1]), key = getLineNumber):
                if m[0][0] == '_' or m in baseMems:
                    pass
                elif inspect.isfunction(m[1]):
                    bigTableEntries.append((m[0], m[1], cls[0]))

        f.write(makeTable(bigTableEntries, header = '<a name="fulllist"></a>All the functions and methods of <i>metaknowledge</i> and its objects are as follows:', bigTable = True))

        for mod in documentedModules:
            modTableEntries = []
            module = importlib.import_module('metaknowledge.{}'.format(mod))
            for m in sorted(inspect.getmembers(module, predicate = inspect.isfunction), key = getLineNumber):
                if inspect.isbuiltin(m[1]) or m[0][0] == '_':
                    pass
                elif inspect.isfunction(m[1]):
                    modTableEntries.append((m[0], m[1], mod))
            f.write(makeTable(modTableEntries, header = 'All the functions of the <a href="#{0}"><u>{0}</u></a> module are as follows:'.format(mod), bigTable = True))

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
    print("{} total functions".format(funcCounter))
    print("{} undocumented".format(undocumented))

if __name__ == '__main__':
    mkDocs()
