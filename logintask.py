import datetime as d
name=input("Enter a UserName:")
password=int(input("Enter a Password:"))
class login:
    def __init__(self):
        if name=="nandha" and password==12345:
            print("Login Success")
            self.time=d.datetime.now()
            self.view()     
            
        else:
            print("Fail")
    def view(self):
        v=input("View the Detail(Y/N)")
        if v=="y":
            print("Lasr Login",self.time.hour,":",self.time.minute,":",self.time.second)
                    #OR
            print(self.time.strftime("%X"))
a=login()
            
        
    
