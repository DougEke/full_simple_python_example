"""
Although a little over kill here, but this is a simple demo of a class implementing
an abstract class and implementing the abstract class method
"""

import os
from abtractLogger import AbstractLogger


class FileWriter(AbstractLogger):
    def writeFile(self, filename, msgtowrite):
        f = open(filename, "a")
        f.write(msgtowrite)
        f.close()

    # Need to check that the exists so that we can read from it, otherwise
    # lets just show a message that it doens't exist.
    def readFile(self, file):
        if os.path.exists(file):
            return open(file).read()
        else:
            print(f"{file} does not exists..")

    # We'll just check that the file exists first
    def deleteFile(self, file):
        if os.path.exists(file):
            os.remove(file)
        else:
            print(f"{file} does not exists..")
