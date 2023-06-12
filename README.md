This is a simple OO example using various aspects of Python. The idea is that we have a library that keeps a collection of borrows within a dictionary.

The app has a number of classes:
librarySystem.py    : A simple class that tests the functionality, not a formal unti test class
library.py          : The main library that keeps track of the borrowers within a dictionary
logger.py           : Logger class that logs when a borrower has been created, writes the detials to a file
borrower.py         : Borrower class that keeps track of the book and person who's borrowed the book
book.py             : Book class that stores the details of a book
person.py           : Super class of the member and guest
member.py           : Class that inherits from the person class
guest.py            : Class that inherits from the person class

This is only a basic app and could certainly be written/designed better, however the primary aim is to demonstrate various aspects of python and the area of OO (Object Oriented) development.

There is a kind of test class, not formal unit testing as I'll implement that at a later date to demonstrate unit testing with Python, called librarySystem. This will simply run through the various bits of functionality with the output into the terminal/powershell window, or which ever prompt you're using.

To run the app simply navigate to the location as to where you have saved the files to and run:
python librarySystem.py

This will produce an output something like the following
===============================================================================================
===> New borrower added to the system: Doug...

===> Dictionary size: 1

***Borrower***
Date: 2023-06-09 17:17:02
Name: Name: Doug, Age: 41, Type: Member, Membership: mem001
Book: Author: J.K. Rowling, Title: Harry Potter, ISBN: c9b34cd9-94e7-4644-b2c1-3af48d5512b7

===> New borrower added to the system: John Smith...

===> Dictionary size: 2

***Borrower***
Date: 2023-06-09 17:17:02
Name: Name: Doug, Age: 41, Type: Member, Membership: mem001
Book: Author: J.K. Rowling, Title: Harry Potter, ISBN: c9b34cd9-94e7-4644-b2c1-3af48d5512b7

***Borrower***
Date: 2023-06-09 17:17:02
Name: Name: John Smith, Age: 50, Type: Guest, Date: 2023-06-09
Book: Author: Stephen King, Title: The Shining, ISBN: adb783d5-28e9-4255-b4e2-bf1253032fd4

Log FIle...
[2023-06-09 17:17:02] - New borrower added: Doug, Book: Harry Potter
[2023-06-09 17:17:02] - New borrower added: John Smith, Book: The Shining

Log FIle...
logger.txt does not exists..
None
===============================================================================================

You can get hold of the files via the 'Code' option within github at https://github.com/DougEke/full_simple_python_example

or create a file that you wish to save the files to and enter the following within a command prompt of your choice:

git clone https://github.com/DougEke/full_simple_python_example.git