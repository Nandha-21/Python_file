#Encapsulation
'''
private
public
protected
'''
'''
class grandparent:
    def __init__(self):
        self._a=45      #protected
        self.__b=60

class parent(grandparent):
    def add1(self):
        print(self._a)

class child(parent):
    def __init__(self):
        print("child constructor")
    def add1(self):
        print(self._a)

z=parent()
z.add1()

print("\n")

'''
#MAP   (for loop overcome )
'''
def demo(a):
    return a*2
x=map(demo,[1,2,3,4,5,6,7,8,9,10])
print(set(x))
'''
#some demo
'''
x=[1,2,3,4,5,6,7,8,9,10]
def some(a):
    return a*2
for i in range(0,len(x)):
    x[i]=some(i)

print(x)
'''

#reduce
'''
import functools
def demo(a,b):
    print(a,b)
    return a*2
x=functools.reduce(demo,[1,2,3,4,5,6,7])
print(x)
'''

