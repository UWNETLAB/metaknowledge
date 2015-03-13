#!/usr/bin/env python2
#Written by Reid McIlroy-Young for John McLevey

import os
import sys
import csv
import networkx as nx


#If edges have weight <= cutoff they are removed
cutoff = 3

#output files names
csvOutFile = "co-authorshipNetwork.csv"
graphOutFile = "co-authorshipNetwork.graphml"
GEXFOutFile = "co-authorshipNetwork.gexf"
GMLOutFile = "co-authorshipNetwork.gml"

#The separator used in the output csv
csvSeparator = '|'

#flags for changing the output files
outputCSV = True
outputgraphml = True
ouputGEXF = False
ouputGML = False

csvHeader = ['Author', 'Number of Papers', 'Co-authors', 'Number of Co-authors']

class BadPaper(Exception):
    pass

def netPaper(index, flines, graph):
    """
    Reads flines Starting at index and checks for the AF flag or a flag given in
    importantData. AF go to authorls creating a list of the authors full
    names while the rest go to importdict, a dict of paper data.
    Then the authors are added to the graph if missing and edged between them
    are created or increased in weight.
    Papers not starting with PT will throw an Exception
    """
    loc = index
    if 'PT' not in flines[loc]:
        raise BadPaper("Bad paper " + str(flines[index - 1 : index + 2]))
    authorls = []
    importdict = {}
    try:
        while 'ER' not in flines[loc][:2]:
            if 'AF' in flines[loc][:2]:
                authorls = flines[loc].split('\t')
            loc += 1
    except BadPaper as e:
        raise type(e)(e.message + str(loc + 1) + ": " + flines[loc][:-1])
    except Exception as e:
        print "readPaper Exception:"
        print "currentVal = " + str(currentVal)
        print "loc = " + str(loc)
        print "flines[loc] = " + flines[loc],
        print rowDict
        raise type(e)(e.message + " While loop Exception.")
    if 'ER' not in flines[loc]:
        raise BadPaper("Paper terminator is not valid: " + flines[loc][:-1])
    for author in authorls:
        if author not in graph:
            graph.add_node(author)
            graph.node[author][csvHeader[1]] = 1
        else:
            graph.node[author][csvHeader[1]] += 1
    for author1 in authorls:
        for author2 in authorls[authorls.index(author1) + 1:]:
            if graph.has_edge(author1, author2):
                graph.edge[author1][author2]['weight'] += 1
            else:
                graph.add_edge(author1, author2, weight = 1)
    loc += 1
    return loc

def readFiles(fls, grph):
    """
    readFiles goes through the files in fls checks if they have valid headers
    then strips out all the superfluous lines and runs netPaper on each paper.
    readFiles will throw an Exception if the file does not begin or end
    correctly.
    """
    for fname in fls:
        print "Reading " + fname
        namesplit = fname[:-4].split('_')
        if len(namesplit) < 3:
            print fname + " is not a valid file name, it will be skipped"
        else:
            readisi = open(fname,"r").read().replace('\n   ','\t').split('\n')
            if "VR 1.0" not in readisi[1] and "VR 1.0" not in readisi[0]:
                    #checks that the txt has the right header
                    print "Wrong header in found in " + fname
                    print readisi[0],
                    print readisi[1],
                    print fname + " will be skipped"
            else:
                fileIndex = 2
                while fileIndex < len(readisi) - 1:
                    if readisi[fileIndex].isspace() or not readisi[fileIndex]:
                        fileIndex += 1
                    elif 'EF' in readisi[fileIndex][:2]:
                        if fileIndex != len(readisi) - 1:
                            print fname + " does not end at ER"
                            print "EF is at " + str(fileIndex + 1)
                            print fname + " ends at " + str(len(readisi) + 1)
                            print "Papers after " + str(fileIndex + 1) + " will not be recorded"
                        break
                    else:
                        try:
                            fileIndex = netPaper(fileIndex, readisi, grph)
                        except BadPaper as e:
                            print e
                            print "skipping the rest of " + fname
                            break
                        except Exception as e:
                            print type(e)
                            raise type(e)(e.message + " Exception in " + fname + " at line " + str(fileIndex + 1))

def csvMaker(grph, f):
    """
    Takes in a graph and file name and makes a csv file of name f with rows
    containing everything in csvHeader.
    """
    ocsv = csv.DictWriter(open(f, 'wb'), csvHeader, quotechar='"', quoting=csv.QUOTE_ALL)
    ocsv.writeheader()
    authdict = {}
    for auth in grph.nodes():
        authdict[csvHeader[0]] = auth
        authdict[csvHeader[1]] = grph.node[auth][csvHeader[1]]
        coAuths = grph.neighbors(auth)
        if len(coAuths) > 0:
            authdict[csvHeader[2]] = coAuths[0]
            for coAuth in coAuths[1:]:
                authdict[csvHeader[2]] += csvSeparator + coAuth
            authdict[csvHeader[3]] = len(coAuths)
        else:
            authdict[csvHeader[2]] = ''
            authdict[csvHeader[3]] = 0
        ocsv.writerow(authdict)

if __name__ == '__main__':
    if os.path.isfile(csvOutFile) and outputCSV:
        #Checks if the output csv already exists and terminates if so
        print csvOutFile +  " already exists\nexisting"
        sys.exit()
        #os.remove(csvOutFile)
    if (os.path.isfile(graphOutFile)) and outputgraphml:
        #Checks if the output graphml already exists and terminates if so
        print graphOutFile +  " already exists\nexiting"
        sys.exit()
        #os.remove(graphOutFile)
    if os.path.isfile(GEXFOutFile) and ouputGEXF:
        #Checks if the output GEXF already exists and terminates if so
        print GEXFOutFile +  " already exists\nexisting"
        sys.exit()
        #os.remove(GEXFOutFile)
    if os.path.isfile(GMLOutFile) and ouputGML:
        #Checks if the output GML already exists and terminates if so
        print GMLOutFile +  " already exists\nexisting"
        sys.exit()
        #os.remove(GMLOutFile)
    flist = [f for f in os.listdir(".") if f.endswith(".txt")] #Creates list of all .txt in the directory
    if len(flist) == 0:
        #checks for any valid files
        print "No txt Files"
        sys.exit()
    else:
        #Tells how many files were found
        print "Found " + str(len(flist)) + " txt files"
    G = nx.Graph()
    readFiles(flist, G)
    if outputCSV:
        print "Making csv"
        print "Writing " + csvOutFile
        csvMaker(G, csvOutFile)
    for ed in G.edges():
            if G.edge[ed[0]][ed[1]]['weight'] <= cutoff:
                  G.remove_edge(ed[0],ed[1])
    if outputgraphml:
        print "Making graphml"
        print "Writing " + graphOutFile
        nx.write_graphml(G, graphOutFile)
    if ouputGEXF:
        print "Making GEXF"
        print "Writing " + GEXFOutFile
        nx.write_gexf(G, GEXFOutFile)
    if ouputGML:
        print "Making GML"
        print "Writing " + GMLOutFile
        nx.write_gml(G, GMLOutFile)
    print "Done"