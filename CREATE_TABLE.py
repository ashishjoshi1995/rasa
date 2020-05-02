import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS CUSTOMERS(FIRSTNAME TEXT, LASTNAME TEXT, PHONENUM TEXT, ADDRESS TEXT, EMAIL TEXT)')
	c.execute('CREATE TABLE IF NOT EXISTS BILLS(FIRSTNAME TEXT, LASTNAME TEXT, PHONENUM TEXT, BILLID TEXT, METERREADING TEXT, BILLAMOUNT TEXT, BILL_STATUS INT, PAYMENT_LAST_DATE DATE)')
	c.execute('CREATE TABLE IF NOT EXISTS SERVICE_REQUESTS(FIRSTNAME TEXT, LASTNAME TEXT, PHONENUM TEXT, ADDRESS TEXT, REQUEST_TYPE TEXT, STATUS TEXT)')

def data_entry():
	c.execute("INSERT INTO CUSTOMERS VALUES('Ashish', 'Joshi', '9756475739', 'Indore', 'ashish.f.joshi@accenture.com')")
	c.execute("INSERT INTO CUSTOMERS VALUES('Sarthak', 'Bhargava', '9899808458', 'Pune', 'sarthak.bhargava@accenture.com')")
	c.execute("INSERT INTO CUSTOMERS VALUES('Sweta', 'Bhoi', '9620000852', 'Gurugram', 'sweta.bhoi@accenture.com')")
	c.execute("INSERT INTO CUSTOMERS VALUES('Yogesh', 'Dhond', '9820358586', 'Mumbai', 'yogesh.dhond@accenture.com')")

def query():
	c.execute("SELECT * FROM CUSTOMERS WHERE PHONENUM='9899808458'")
	print(c.fetchall())

def create_Bill():
	c.execute("INSERT INTO BILLS VALUES('Ashish', 'Joshi', '9756475739', 'Bill_123', '4598','$500', 'Pending', '12/05/2020')")
	c.execute("INSERT INTO BILLS VALUES('Sarthak', 'Bhargava', '9899808458', 'Bill_124', '7896', '$500', 'Pending', '12/05/2020')")
	c.execute("INSERT INTO BILLS VALUES('Sweta', 'Bhoi', '9620000852', 'Bill_125', '5679', '$500', 'Pending', '12/05/2020')")

create_table()
data_entry()
query()
create_Bill()
conn.commit()
c.close()
conn.close()