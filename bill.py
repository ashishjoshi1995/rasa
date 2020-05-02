class BILL:
    """A sample Employee class"""

    def __init__(self, FIRSTNAME, LASTNAME, PHONENUM, BILLID, METERREADING, BILLAMOUNT, BILL_STATUS, PAYMENT_LAST_DATE):
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.PHONENUM = PHONENUM
        self.METERREADING = METERREADING
        self.BILLID = BILLID
        self.BILLAMOUNT = BILLAMOUNT
        self.BILL_STATUS = BILL_STATUS
        self.PAYMENT_LAST_DATE = PAYMENT_LAST_DATE

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.FIRSTNAME, self.LASTNAME, self.PHONENUM, self.BILLID, self.METERREADING, self.BILLAMOUNT, self.BILL_STATUS, self.PAYMENT_LAST_DATE)