#
'''
z=input("Enter a word:")
vowels=("aeiouAEIOU")
x = 0
for i in z:
    if i in vowels:
        x += 1
print("Number of vowels:",x)
'''
#
'''
z=input("Enter the word:")
x=0
for i in z:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        x=x+1
print("number of vowels:",x)
 '''      

#using filter
def find(x):
    a=['a','e','i','o','u','A','E','I','O']
    if x in a:
        return True
    else:
        return False
x=input("Enter Word")
y=filter(find,x)
print(len(list(y)))

