#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import argparse
import re
import os.path
import subprocess

args = argparse.Namespace()
codeRegex = re.compile(r'\[([0-9]*)\](.*)')

startString = """{
 "cells": [
  """

endString = """  ],
 "metadata": {
   "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
 },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}"""

def argumentParser():
    parser = argparse.ArgumentParser(description="A simple script to convert markdown (.md) files to iPython Notebooks (.ipynb)")
    #parser.add_argument("--output", "-o")
    #parser.add_argument("--execute", "-e", action = "store_true", default = False)
    parser.add_argument("files", type=argparse.FileType('r'), default = [], nargs = '*')

    return parser.parse_args()

def convertString(file):
    currentExNum = float('inf')
    currentBufferType = ''
    stringBuffer = ''
    stringResult = []
    for line in file.readlines():
        code = re.match(codeRegex,line)
        if stringBuffer == '':
            if code:
                stringBuffer = code.group(2) + '\n'
                currentExNum = code.group(1)
                currentBufferType = 'py'
            else:
                stringBuffer = line
                currentBufferType = 'md'
                currentExNum = float('inf')
        else:
            if code:
                if currentBufferType == 'py' and currentExNum == code.group(1):
                    stringBuffer += code.group(2) + '\n'
                elif currentBufferType == 'py':
                    stringResult.append(writePYcell(stringBuffer, currentExNum))
                    stringBuffer = code.group(2)+ '\n'
                    currentExNum = code.group(1)
                    currentBufferType = 'py'
                else:
                    stringResult.append(writeMDcell(stringBuffer))
                    stringBuffer = code.group(2)+ '\n'
                    currentExNum = code.group(1)
                    currentBufferType = 'py'
            else:
                if currentBufferType == 'md':
                    if line == '\n' and stringBuffer[-2:] == '\n\n':
                        stringResult.append(writeMDcell(stringBuffer[:-1]))
                        stringBuffer = ''
                        currentBufferType = ''
                    else:
                        stringBuffer += line
                else:
                    stringResult.append(writePYcell(stringBuffer, currentExNum))
                    stringBuffer = line
                    currentBufferType = 'md'
                    currentExNum = float('inf')
    if stringBuffer != '':
        if currentBufferType == 'md':
            stringResult.append(writeMDcell(stringBuffer))
        else:
            stringResult.append(writePYcell(stringBuffer, excount = currentExNum))
    return startString + ',\n  '.join(stringResult) + endString

def convert(file):
    nameCompts = os.path.splitext( os.path.expanduser(os.path.normpath(file.name)))
    fileName = nameCompts[0] + '.ipynb'
    outFile = open(fileName, 'w+')
    outFile.write(convertString(file))
    return fileName


def stringPreprossesing(s):
    s = s.lstrip('\n')
    s = s.replace(r'"', r'\"')
    s = s.replace('\n', '\\n",\n     "')[:-11]
    return s


def writeMDcell(s):
    return """{{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
    "{0}"
   ]
  }}""".format(stringPreprossesing(s))

def writePYcell(s, excount = ''):
    return """{{
   "cell_type": "code",
   "execution_count": null,
   "metadata": {{
     "collapsed": false
   }},
   "outputs": [],
   "source": [
    "{}"
   ]
  }}""".format(stringPreprossesing(s))

def mkMdToNb():
    args = argumentParser()
    for f in args.files:
        fname = convert(f)
if __name__ =='__main__':
    mkMdToNb()
