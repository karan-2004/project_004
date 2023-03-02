import database as db
class password:
    def auth(self,x):
        self.stat=[1,1]
        a=[str(x)]
        crsr=db.data.db.cursor()
        crsr.execute("SELECT emp_id FROM employees WHERE passcode=%s",tuple(a))
        for i in crsr:
           emp=i  
        if(self.stat[emp[0]-1]==0):
            crsr.execute("UPDATE REGISTER SET ENTRY_TIME=NOW() WHERE EMP_ID=%s AND DATE_OF_REGISTER=CURRENT_DATE AND CR_STATUS='O'",emp)
            #
            db.data.db.commit()
            self.stat[emp[0]-1]=1
            main.main()
        else:
            crsr.execute("UPDATE REGISTER SET EXIT_TIME=NOW() WHERE EMP_ID=%s AND DATE_OF_REGISTER=CURRENT_DATE AND CR_STATUS='O'",emp)
            #
            db.data.db.commit()    
            self.stat[emp[0]-1]=0
           

    