import os
import sys
import time
import math
import threading

class _ProgressBar(object):
    difTermAndBar = 8 #the number of characters difference between the bar's length and the terminal's width
    timeLength = 6 # width of elapse time display
    percLength = 6 # width of percent display
    def __init__(self, initPer, initString = ' ', output = sys.stdout, secondRow = False, dummy = False):
        self.dummy = dummy
        self.finished = False
        self.big = secondRow
        self.per = initPer
        self.out = output
        self.inputString = initString
        if not dummy:
            self.sTime = time.time()
            try:
                self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
                if self.barMaxLength < 0:
                    self.barMaxLength = 0
            except OSError:
                self.barMaxLength = 80 - self.difTermAndBar
            except AttributeError:
                #Pypy fallback
                self.barMaxLength = 80 - self.difTermAndBar
            self.ioThread = threading.Thread(target = self.threadedUpdate, kwargs = {"self" : self})
            self.ioThread.daemon = True
            self.ioThread.start()

    def __bool__(self):
        return not self.dummy

    def __del__(self):
        if not self.dummy and not self.finished:
            self.finished = True
            self.ioThread.join()
            self.out.write('\n')
            self.out.flush()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__del__()

    def updateVal(self, inputPer, inputString = None):
        self.per = inputPer
        if inputString is not None:
            self.inputString = inputString

    def finish(self, inputString):
        if not self.dummy:
            self.finished = True
            self.inputString = str(inputString)
            self.ioThread.join()
            try:
                self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
                if self.barMaxLength < 0:
                    self.barMaxLength = 0
            except OSError:
                self.barMaxLength = 80 - self.difTermAndBar
            except AttributeError:
                #Pypy fallback
                self.barMaxLength = 80 - self.difTermAndBar
            if self.big:
                self.out.write('\n' + ' ' * (self.barMaxLength + self.difTermAndBar) + '\033[F')
            else:
                self.out.write('\r')
            if len(self.inputString) < self.barMaxLength + self.difTermAndBar - self.timeLength:
                tString = self.prepTime(time.time() - self.sTime, self.barMaxLength + self.difTermAndBar - len(self.inputString) - 1)
                self.out.write(self.inputString + ' ' + tString)
            else:
                self.out.write(self.prepString(self.inputString, self.barMaxLength + self.difTermAndBar - self.timeLength) + self.prepTime(time.time() - self.sTime, self.timeLength))
            self.out.write('\n')
            self.out.flush()

    def jumpUp(self):
        self.out.write('\033[F')
        self.out.flush()

    @staticmethod
    def prepString(s, maxLength):
        maxLength = maxLength - 1
        sString = str(s)
        if len(sString) <= maxLength:
            return sString.ljust(maxLength, ' ') + ' '
        else:
            if maxLength % 2 == 0:
                return sString[:int(maxLength/2 - 3)] + '...' + sString[int(-maxLength/2):] + ' '
            else:
                return sString[:int(maxLength/2 - 2)] + '...' + sString[int(-maxLength/2):] + ' '

    @staticmethod
    def prepTime(t, maxLength):
        try:
            if math.log10(t) + 3.01 > maxLength:
                return "{1:{0}.0E}s".format(maxLength - 1 ,t)
            else:
                return "{1:{0}.1f}s".format(maxLength - 1,t)
        except ValueError:
            return "{1:{0}.1f}s".format(maxLength - 1,t)

    @staticmethod
    def threadedUpdate(self = None):
        while not self.finished:
            try:
                self.barMaxLength = os.get_terminal_size(self.out.fileno()).columns - self.difTermAndBar
                if self.barMaxLength < 0:
                    self.barMaxLength = 0
            except OSError:
                self.barMaxLength = 80 - self.difTermAndBar
            except AttributeError:
                #Pypy fallback
                self.barMaxLength = 80 - self.difTermAndBar
            self.out.write('\r')
            percentString = '{:.1%}'.format(self.per).rjust(self.percLength, ' ')
            barLength = int(self.per * self.barMaxLength)
            if self.big and self.inputString:
                self.dString = self.prepString(self.inputString, self.barMaxLength + self.difTermAndBar - self.timeLength) + self.prepTime(time.time() - self.sTime, self.timeLength)
                if barLength >= self.barMaxLength:
                    self.out.write('[' + '=' * barLength + ']' + percentString)
                    self.out.write('\n' + self.dString + '\033[F')
                else:
                    self.out.write('[' + '=' * barLength + '>' + ' ' * (self.barMaxLength - barLength - 1) + ']' + percentString)
                    self.out.write('\n' + self.dString + '\033[')
            elif self.inputString:
                self.dString = self.prepString(self.inputString, self.barMaxLength + self.difTermAndBar - self.timeLength - self.percLength - 2) + '[' + self.prepTime(time.time() - self.sTime, self.timeLength) +  ']' + percentString
                self.out.write(self.dString)
            else:
                if barLength >= self.barMaxLength:
                    self.out.write('[' + '=' * barLength + ']' + percentString + '\r')
                else:
                    self.out.write('[' + '=' * barLength + '>' + ' ' * (self.barMaxLength - barLength - 1) + ']' + percentString + '\r')
            self.out.flush()
            time.sleep(.1)
