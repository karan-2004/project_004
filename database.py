import mysql.connector
class database:
    def __init__(self):
        dataBase=str(input('Enter your DATABASE name:'))
        paSSword=str(input('Enter your DATABASE password:'))
        self.db=mysql.connector.connect(host='localhost',
                           database=dataBase,
                           user='root',
                           password=paSSword)
    def close(self):
        self.db.close()                       
   
data=database()       
           


