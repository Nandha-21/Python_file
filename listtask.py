#task
'''customer=["nandha","kumar","sai","sri","arun"]
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
    else:
        print("not available")'''


'''cust=["nandha","kumar","sai","sri","arun"]
amt=[1500,1700,1250,2010,2300]
send=input("enter the sender name")
a=0
rec=input("enter the receiver name")
b=0
senderamt=int(input("enter the send amt"))
for i in cust:
    if i!=send and i!=rec:
        print("not avi")
        pass
    else:
        for i in cust:
            if i==send:
                x=amt[a]
                print(i,"avilable bal",x)
                z = x - senderamt
                print(i,"current bal is",z)
            a+=1
            break
        for i in cust:
            if i==rec:
                f=amt[b]
                print(i,"avilable bal",f)
                h = f + senderamt
                print(i,"current bal is",h)
            b+=1
            break'''

cust = ["nandha", "kumar", "sai", "sri", "arun"]
amt = [1500, 1700, 1250, 2010, 2300]

send = input("Enter the sender's name: ")
rec = input("Enter the receiver's name: ")
senderamt = int(input("Enter the amount to send: "))

a = 0
b = 0

# Process the sender
for i in cust:
    if i == send:
        x = amt[a]
        print(f"{i} available balance: {x}")
        if x >= senderamt:
            z = x - senderamt
            print(f"{i} current balance after sending: {z}")
            amt[a] = z  # Update sender's balance
        else:
            print(f"{i} does not have enough balance.")
        break
    a += 1
else:
    print("Sender not available")

# Process the recipient
for i in cust:
    if i == rec:
        f = amt[b]
        print(f"{i} available balance: {f}")
        h = f + senderamt
        print(f"{i} current balance after receiving: {h}")
        amt[b] = h  # Update recipient's balance
        break
    b += 1
else:
    print("Recipient not available")

print("Updated balances:", amt)

    
        
 

