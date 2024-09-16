a='hello world '
b='this my python program '
#CONCADINATION(+)
c=a+b
print(c)

#APPEND(+)
d=a+'python coding '
print(d)

#REPEAT(*)
print(a*3)

#BUILD IN FUNCTION FOR STRING

#len
print(len(a))

#UPPER
print(a.upper())

#lower
print(a.lower())

#capitalize
print(a.capitalize())

#ord
z='Q'
print(ord(z))

#id()
print(id(z))

#string slicing(cut)
#SYNTAX: Variable_name[start:end]
s='g.nandhakumar'
h=s[2:8]
print(h)

h=s[:]
#take full string
print(h)

h=s[:8]
print(h)

h=s[8:]
print(h)

#string sride slicing(cut)
#SYNTAX: Variable_name[start:end:step]
h=s[::2]
print(h)

'''#we can use slicing method in list
a='hello wrold'
a[2]='a'
print(a)'''

#COUNT(STRING:START:END)
a='hello wrold'
print(a.count("l"))

#chr()
a=65
print(chr(a))
