class CUSTOMER:
    """A sample Employee class"""

    def __init__(self, FIRSTNAME, LASTNAME, PHONENUM, ADDRESS, EMAIL):
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.PHONENUM = PHONENUM
        self.ADDRESS = ADDRESS
        self.EMAIL = EMAIL

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {}, {}, {})".format(self.FIRSTNAME, self.LASTNAME, self.PHONENUM, self.ADDRESS, self.EMAIL)