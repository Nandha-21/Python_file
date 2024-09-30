#FUNCTION       python function
#SYNTAX
'''
deffunction_name(parameter/argument):
        function block start


        function block end
print()
'''
#EXAMPLE for function
'''
def print1():
    a='hello world'
    print(a)
print1()
print("end of program")
print1()
print1()
print("end of program")
'''
'''
a=int(input("Enter the value 1:"))
b=int(input("Enter the value 2:"))
c=input("\n1.add\n2.sub\n3.multi\n4.div\n5.m_div\n choose the symbol~")
def cal():
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def multi():
        print(a*b)
    def div():
        print(a/b)
    def m_div():
        print(a%b)
    if c=="1":
        add()
    elif c=="2":
        sub()
    elif c=="3":
        multi()
    elif c=="4":
        div()
    elif c=="5":
        m_div()
    else:
        print("invaild selection")
cal()
'''
'''
def input_fun():
    a=int(input("Enter the value 1:"))
    b=int(input("Enter the value 2:"))
    c=input("\n1.add\n2.sub\n3.multi\n4.div\n5.m_div\n choose the symbol~")
    cal(a,b,c)
def cal(a,b,c):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def multi():
        print(a*b)
    def div():
        print(a/b)
    def m_div():
        print(a%b)
    if c=="1":
        add()
    elif(c=="2"):
        sub()
    elif(c=="3"):
        multi()
    elif(c=="4"):
        div()
    elif(c=="5"):
        m_div()
    else:
        print("invaild selection")
input_fun()
'''

#sample
    #local
    #enclosed
    #gobal
'''
z=10    #gobal
def local():
    z=100     #local scope
    print(z)
def enclosed_fun():
    z=200    #enclosed scope
    def closed_fun():
        z=1  #local scope
        print(z)
    closed_fun()
    print(z)
print(z)
enclosed_fun()
'''
a=10
def demo():
    global a
    print(a)
    a=1

demo()




