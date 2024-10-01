#constructor & destructor
#special function
#constructor
'''
class person:
    def __init__(self,name,age):          #syntax  __init__
        print("Constructor is Executed")
        self.name=name
        self.age=age
        print("name:",name)
        print("age:",age)
    def __del__(self):           #syntax   __del__
        print("Destructor is Executed")

class person1:
    def hello(self):
        print("Constructor is executed")
        
a1=person("nk",20)
a2=person1()
a2.hello()
del a1


#data member
# two type are
        #Public
        #private
class member:
    a="nandha"#public
    __a1="kumar"#private
    def demo(self):
        print(self.__a1)
x=member()
x.demo()
print(x.a)
'''
#single inheritance
'''class person1:#parent
    a=''
    b=0
    def detail(self):
        self.a=input("Enter a name:")
        self.b=input("Enter a id:")
        
class person2(person1):#child
    def print(self):
        print(self.a)
        print(self.b)
    
x=person2()
x.detail()
x.print()
'''
#Multiple inheritance
class student:#parent
    a=''
    b=0
    def detail(self):
        self.a=input("Enter a name:")
        self.b=input("Enter a id:")
class subject():
    sub_name=""
    sub_mark=0
    def subDetail(self):
        self.sub_name=input("Enter a subject name")
        self.sub_mark=int(input("Enter a mark"))
        
class person(student,subject):#child
    def print(self):
        print(self.a)
        print(self.b)
        print(self.sub_name)
        print(self.sub_mark)

x=person()
x.detail()
x.subDetail()
x.print()
        
