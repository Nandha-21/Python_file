#tuple in amount 
customer=["nandha","dj","ak","vj","sk"]
amount=(3500,2400,4250,1430,4300)
sender=input("Enter Sender name:")
receiver=input("Enter Receiver name:")
senderamount=int(input("Enter you amount name:"))
for i in customer:
    if(i==sender):
        x=(customer.index(i))
        print(i,"the amount is",amount[x])
        y = amount[x] - senderamount
        print(sender,"current balance:",y)
        a=list(amount)
        a[x]=amount[x]-senderamount
        a=tuple(a)
        amount=a
        
for j in customer:
    if(j==receiver):
        x=(customer.index(j))
        z = amount[x] + senderamount
        print(receiver,"current balance:",z)
        a=list(amount)
        a[x]=amount[x]+senderamount
        a=tuple(a)
        amount=a
        
print(amount)
print(type(amount))
