#Operator OverLoading

class over():
    def __init__(self):
        self.a=int(input("Enter number"))
    def __add__(self,v):
        return(self.a+v.a)
n=over()
m=over()
print(n+m)

#error and handing exception
a=int(input("enter a number"))
b=int(input("enter a number"))
try:
    print(a/b)
except Exception as e:
    print("Error",e)
finally:
    print("finished")
