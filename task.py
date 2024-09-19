a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=input("Enter operator value=")
if(c=="+"):
    print("ans:",a+b)
elif(c=="-"):
    print("ans:",a-b)
elif(c=="*"):
    print("ans:",a*b)
elif(c=="/"):
    print("ans:",a/b)
elif(c=="%"):
    print("ans:",a/b)
else:
    print("Nothing")

z=input("Enter the word:")
x=0
for i in z:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        x=x+1
print("number of vowels:",x)
        
