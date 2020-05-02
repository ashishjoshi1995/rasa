class SERVICE_REQUEST:
    """A sample Employee class"""

    def __init__(self, FIRSTNAME, LASTNAME, PHONENUM, BILLID, BILLAMOUNT, BILL_STATUS):
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.PHONENUM = PHONENUM
        self.BILLID = BILLID
        self.BILLAMOUNT = BILLAMOUNT
        self.BILL_STATUS = BILL_STATUS
        
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}', '{}')".format(self.FIRSTNAME, self.LASTNAME, self.PHONENUM, self.ADDRESS, self.REQUEST_TYPE, self.STATUS)