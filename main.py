from auth import password 
import employee as em
#em.emp.show()
def main(): 
    while True:
        pas=int(input('Enter your password:'))
        if(pas>9998):
            break
        password.auth(password,pas)
main()    
    