from dataclasses import dataclass

"""
The @dataclass is not needed here as this, ineffect, replaces the properties and setters sections
"""
# @dataclass(slots = True)
class Book:
    def __init__(self, author, title, isbn):
        self.__author = author
        self.__title = title
        self.__isbn = isbn

    """
    Properties
    This will enable you to retrieve the attributes values.
    """
    @property
    def author(self):
        return self.__author
    
    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn

    """
    Setters
    these properties will enable you to update the attributs value.
    """
    @author.setter
    def author(self, author):
        self.__author = author

    @title.setter
    def title(self, title):
        self.__title = title

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    """
    A simple set of functions that return the data information
    """
    def bookinfo(self):
        print(f"Author: {self.__author}, Title: {self.__title}, ISBN: {self.__isbn}")

    def __str__(self):
        return f"Author: {self.author}, Title: {self.title}, ISBN: {self.isbn}"
    
    def __repr__(self):        
        return f"Author: {self.author}, Title: {self.title}, ISBN: {self.isbn}"