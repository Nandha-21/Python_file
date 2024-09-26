#TYPE OF FUNCTION
'''
1.User defined function
2.Recursive function
3.Lambda fumction
4.built-in function (already built the function)
        (for ex: type(),index(),input(),count()...)
'''
#User Defined & recursive function
def add():
    print("hello")
    x=int(input("enter x value"))
    if x==1:
        add()
    else:
        print("sry")
add()


#lambda function
#keyvalue = lambda

x=lambda a:a**5
print(x(2))

y=lambda a,b,c:a+b+c
print(y(10,25,5))

#returning value from function

def nor():
    x=int(input("Enter x value"))
    y=int(input("Enter y value"))
    return(x,y)
a,b=nor()
print(a-b)


