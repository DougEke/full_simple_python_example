from dataclasses import dataclass
from datetime import date
from person import Person
from person_type import Person_Type


@dataclass
class Guest(Person):
    loan_date: date

    type: Person_Type

    def __init__(self, name, age, date):
        super().__init__(name, age)
        self.loan_date = date
        self.type = Person_Type.GUEST

    # def __str__(self):
    #     return (
    #         f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Date: {self.date}"
    #     )

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Type: {self.type.name}, Date: {self.loan_date}"
