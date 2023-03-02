import database as db
class employee:
    def __init__(self) -> None:
        self.key=1324
    def add_employee(self):
        id=input("id:")
        name=input("name:")
        password=input("Enter the passcode:")
        crsr=db.data.db.cursor()
        crsr.execute("INSERT INTO employees VALUE(%s,%s,%s)",(id,name,password))
        db.data.db.commit() 
    def rm_employee(self):
        id=input('id:')
        crsr=db.data.db.cursor()
        crsr.execute("DELETE FROM employees WHERE emp_id=%s",tuple(id)) 
        db.data.db.commit()      
    def show(self):
        crsr=db.data.db.cursor()
        crsr.execute("SELECT * FROM employees")
        for i in crsr:
            print(i) 
emp=employee()            