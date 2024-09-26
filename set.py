#set
#set symbol==>{} and remove duplicate value
#a={20,30,40,50,33,45,22,30,40}
#b={45,22,60,33,70,80}
#print(type(a),a)
#types
'''a={1,2,3,4,5,6,7,8,9}
b={6,7,8,9,10,11,12}
#UNION
print(a.union(b))

#INTERSECTION(COMMON VALUE) (&)
print(a.intersection(b))

#DIFFERENCE (common value delete and print a)    (-)
print(a.difference(b))

#SYMMETRIC_DIFFERENCE
print(a.symmetric_difference(b))

z={}
print(type(z))

u=set()
print(type(u))

u.add(20)
print(u)

z=set()
y=[10,20,30,40,50,60]

z.update(y)
print(z)'''

g={10,20,30,40,50,60}
g.pop()
print(g)

g.remove(20)
print(g)

g.discard(30)
print(g)

#g.clear()
#print(g)

del g
print(g)
