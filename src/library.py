"""
A simple class that allows the adding, removing and displaying of borrowers of books.
The borrowers are stored within a dictionary that takes a simple id and a Borrower object
"""
import datetime
import logging  # Used for logging, using the inbuilt logging facility

from borrower import Borrower
from filewriter import FileWriter
from book import Book
from person import Person

borrowers = {}
filewriter = FileWriter()
filename = "library.txt"

# Format the logging so that it writes to a log file....
logging.basicConfig(filename="logfile.txt", encoding="utf-8", level=logging.INFO)

"""
Description: Add a borrower to the system

id      : Id of the borrower entry
person  : Person object of the borrower
book    : Book object of the book being borrowed
"""


def addBorrower(id, person: Person, book: Book):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    borrowers.update({id: Borrower(person, book, date)})
    print(f"\n===> New borrower added to the system: {person.name}...")

    # Log the fact the new borrower has borrowed a book and been added to the system
    filewriter.writeFile(
        filename, f"[{date}] - New borrower added: {person.name}, Book: {book.title}\n"
    )

    # log that a file has ben added via the inbuilt logging facility from python
    logging.info(f"[{date}] - New borrower added: {person.name}, Book: {book.title}")


"""
Description: Display the current borrowers within the system
"""


def displayBorrowers():
    for borrower in borrowers.values():
        print(borrower.borrowerInfo())


def removeBorrower(name):
    borrowers.pop(name)


def getNumberOfBorrowers():
    return len(borrowers)


def readFile():
    return filewriter.readFile(filename)


def removeFile():
    filewriter.deleteFile(filename)
