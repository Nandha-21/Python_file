#min and max 
a=[7,10,12,23,12,8,10,35]
b=a[0]
#print(min(a))
#print(max(a))

for i in a:
    if i < b:#min
        b = i
print(b)

for i in a:
    if i > b:#max
        b = i
print(b)

'''for i in a:
    for j in a:
        while i<j:
            j+=1
            print(j)'''



#duplicate value
z=[20,20,30,35,45,40,30,22,40,50,55]

for i in z:
    for j in z:
        if i==j and z.count(j) > 1:
            z.remove(j)           
print(z)
