from person import Person

class Guest(Person):
    def __init__(self, name, age, date):
        super().__init__(name, age)
        self.__date = date
        self.__type = "Guest"

    """
    class properties
    """
    @property
    def date(self):
        return self.__date
    
    @property
    def type(self):
        return self.__type
    
    """
    class setters
    """
    @date.setter
    def date(self, date):
        self.__date = date

    """
    A simple set of functions that return the data information
    """
    def bookinfo(self):
        print(f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Date: {self.date}")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Date: {self.date}"
    
    def __repr__(self):        
        return f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Date: {self.date}"