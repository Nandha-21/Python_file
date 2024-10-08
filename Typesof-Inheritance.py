#type of Inheritance
'''
single
multiple
multiple-level
Hierarchical
Hybrid
'''
#single Inheritance
#ex
'''
class parent:
    def print1(self):
        print("Print a parents class")

class child(parent):
    pass
a1=child()
a1.print1()
print("\n")
'''
#another one
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

#multiple Inheritance
#ex
'''
class parent1:
    def c1(self):
        print("This is First Parent")

class parent2:
    def c2(self):
        print("This is second Parent")

class child(parent1,parent2):
    pass

a1=child()
a1.c1()
a1.c2()
print("\n")
'''
'''
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
'''        
#multiple-Level Inheritance
#ex
'''
class parent1:
    def c1(self):
        print("This is First Parent")

class parent2(parent1):
    def c2(self):
        print("This is second Parent")

class child(parent2):
    pass

a1=child()
a1.c1()
a1.c2()
'''
#Hierarchical
#ex
'''
class parent():
    def c1(self):
        print("parent")
class child1(parent):
    def c2(self):
        print("first child")
class child2(parent):
    def c3(self):
        print("second child")

x=child1()
x.c1()
x.c2()
y=child2()
y.c1()
y.c3()
'''
#Hybrid
#ex
class parent():
    def c1(self):
        print("parent")
class child1(parent):
    def c2(self):
        print("first child")
class child2(parent):
    def c3(self):
        print("second child")
class child3(child1,child2):
    def c4(self):
        print("third child")
a1=child3()
a1.c1()
a1.c2()
a1.c3()
a1.c4()
