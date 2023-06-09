"""
Although a little over kill here, but this is a simple demo of a class implementing
an abstract class and implementing the abstract class method
"""

import os
from abtractLogger import AbstractLogger

class Logger(AbstractLogger):

    def log(self, logFilename, msgtolog):
        f = open(logFilename, "a")
        f.write(msgtolog)
        f.close()

    # Need to check that the exists so that we can read from it, otherwise
    # lets just show a message that it doens't exist.
    def readLog(self, file):
        if os.path.exists(file):
            return open(file).read()
        else:
            print(f"{file} does not exists..")
    
    # We'll just check that the file exists first
    def deleteLogFile(self, file):
        if os.path.exists(file):
            os.remove(file)
        else:
            print(f"{file} does not exists..")

