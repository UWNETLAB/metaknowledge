#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import metaknowledge
import metaknowledge.journalAbbreviations
import networkx as nx
import argparse
import os
import sys
import readline
import collections
import code
import platform

#TODO: Figure output name stuff

#These are used when the user goes to the interactive terminal, so they must be global
RC = None
G = None

def argumentParser():
    parser = argparse.ArgumentParser(description="metaknowledge's simple command line interface")
    parser.add_argument("files", default = [], nargs = '*')
    parser.add_argument("--verbose", "-v", action = 'store_true' , default = False, help = "Verbose mode, every step is printed")
    parser.add_argument("--name", "-n",  default = False, help = "The name used for the recordCollection and resulting files.")
    parser.add_argument("--debug", "-d", action = 'store_true', default = False, help = "Enables debug messages.")
    parser.add_argument("--quiet", "-q", action = 'store_true', default = False, help = "Disables the progress bar. Progress bars only works on some operating system, if it does not work it will be disabled")
    parser.add_argument("--suffix", "-s", default = '', help = "The suffix of the WOS files you wish to extract Records from, by default all files are used and those that do not have Records are skipped")
    return parser.parse_args()

def yesorNo(prompt):
    while True:
        val = input(prompt).upper()
        if val == 'Y' or val == '':
            return True
        elif val == 'N':
            return False
        else:
            pass

def inputMenu(inputDict, header = None, footer = None, errorMsg = 'That is not an option please select a different value.', promptMsg = 'What is your selection: ', extraOptions = True):
    s = ''
    if header:
        s += '{}\n'.format(header)
    for k in inputDict.keys():
        s += '{0}) {1}\n'.format(k,inputDict[k])
    if extraOptions:
        s += 'i) open python console\n'
        s += 'q) quit\n'
    if footer:
        s += '{}\n'.format(footer)
    print(s, end = '')
    selection = input(promptMsg)
    if selection in inputDict:
        return selection
    elif extraOptions and selection == 'q':
        sys.exit()
    elif extraOptions and selection == 'i':
        bannerMsg = 'Python {0} on {1}\nType "help", "copyright", "credits" or "license" for more information.\nmetaknowledge is imported as "metaknowledge" and Networkx is imported as "nx".\n'.format(sys.version, platform.system())
        if RC:
            bannerMsg += "The metaknowledge RecordCollection is called 'RC'"
            if G:
                bannerMsg += " and the Networkx graph is called 'G'."
            else:
                bannerMsg += '.'
        code.interact(local = globals(), banner = bannerMsg)
    else:
        print('\033[93m\a' + errorMsg + '\033[0m') #Not windows compatible
        return inputMenu(inputDict, header = header, footer = footer, errorMsg = errorMsg, promptMsg = promptMsg)

def getOutputName(clargs, suffix, prompt = "What do you wish to call the output file? ", errorMsg = 'That is not a valid file name.', checking = True):
    if clargs.name:
        return clargs.name + suffix
    s  = input(prompt) + suffix
    if len(s) == 0:
        print(errorMsg)
        return getOutputName(clargs, suffix, prompt = prompt, errorMsg = errorMsg)
    else:
        if os.path.lexists(s) and checking:
            overWrite = yesorNo("{} already exists overwrite (y/n)? ".format(s))
            if overWrite:
                return s
            else:
                return getOutputName(clargs, suffix, prompt = prompt, errorMsg = errorMsg)
        else:
            return s

def Tag(prompt, collection, nMode = False):
    retTag = input(prompt).upper()
    if retTag in collection.tags():
        return retTag
    else:
        if nMode and retTag == '':
            return False
        else:
            print("{} is not a tag in any of the Records, please try again".format(retTag))
            return Tag(prompt, collection, nMode = nMode)

def getNum(prompt):
    retNum = input(prompt)
    try:
        return float(retNum)
    except ValueError:
        print("{} is not a number, please try again".format(retNum))
        return getNum(prompt)

def getFiles(args):
    tmpRC = metaknowledge.RecordCollection(name = '')
    if len(args.files) > 0:
        for f in args.files:
            path = os.path.abspath(os.path.expanduser(f))
            if os.path.exists(path):
                tmpRC |= metaknowledge.RecordCollection(path, extension = args.suffix)
            else:
                raise TypeError(path + " is not an existing file or directory")
        if args.name:
            tmpRC._repr = args.name
        else:
            FileNames = [os.path.basename(nm) for nm in args.files]
            if len(FileNames) == 1:
                tmpRC._repr = "WOS files from: {}".format(FileNames[0])
            else:
                tmpRC._repr = "WOS files from: {0} and {1}".format(', '.join(FileNames[:-1]), FileNames[-1])
        return tmpRC
    else:
        nflist = input("What files or directorys do you want to extract a network from: ")
        paths = [os.path.abspath(os.path.expanduser(f)) for f in nflist.split(' ')]
        badPaths = [f for f in paths if not os.path.exists(f)]
        if len(badPaths) > 1:
            print(', '.join(badPaths[:-1]) + " and " + badPaths[-1] + " are not existing files or directorys")
            args.files = []
            return getFiles(args)
        elif len(badPaths) == 1:
            print(badPaths[0] + " is not an existing file or directory")
            args.files = []
            return getFiles(args)
        else:
            args.files = paths
            return getFiles(args)

