for i in range(64,71):
    j=65
    while(j<i):
        print(chr(j),end=' ')
        j+=1
    print("\n")

#helloworld
a = "HELLOWORLD"
for i in range(len(a)):
    for j in range(i + 1):
        print(a[j], end=' ')
    print("\n")
    
#
s=" "
for i in a:
    s+=i
    print(s, end=' ')
    
