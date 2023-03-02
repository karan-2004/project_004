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
   
data=database()       
           


