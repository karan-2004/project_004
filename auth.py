import database as db
class password:
    def auth(self):
        password=input("Enter your password:")
        crsr=db.data.db.cursor(prepared=True)
        crsr.executemany("SELECT EMP_ID FROM EMPLOYEES WHERE PASSCODE= %s",[tuple(password)])
        crsr.executemany("UPDATE REGISTER SET ENTRY_TIME=NOW() WHERE EMP_ID=%s AND DATE_OF_REGISTER=CURRENT_DATE AND CR_STATUS='O'",[i for i in crsr])
        db.data.db.commit()
authen=password()           

    