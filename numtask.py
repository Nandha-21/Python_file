a=[10,1,2,3,4,5,6,9,10,12]
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

'''for num in a:
    while(num > b):
        num+=1
        print(b)
    break'''
        