def getWhatToDo(clargs, inRC):
    promptDict = collections.OrderedDict([
    ('1', "Make a graph"),
    ('2', "Write the collection as a single WOS style file"),
    ('3', "Write the collection as a single WOS style file and make a graph"),
    ('4', "Write the collection as a single csv file"),
    ('5', "Write the collection as a single csv file and make a graph"),
    ('6', "Write all the citations to a single file"),
    ('7', "Go over non-journal citations"),
    ])
    print("A collection of {0} WOS records has been created".format(len(inRC)))
    optionNum = int(inputMenu(promptDict, header = "What do you wish to do with it:"))
    if optionNum == 1:
        return True
    elif optionNum == 2 or optionNum == 3:
        fName = getOutputName(clargs, '.txt')
        print("Writing {}".format(fName))
        inRC.writeFile(fname = fName)
        if optionNum == 2:
            return False
        else:
            return True
    elif optionNum == 4 or optionNum == 5:
        fName = getOutputName(clargs, '.csv')
        print("Writing {}".format(fName))
        inRC.writeCSV(fname = fName)
        if optionNum == 4:
            return False
        else:
            return True
    elif optionNum == 6:
        drop = yesorNo("Write only journals (y/n)? ")
        cites = []
        for R in inRC:
            if drop:
                cites += [str(c) + '\n' for c in R.get('citations', []) if c.isJournal()]
            else:
                cites += [str(c) + '\n' for c in R.get('citations', [])]
        fName = getOutputName(clargs, '.csv')
        cites = set(cites)
        print("Writing {}".format(fName))
        with open(fName, 'w') as f:
            f.writelines(cites)
        return False
    else:
        dbName = input("The default manual databse file is called {}, press Enter to use it or type the name of the database you wish to use:\n".format(metaknowledge.journalAbbreviations.manualDBname))
        print("Starting to go over citations, to exit press ctr-C.")
        if dbName == '':
            dbName = metaknowledge.journalAbbreviations.manualDBname
        try:
            for R in inRC:
                for c in R.get('citations', []):
                    if not hasattr(c, 'journal'):
                        print("{} does not have a journal field".format(c))
                    elif c.isJournal(manualDB= dbName, returnDict ='both'):
                        print("the journal field of {} is in the database".format(c.journal))
                    elif c.isJournal(manualDB= dbName, returnDict ='both', checkIfExcluded = True):
                        print("the journal field of {} is in the database marked to be skipped".format(c.journal))
                    else:
                        addToDB = yesorNo("The citation {} has the journal field:\n{} add as a journal (y/n)? ".format(c, c.journal))
                        if addToDB:
                            c.addToDB(manualDB= dbName)
                            print("{} added as a journal abbrviation.".format(c.journal))
                        else:
                            c.addToDB(invert = True)
                            print("{} will now be skipped".format(c.journal))
        except KeyboardInterrupt:
            print('\nExiting manual citation clasification', end = '')
            raise
        else:
            print('Done manual citation clasification')
            return False



def getNetwork(clargs, inRC):
    netsDict = collections.OrderedDict([
    ('1', "a one-mode network"),
    ('2', "a two-mode network"),
    ('3', "an n-mode network"),
    ('4', "a citation network"),
    ('5', "a co-citation network"),
    ('6', "a co-authorship network"),
    ])
    netID = int(inputMenu(netsDict, header = "What type of network do you wish to create?", promptMsg = "Input the number corresponding to the type of network you wish to generate? "))
    if netID == 1:
        otg = Tag("What is the tag to use for the network? ", inRC)
        print("Generating a network using the {0} tag.".format(otg), inRC)
        return inRC.networkOneMode(otg)
    elif netID == 2:
        tg1 = Tag("What is the first tag to use for the network? ", inRC)
        tg2 = Tag("And the second tag? ", inRC)
        print("Generating a network using the {0} and {1} tags.".format(tg1, tg2))
        return inRC.networkTwoMode(tg1, tg2)
    elif netID == 3:
        tgs = []
        tgs.append(Tag("What is the first tag to use for the network? ", inRC))
        innertag = Tag("And the next tag (leave blank to continue)? ", inRC, nMode = True)
        while innertag:
            tgs.append(innertag)
            innertag = Tag("And the next tag (leave blank to continue)? ", inRC, nMode = True)
        print("Generating a network using the {0} and {1} tags".format(', '.join(tgs[:-1]), tgs[-1]))
        return inRC.networkMultiMode(tgs)
    elif netID == 4:
        print("Generating citation network")
        return inRC.networkCitation()
    elif netID == 5:
        print("Generating co-citation network")
        return inRC.networkCoCitation()
    else:
        print("Generating co-authorship network")
        return inRC.networkCoAuthor()

