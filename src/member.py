from person import Person

class Member(Person):
    def __init__(self, name, age, membership_no):
        super().__init__(name, age)
        self.__membership_no = membership_no
        self.__type = "Member"

    """
    class properties
    """
    @property
    def membership_no(self):
        return self.__membership_no
    
    @property
    def type(self):
        return self.__type
    
    """
    class setters
    """
    @membership_no.setter
    def membership_no(self, memberhip_no):
        self.__membership_no = memberhip_no

    """
    A simple set of functions that return the data information
    """
    def bookinfo(self):
        print(f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Membership: {self.membership_no}")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Membership: {self.membership_no}"
    
    def __repr__(self):        
        return f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Membership: {self.membership_no}"