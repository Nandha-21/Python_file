#DICTIONARY
d={'reg_no':257,'name':'nandha','dept_name':'CMC'}
'''print(type(d))
print(d)

#accessing value from dictionary
print(d['name'],d['reg_no'])

#function 
#print all value and keys
print(d.items())
print(d.keys())
print(d.values())

#adding or updating dictionary

d['city']='madurai'
print(d)

#update function
f={"yrs":'2yrs','gender':'male'}
d.update(f)
print(d)
            #or
d.update({"blood_group":'O+ve','DOB':'21/12/2003'})
print(d)

d.update({'name':'kumar'})
print(d)

#delete ,clear , pop , popitem

d.pop('name')
print(d)

del d["DOB"]
print(d)

#d.clear()
#print(d)

d.popitem()  #list last value and last update value
print(d)

#function 
print("\n")
print(d)
#keys
for i in d.keys():
    print(i)
#values
for i in d.values():
    print(i)
#items
for i in d.items():
    x,y=i
    print(i)

#copy function
a=d.copy()
print(a)

#get()
x=d.get('dept_name')
print(x)

#setdefault
x=d.setdefault('dept','computer')
print(x)
print('\n')
print(d)

#fromkey()
x=('state','dist')
y=('tamilnadu','madurai')
z=d.fromkeys(x,y)
print(z)'''

#print("\n")
'''
a=input("enter keys")
b=input("enter value")
#first
c={a:b}
d.update(c)
print(d)
#second
d[a]=b
print(d)
'''
#nested Dictionary
#syntax
a={'key':{'key':'value'}}

#for key, value in b.items():
 #   print(f"Key: {key}, Name: {value['name']}, Age: {value['age']}, City: {value['city']}")


#print(a['a1']['name'])
#print(a['a2']['name'])
#print(a['a3']['name'])

#normal Dictionary
#a={'key':'value'}

#accessing values in dictionary
#for i in a.keys():
 #   print(i,"\t",a[i]['age'])
'''b={
    'a1':{'name':'nandha','age':20,'city':'madurai'},
    'a2':{'name':'kumar','age':22,'city':'madurai'},
    'a3':{'name':'vj','age':25,'city':'madurai'},
    }
for j in b.keys():
    print(j,"\t",b[j]['name'],"\t",b[j]['age'],"\t",b[j]['city'])
    
#task in nested loop:
for i in b.items():
    x,y=i
    print("\n")
    print(x)
    print("\n")
    for j in y:
        print(j,"-",y[j])'''

#task
'''
z={}
for i in range(0,5):
    a=input("enter a keys1:")
    if a=="quit":
        break
    b=input("enter a keys:")
    c=input("enter a values:")
    #z[a]=c
    z.update({a:{b:c}})
print(z)
'''
#task1
'''
q={}
for i in range(10):
    a=input("enter a keys1:")
    if a=="0":
        break
    b=input("enter a product:")
    c=input("enter a id-:")
    d=input("enter a price:")
    e=input("enter a date")
   # q.update({a:{b,c,d,e}})
#or
    q[a]={'product':b,"id-":c,"price":d,"date":e}
print(q)
'''
#task2
'''
a={}
l=['name','age','city']
z=int(input("Enter a number pair:"))
for i in range(z):
    x=input("Enter a Key")
    y=[]
    for j in i:
        y[j]=input(j)
    a[x]=y
print(a)
'''
    
