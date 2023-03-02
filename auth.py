import database as db
import main
class password:
    def __init__(self) -> None:
        self.stat=[0,0]
    def auth(self):
        pas=input("Enter your password:")
        crsr=db.data.db.cursor()
        #crsr.execute("SELECT emp_id FROM employees WHERE passcode=%s",tuple(pas))
        #for i in crsr:
        #   print(i)
        #    emp=i
        if(self.stat[emp-1]==0):
            crsr.execute("UPDATE REGISTER SET ENTRY_TIME=NOW() WHERE EMP_ID=2 AND DATE_OF_REGISTER=CURRENT_DATE AND CR_STATUS='O'")
            #
            db.data.db.commit()
            self.stat[emp-1]=1
            main.main()
        else:
            crsr.execute("UPDATE REGISTER SET EXIT_TIME=NOW() WHERE EMP_ID=2 AND DATE_OF_REGISTER=CURRENT_DATE AND CR_STATUS='I'")
            #
            db.data.db.commit()    
            self.stat[emp-1]=0
            main.main()
authen=password()           

    