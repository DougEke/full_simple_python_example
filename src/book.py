from dataclasses import dataclass

"""
The @dataclass is not needed here as this, ineffect, replaces the properties and setters sections
"""


@dataclass(slots=True)
class Book:
    author: str
    title: str
    isbn: str

    def __init__(self, author, title, isbn):
        self.author = author
        self.title = title
        self.isbn = isbn

    # def bookinfo(self):
    #     print(f"Author: {self.author}, Title: {self.title}, ISBN: {self.isbn}")

    # def __str__(self):
    #     return f"Author: {self.author}, Title: {self.title}, ISBN: {self.isbn}"

    def __repr__(self):
        return f"Author: {self.author}, Title: {self.title}, ISBN: {self.isbn}"
