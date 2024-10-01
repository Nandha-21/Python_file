#class and objects
#class = template
'''
class emp_name:
    name=""
    id=""
    age=""
    city=""

a=emp_name()
b=emp_name()


a.name="nandha"
a.id=21257
a.age=21
a.city="mdu"

print(a.name)
print(a.id)
print(a.age)
print(a.city)

print("\n")

b.name="kumar"
b.id=21220
b.age=25
b.city="chennai"
print(b.name)
print(b.id)
print(b.age)
print(b.city)
'''
#using function name
'''class student_name:
    name=""
    id=""
    age=""
    city=""
    def get(self):
        self.name=input("Enter a name:")
        self.id=int(input("Enter a id:"))
        self.age=int(input("Enter a age:"))
        self.city=input("Enter a city:")
        
    def put(self):
        print("name :",self.name)
        print("id :",self.id)
        print("age :",self.age)
        print("city :",self.city)
nandha=student_name()
sk=student_name()

nandha.get()
nandha.put()
sk.get()
sk.put()
'''
'''
#task
print("Welcome To All")
print("~~Enter Your Option~~")
n=1
class Name:
    Name=""
    Age=0
    Roll_No=0
  
    def input_1(self):
        self.Name=input("Enter Name:")
        self.Age=int(input("Enter Age:"))
        self.Roll_No=int(input("Enter Roll_No:"))
        
    def print_1(self):
        print(self.Name)
        print(self.Age)
        print(self.Roll_No)

    def running(self):
        #for i in range(10):
        while n:
            x=int(input("1.Add Student Detail,\n2.View Student Details,\n*The Given Values must be in Number"))

            if x == 1:
                name.input_1()
            elif x==2:
                name.print_1()
            else:
                print("wrong...")

            choose=input("Do You Want to Continue (Y/N): ")
            if choose!="y":
                print("Exiting ...... bye")
                break
                
name=Name()
name.running()
'''
# 2 method
print("Welcome To All")
print("~~Enter Your Option~~")
class Name:
    Name=""
    Age=0
    Roll_No=0
  
    def input_1(self):
        self.Name=input("Enter Name:")
        self.Age=int(input("Enter Age:"))
        self.Roll_No=int(input("Enter Roll_No:"))
        
    def print_1(self):
        print(self.Name)
        print(self.Age)
        print(self.Roll_No)

    def program(self):
        x=int(input("1.Add Student Detail,\n2.View Student Details,\n*The Given Values must be in Number"))
        if x == 1:
            name.input_1()
        elif x==2:
            name.print_1()
        else:
            print("wrong...")

    def running(self):
        choose=input("Do You Want to Continue (Y/N): ")
        if choose=="y":
            name.program()
            name.running()
        else:
            print("Exiting ...... bye")
                
name=Name()
name.program()
name.running()










        




        