def getThresholds(clargs, grph):
    thresDict = collections.OrderedDict([
    ('0', "Continue"),
    ('1', "Drop isolates"),
    ('2', "Remove self loops"),
    ('3', "Remove edges below some weight"),
    ('4', "Remove edges above some weight"),
    ('5', "Remove nodes below some degree"),
    ('6', "Remove nodes above some degree"),
    ])
    print("The network contains {0} nodes and {1} edges, of which {2} are isolated and {3} are self loops.".format(len(list(grph.nodes())), len(list(grph.edges())), len(list(nx.isolates(grph))), len(list(nx.selfloop_edges(grph)))))
    thresID = int(inputMenu(thresDict, header = "What type of filtering to you want? "))
    if thresID == 0:
        return grph
    elif thresID == 1:
        metaknowledge.dropNodesByDegree(grph, minDegree = 1)
        return getThresholds(clargs, grph)
    elif thresID == 2:
        metaknowledge.dropEdges(grph, dropSelfLoops = True)
        return getThresholds(clargs, grph)
    elif thresID == 3:
        metaknowledge.dropEdges(grph, minWeight = getNum("What is the minumum weight for an edge to be included? "))
        return getThresholds(clargs, grph)
    elif thresID == 4:
        metaknowledge.dropEdges(grph, minWeight = getNum("What is the maximum weight for an edge to be included? "))
        return getThresholds(clargs, grph)
    elif thresID == 5:
        metaknowledge.dropNodesByDegree(grph, minDegree = getNum("What is the minumum degree for an edge to be included? "))
        return getThresholds(clargs, grph)
    else:
        metaknowledge.dropNodesByDegree(grph, minDegree = getNum("What is the maximum degree for an edge to be included? "))
        return getThresholds(clargs, grph)

def  outputNetwork(clargs, grph):
    outDict = collections.OrderedDict([
    ('1', "edge list and node attribute list"),
    ('2', "edge list"),
    ('3', "node attribute list"),
    ('4', "graphml (SLOW)"),
    ])
    try:
        import metaknowledge.contour
    except ImportError:
        import metaknowledge
    else:
        outDict['0'] = "view graph"
        outDict.move_to_end('0', last = False)
    print("The network contains {} nodes and {} edges.".format(len(grph.nodes()), len(grph.edges())))
    outID = int(inputMenu(outDict, header = "What type of output to you want? "))
    if outID == 0:
        metaknowledge.contour.quickVisual(grph)
        outputNetwork(clargs, grph)
    elif outID == 1:
        while True:
            try:
                outName = getOutputName(clargs, '', checking = False)
                metaknowledge.writeGraph(grph, outName, overwrite = False)
            except OSError:
                if clargs.name:
                    metaknowledge.writeGraph(grph, outName, overwrite = True)
                    break
                else:
                    overWrite = yesorNo("{}, overwrite (y/n)? ")
                    if overWrite:
                        metaknowledge.writeGraph(grph, outName, overwrite = True)
                        break
                    else:
                        pass
            else:
                break

    elif outID == 2:
        outName = getOutputName(clargs, '.csv')
        metaknowledge.writeEdgeList(grph, outName)
    elif outID == 3:
        outName = getOutputName(clargs, '.csv')
        metaknowledge.writeNodeAttributeFile(grph, outName)
    else:
        outName = getOutputName(clargs, '.graphml')
        nx.write_graphml(grph, outName)

def mkCLI():
    try:
        args = argumentParser()
        if args.quiet:
            metaknowledge.VERBOSE_MODE = False
        global RC
        RC = getFiles(args)
        makeNetwork = getWhatToDo(args, RC)
        if makeNetwork:
            global G
            G = getNetwork(args, RC)
            G = getThresholds(args, G)
            outputNetwork(args, G)
    except KeyboardInterrupt:
        print('')
        return 0
    except Exception as e:
        if args.debug:
            raise e
        else:
            print("A {0} error occured: {1}".format(type(e).__name__ ,e))
            return e
    else:
        return 1

if __name__ == "__main__":
    mkCLI()
