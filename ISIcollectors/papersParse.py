#Written by Reid McIlroy-Young
#Useful functions for parsing isi files

class BadPaper(Warning):
    """
    Exception thrown by paperParser and isiParser for mis-formated papers
    """
    pass

def paperParser(paper):
    """
    paperParser reads paper until it reaches 'EF' for each field tag it adds an
    entry to the returned dict with the tag as the key and a list of the entries
    for the tag as the value, the list has each line as an entry.   
    """
    tdict = {}
    currentTag = ''
    for l in paper:
        if 'ER' in l[:2]:
            return tdict
        elif '   ' in l[:3]: #the string is three spaces in row
            tdict[currentTag].append(l[3:-1])
        elif l[2] == ' ':
            currentTag = l[:2]
            tdict[currentTag] = [l[3:-1]]
        else:
            raise BadPaper("Field tag not formed correctly: " + l)
    raise BadPaper("End of file reached before EF")

def isiParser(isifile):
    """
    isiParser reads a file, checks that the header is correct then reads each
    paper returning a list of of dicts keyed with the field tags.
    """
    f = open(isifile, 'r')
    if "VR 1.0" not in f.readline() and "VR 1.0" not in f.readline():
        raise BadPaper(isifile + " Does not have a valid header")
    notEnd = True
    plst = []
    while notEnd:
        try:
            l = f.next()
        except StopIteration as e:
            raise BadPaper("File ends before EF found")
        if not l:
            raise BadPaper("No ER found in " + isifile)
        elif l.isspace():
            continue
        elif 'EF' in l[:2]:
            notEnd = False
            continue
        else:
            try:
                if l[:2] != 'PT':
                    raise BadPaper("Paper does not start with PT tag")
                plst.append(paperParser(f))
                plst[-1][l[:2]] = l[3:-1]
            except Warning as w:
                raise BadPaper(str(w.message) + "In " + isifile)
            except Exception as e:
                 raise e
    try:
        f.next()
        print "EF not at end of " + isifile
    except StopIteration as e:
        pass
    finally:
        return plst

def getFiles(suffix):
    """
    getFiles reads the current directory and returns all files ending with
    suffix. Terminates the program if none are found, no exceptions thrown.
    """
    fls = sys.argv[1:] if sys.argv[1:] else [f for f in os.listdir(".") if f.endswith(suffix)]
    if len(fls) == 0:
        #checks for any valid files
        print "No " + suffix + " Files"
        sys.exit()
    pubFormatFiles = [] 
    citeFormatFiles = []
    miscFiles = []
    for fname in fls:
        slst = fname.split('_')
        if len(slst) < 3:
            miscFiles.append(fname)
        elif "cited" in slst[2].lower():
            citeFormatFiles.append(fname)
        elif "pubs" in slst[2][:4].lower():
            pubFormatFiles.append(fname)
        else:
            miscFiles.append(fname)
    else:
        #Tells how many files were found
        print str(len(pubFormatFiles)) + " PUBS, " + str(len(citeFormatFiles)) + " CITED and " + str(len(miscFiles)) + " miscellaneous files found."
    return [pubFormatFiles, citeFormatFiles, miscFiles]