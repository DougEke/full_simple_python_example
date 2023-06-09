"""
This is a simple test app that tests that things are working, not a formal test approach within python.
"""

import datetime
import uuid
from book import Book
from library import Library
from member import Member
from guest import Guest


library = Library()

"""
Functions need to be declared before they are used
"""
def createperson(name, dob, memno, type):
    # Guest takes name, dob, date
    if type == "guest":
        return Guest(name, dob, datetime.date.today())

    # Member takes, name, dob, memno
    return Member(name, dob, memno)

def createBook(author, title, isbn):
    return Book(author, title, isbn)

def getUUID():
    return uuid.uuid4()

"""
End of function declarations
"""

"""
main application function.
Not really needed s we could have simply just put all this outside of a function, but
kind of keeps it tidy, I believe.
"""
######################################Main Application Code#####################################
def main():
    # Simple check to see that the dictionary/library is empty
    print(f"Initial dictionary size: {library.getNumberOfBorrowers()}")

    # Create a person who is a member...
    person = Member("Doug", datetime.date(1982, 3, 5), "mem001")
    book = Book("J.K. Rowling", "Harry Potter", getUUID())
    library.addBorrower("1", person, book)

    # Lets just check that the borrower has been added:
    #   Should be 1 record
    #   Should just display 1 borrower
    print(f"===> Dictionary size: {library.getNumberOfBorrowers()}")
    library.displayBorrowers()

    # Create a guest via the createPerson function
    person = createperson("John Smith", datetime.date(1973, 5, 2), "123", "guest")
    book = createBook("Stephen King", "The Shining", uuid.uuid4())
    library.addBorrower("2", person, book)

    # Lets just check that the borrower has been added:
    #   Should be 2 records
    #   Should just display 2 borrowers
    print(f"\n===> Dictionary size: {library.getNumberOfBorrowers()}")
    library.displayBorrowers()

    # Now lets read from the log file, logger.txt..
    print(f"\nLog FIle...")
    print(f"{library.readLog()}\n")

    # Now let delete the log file, can comment out if you wish to just keep adding to it :-)
    library.removeLog()
    
    # Now lets read from the log file, logger.txt..
    print(f"\nLog FIle...")
    print(f"{library.readLog()}\n")

################################################################################################

"""
Calling the main application function
"""
main()