#ADD MORE ELEMENT IN LIST
    #APPEND
    #EXTEND
    #INSERT
list=[]
print(list)
#add value in end/last element of list and only one value/single value
list.append(10)
print(list)
#same concent but more value in add list
list.extend([20,30,40,50])
print(list)
list.insert(3,35)
print(list)

#DELETING ELEMENT FOR LIST
del list[3]
print(list)
del list

s=[20,30,40,50]
#remove element list
s.remove(20)
print(s)

#min and max value  in list
l1=[5,10,20,30,40,50]
z=0
x=min(l1)
print(x)
x=max(l1)
print(x)
l1.pop(2)
print(l1)
l1.clear()

x=int(input("enter a searching value:"))
for i in l1:
    if i==x:
        z=1
if z==1:
    print("value is available")
else:
    print("value is not available")

#task delete the value        
a = int(input("Enter a number to remove: "))
k = [10, 20, 30, 40, 50, 60]
if a in k:
    index = k.index(a)
    del k[index]
    print(k)
else:
    print("Number not found")
    
#task remove the value
a = int(input("Enter a number to remove: "))
k = [10, 20, 30, 40, 50, 60]
z=0
for i in k:
    if i==a:
        z=1
if z==1:
    index = k.index(a)
    k.remove(a)
    print(k)
else:
    print("Number not found")


list1=[20,30,450,33]
del list1[3]
print(list1)
list1.clear()
print(list1)

m=[10,30,20,20,30,44,45,45,50,44,47,60]
n=[]
for i in m:
    if i not in n:
        n.append(i)
m.clear()
m=n.copy()
print(n)
print(m)

#m=input("enter a number")



