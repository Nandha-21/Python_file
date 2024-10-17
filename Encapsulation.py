#Encapsulation
'''
private
public
protected
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
