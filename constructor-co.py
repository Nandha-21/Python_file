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

