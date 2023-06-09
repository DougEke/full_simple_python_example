"""
This is a simple super class that will be used for inheriting into the Member nad Guest classes
"""
from datetime import date
from dataclasses import dataclass

"""
We're using the @dataclass tag here so don'tneed to supply any property or setter
functions, as well as a display function.
"""
@dataclass
class Person:
    def __init__(self, name, dob):
        self.__name = name
        self.__age = self.calculateAge(dob)

    @classmethod
    def calculateAge(self, dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age