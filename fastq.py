  
import gzip
import os,sys
from smart_open import open


def isFastq(f):
    fqext = (".fq", ".fastq", "fq.gz", ".fastq.gz")
    for ext in fqext:
        if f.endswith(ext):
            return True
    return False

################################
#fastq.reader

class Reader:

    def __init__(self, fname):
        self.__file = None
        self.__gz = False
        self.__eof = False
        self.filename = fname
        if self.filename.endswith(".gz"):
            self.__gz = True
            #self.__file = gzip.open(self.filename, "r")
            self.__file = open(self.filename, "r")
        else:
            self.__gz = False
            self.__file = open(self.filename, "r")
        if self.__file == None:
            print("Failed to open file " + self.filename)
            sys.exit(1)
            
    def __del__(self):
        if self.__file != None:
            self.__file.close()
            
    def nextRead(self):
        if self.__eof == True or self.__file == None:
            return None

        lines = []
        for i in range(0,4):
            line = self.__file.readline().rstrip()
            if len(line) == 0:
                self.__eof = True
                return None
            lines.append(line)
        return lines

    def isEOF(self):
        return False