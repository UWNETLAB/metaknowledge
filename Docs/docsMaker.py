"""This is intended for isilib only and may not work with anything else"""
import inspect
import argparse
import os
import isilib

documentedModules = ['tagFuncs']

jekyllyHeader ="""---
layout: page
title: isilib Docs
---
<a name="isilib"></a>"""

def argumentParser():
    parser = argparse.ArgumentParser(description="A simple script to genrate docs for isilib")
    parser.add_argument("--output", "-o", default = 'isilibDocs.md', nargs='?')
    parser.add_argument("dir", default = os.getcwd() ,nargs='?', help = 'Directory to write files to')
    return parser.parse_args()

def cleanargs(obj):
    argStr = inspect.formatargspec(*inspect.getfullargspec(obj))
    argStr =  argStr.replace(", *args", '').replace(", **kwargs", '').replace('self, ', '').replace('self', '')[1:-1]
    if len(argStr) > 0:
        return "(_{0}_)".format(argStr)
    else:
        return '()'


def cleanedDoc(obj, lvl):
    ds = inspect.getdoc(obj)
    ds = ds.replace('\n', '\n>')
    ds = ds.replace('# ', '#' * lvl + '# ')
    return '>{}\n\n'.format(ds)

def writeFunc(fn, f, prefix = 'isilib.', level = 4):
    #print("Writing {0}{1}".format(prefix, fn[0]))
    s = '<a name="{0}{1}"></a>{0}**{1}**{2}:\n\n'.format(prefix, fn[0], cleanargs(fn[1]))
    f.write(s)
    try:
        f.write(cleanedDoc(fn[1], lvl = level))
    except AttributeError:
        f.write("# Needs to be written\n\n")
        print("\033[93m{0}{1} had no docs\033[0m".format(prefix, fn[0]))

def writeClass(cl, f, prefix = 'isilib.', level = 4):
    #print("Writing {0}{1}".format(prefix, cl[0]))
    s = '<a name="{0}{1}"></a>{0}**{1}**{2}:\n\n'.format(prefix, cl[0], cleanargs(cl[1].__init__))
    f.write(s)
    try:
        f.write(cleanedDoc(cl[1], lvl = level))
    except AttributeError:
        f.write("# Needs to be written\n\n")
        print("\033[93m{0}{1} had no docs\033[0m".format(prefix, cl[0]))

def writeMod(md, f, prefix = 'isilib.', level = 3):
    #print("Writing {0}{1}".format(prefix, md[0]))
    f.write('{0} <a name="{1}{2}"></a>{1}**{2}**:\n\n'.format('#' * level, prefix, md[0]))
    f.write(cleanedDoc(md[1], lvl = level))
    for m in inspect.getmembers(md[1], predicate = inspect.isfunction):
        f.write("- - -\n\n")
        if m[0][0] != '_':
            writeFunc(m, f, prefix = '{0}{1}.'.format(prefix, md[0]), level = 4)

def proccessClass(cl, f):
    writeClass(cl, f)
    baseMems = inspect.getmembers(cl[1].__bases__[0])
    for m in inspect.getmembers(cl[1]):
        if m[0][0] == '_' or m in baseMems:
            pass
        elif inspect.isfunction(m[1]):
            writeFunc(m, f, prefix = '{}.'.format(cl[0]), level = 4)


def main(args):
    wDir = os.path.expanduser(os.path.normpath(args.dir))
    if not os.path.isdir(wDir):
        try:
            os.mkdir(wDir)
        except OSError:
            print('Creating the directory {} failed'.format(os.dir))
            return 1
    classes = []
    funcs = []
    vrs = []
    builtins = []
    mods = []
    for m in inspect.getmembers(isilib):
        if inspect.ismodule(m[1]):
            if m[0] in documentedModules:
                mods.append(m)
        elif inspect.isbuiltin(m[1]) or m[0][0] == '_':
            builtins.append(m)
        elif inspect.isclass(m[1]):
            classes.append(m)
        elif inspect.isfunction(m[1]):
            funcs.append(m)
        else:
            vrs.append(m)
    f = open(os.path.expanduser(os.path.normpath(args.dir + '/' + args.output)), 'w')
    f.write(jekyllyHeader)
    #f.write('# <a name="{0}"></a> {0}\n\n'.format('isilib'))
    f.write(isilib.__doc__ + '\n')
    f.write('## Classes\n\n')
    first = True
    for c in classes:
        if first:
            first = False
        else:
            f.write("- - -\n\n")
        proccessClass(c, f)
    f.write('## Functions\n\n')
    first = True
    for fnc in funcs:
        if first:
            first = False
        else:
            f.write("- - -\n\n")
        writeFunc(fnc, f)
    for m in mods:
        writeMod(m, f, prefix = 'isilib.', level = 2)
    f.close()
    #print(inspect.getmembers(mods[0][1]))

if __name__ == '__main__':
    args = argumentParser()
    main(args)
