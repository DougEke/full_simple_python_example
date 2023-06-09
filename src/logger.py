"""
Although a little over kill here, but this is a simple demo of a class implementing
an abstract class and implementing the abstract class method
"""

from abtractLogger import AbstractLogger

class Logger(AbstractLogger):

    def log(self, msgtolog):
        f = open("logger.txt", "a")
        f.write(msgtolog)
        f.close()