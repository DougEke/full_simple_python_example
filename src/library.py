"""
A simple class that allows the adding, removing and displaying of borrowers of books.
The borrowers are stored within a dictionary that takes a simple id and a Borrower object
"""
import datetime

from borrower import Borrower
from logger import Logger
from book import Book
from person import Person

class Library:
    def __init__(self):
        self.borrowers = {}
        self.logger = Logger()
        self.__logFIleName = "logger.txt"

    """
    Description: Add a borrower to the system

    id      : Id of the borrower entry
    person  : Person object of the borrower
    book    : Book object of the book being borrowed
    """
    def addBorrower(self, id, person: Person, book: Book):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.borrowers.update({id: Borrower(person, book, date)})
        print(f"\n===> New borrower added to the system: {person.name}...\n")

        # Log the fact the new borrower has borrowed a book and been added to the system
        self.logger.log(self.__logFIleName, f"[{date}] - New borrower added: {person.name}, Book: {book.title}\n")

    """
    Description: Display the current borrowers within the system
    """
    def displayBorrowers(self):
        for borrower in self.borrowers.values():
            print(borrower.borrowerInfo())
       
    def removeBorrower(self, name):
        self.borrowers.pop(name)

    def getNumberOfBorrowers(self):
        return len(self.borrowers)
    
    def readLog(self):
        return self.logger.readLog(self.__logFIleName)
    
    def removeLog(self):
        self.logger.deleteLogFile(self.__logFIleName)