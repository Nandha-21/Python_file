#set
#set symbol==>{} and remove duplicate value
a={20,30,40,50,33,45,22,30,40}
b={45,22,60,33,70,80}
print(type(a),a)
#types
#UNION
print(a.union(b))
#INTERSECTION(COMMON VALUE)
print(a.intersection(b))
#DIFFERENCE
print(a.difference(b))
