import mysql.connector
class database:
    def __init__(self):
        dataBase=str(input('Enter your database name:'))
        paSSword=str(input('enter your password:'))
        self.db=mysql.connector.connect(host='localhost',
                           database=dataBase,
                           user='root',
                           password=paSSword)
    def close(self):
        self.db.close()                       
    def add_employee(self):
        id=input("id:")
        name=input("name:")
        crsr=self.db.cursor()
        crsr.execute("INSERT INTO employees(emp_id,name) VALUE(%s,%s)",(id,name))
        self.db.commit()    
    def show(self):
        crsr=self.db.cursor()
        crsr.execute("SELECT * FROM employees")
        for i in crsr:
            print(i)    
data=database()       
           


