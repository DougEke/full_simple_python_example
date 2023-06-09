"""
Python has no concept of interfaces like other OO languages, such as C++, C# and Java,
so to get round this we can create an abstratc class that kind of does both jobs.

Although a little over kill here, but this is a simple demo of an abstract class
declaring it's abstract method. Here the method isn't defined as this wolud be carried
out within the class that implements it.
"""

from abc import ABC, abstractmethod

class AbstractLogger:

    @abstractmethod
    def log(self):
        pass