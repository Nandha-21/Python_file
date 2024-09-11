#task
customer=["nandha","kumar","sai","sri","arun"]
amount=[1500,1400,1250,1430,2300]
sender=input("Enter Sender name:")
receiver=input("Enter Receiver name:")
senderamount=int(input("Enter you amount name:"))
for i in customer:
    if(i==sender):
        x=(customer.index(i))
        print("the amount is",amount[x])
        y = amount[x] - senderamount
        print(sender,"current bsalance:",y)
        break
    else:
        print("not available")
        
for j in customer:
    if(j==receiver):
        x=(customer.index(j))
        z = amount[x] + senderamount
        print(receiver,"current balance:",z)
        break
