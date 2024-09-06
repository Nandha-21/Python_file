a=int(input("Enter the A value:"))
b=int(input("Enter the B value:"))
c=int(input("Enter the c value:"))
if(a==b==c):
    print("A,B,C are equal")
else:
    if(a>b):
        if(a>c):
            print("A is greater")
        else:
             print("C is greater")
    else:
        if(b>c):
            print("B is greater")
        else:
             print("C is greater")
