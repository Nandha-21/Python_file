a=[1,2,3,4,5]#list ==>[]
b=(1,2,3,4,5)#tuple ==>()

#list change the value
a[2]=4
print(a)

#tuple don't change the value 
    #b[2]=2
    #print(b)

#creating tuple using function:
    #tuple()
g=tuple(x*2 for x in range(1,10,1))
print(g)

#changing element in tuple
m=(11,12,13,13,15)
#convent into tuple to list
z=list(m)
print(z)
#change the value
z[3]=25
z=tuple(z)
print(z,type(z))

#accessing single element in tuple

print(z[3])

q=(1,2,3,4,5,2)
r=(6,7,8,9,10)
t=q+r
print(t)

#unpacking tuple
a=(20,30,40)
(b,c,d)=(20,30,40)
print(a,'\n',b,'\n',c,'\n',d)

#count()
print(q.count(2))

#index()
print(q[2])

#min()
print(min(q))

#max()
print(max(q))






