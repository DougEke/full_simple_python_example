"""
Name: Borrower.py
Description: This is a simple class that holds the details of a borrower of a specific book.

Person  : This can either be a Member or Guest object of type Person
Book    : A Book object that holds the details of a specific book
"""

from dataclasses import dataclass
from datetime import date

from book import Book
from person import Person


@dataclass
class Borrower:
    person: Person
    book: Book
    loan_date: date

    def __init__(self, person: Person, book: Book, date):
        self.person = person
        self.book = book
        self.loan_date = date

    # # Display the information of the borrower...
    def borrowerInfo(self):
        return f"\n***Borrower***\nDate: {self.loan_date}\nName: {self.person}\nBook: {self.book}"


# @dataclass
# class Borrower:
#     def __init__(self, person: Person, book: Book, date):
#         self.__person = person
#         self.__book = book
#         self.__date = date

#     @property
#     def person(self):
#         return self.__person

#     @property
#     def book(self):
#         return self.__book

#     @property
#     def date(self):
#         return self.__date

#     # Display the information of the borrower...
#     def borrowerInfo(self):
#         return f"\n***Borrower***\nDate: {self.date}\nName: {self.person}\nBook: {self.book}"
