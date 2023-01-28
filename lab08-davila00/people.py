class Person(object):
    """functions for Person class"""

    def __init__(self, fn, ln):
        self.firstname = fn
        self.lastname = ln

class Faculty(Person):
    """functions for Faculty class."""

    def __init__(self, fn, ln, dept):
        Person.__init__(self, fn, ln)
        self.department = dept

class Student(Person):
    """functions for Student class"""

    def __init__(self, fn, ln):
        Person.__init__(self, fn, ln)

    def set_class(self, cyear):
        self.classyear = cyear

    def set_major(self, maj):
        self.major = maj

    def set_advisor(self, Faculty):
        self.advisor = Faculty
