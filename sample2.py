#a=int(input("Enter the value:"))
#if(a==1):
#      print("hello")
#else:
#    print("hai")

#a=int(input("enter the a value:"))
#b=int(input("enter the b value:"))
#if(a>b):
#    print("a is greater")
#else:
#    print("b is greater")

#a=int(input("Enter value(1,2,3):"))
#if(a==1):
#    print("hai")
#elif(a==2):
#    print("hello")
#elif(a==3):
 #   print("welcome")
#else:
 #   print("sorry")

a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("enter the c value:"))
if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
elif(c>a and c>b):
    print("c is greater")
elif(a==b==c):
    print("a and b and c are equal")
elif(a==b>c):
    print("a and b are equal and c is greater")
else:
    print("zero")
