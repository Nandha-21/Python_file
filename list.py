#           LIST
a=[10,20,30,40]
print(a)
print(a[2])
print(a[-3])

#for loop
for i in a:
    print(i)

#using list() function to creat list
z=list(x*2 for x in range(1,11))
print(z)

#task
customer=["nandha","kumar","sai","sri","arun"]
amount=[500,400,250,430,300]
a=input("Enter Sender name")
#b=int(input("Enter Receiver name"))
#amount=int(input("Enter you amount name"))
for i in customer:
    if(a==i):
        print("available")
        break
    else:
        print("not available")
     

 #JUMP STATEMENT   
for i in range(1,10,1):
    if(i==5):
        pass
       # continue
        #break
    print(i)
    
