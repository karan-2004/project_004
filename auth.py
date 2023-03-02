import database as db
from employee import emp as em
class password:
    def auth(self,x):
        emp=None
        a=[str(x)]
        crsr=db.data.db.cursor()
        crsr.execute("SELECT emp_id FROM employees WHERE passcode=%s",tuple(a))
        for i in crsr:
           emp=i  
        if(emp==None):
            print('invalid password')
            return 0

        if(em.stat[emp[0]-1]==0):
            crsr.execute("UPDATE REGISTER SET ENTRY_TIME=NOW() WHERE EMP_ID=%s AND DATE_OF_REGISTER=CURRENT_DATE",emp)
            db.data.db.commit()
            print("HAPPY TO HAVE YOU BACK!!")
            em.stat[emp[0]-1]=1
        else:
            crsr.execute("UPDATE REGISTER SET EXIT_TIME=NOW() WHERE EMP_ID=%s AND DATE_OF_REGISTER=CURRENT_DATE",emp)
            db.data.db.commit()    
            em.stat[emp[0]-1]=0
            print("WE WILL MISS YOU ALL THE NIGHT")
           

    