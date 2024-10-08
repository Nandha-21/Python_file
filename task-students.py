z={}
l=["Name","Age","Class"]
class student:
    def __init__(self):
        for i in range(50):
            x=int(input("1.Enter Student Details,\n2.View Details,\n3.Exit,\n"))

            if x==1:
                self.Add_details()
                                    
            elif x==2:
                #self.View_Detail()     (or)
                self.option()
                
            elif x==3:
                print("Exit....Bye")
                break
               
                
    def Add_details(self):
        a=int(input("enter a Rolls_No:"))
        y={}
        for j in l:
            y[j]=input(j)
            z[a]=y
    
            
    def View_Detail(self):
        g=int(input("enter a Rolls_No:"))

        if g in z:
            c=z[g]
            print("Name:", c["Name"], "\nAge:", c["Age"], "\nClass:", c["Class"])
           
        else:
            print("Wrong... Roll_NO")

    def option(self):
        
        h=int(input("1.Roll_No,\n2.Name,\n3Age,\n4Class"))

        if h==1:
            s=int(input("Enter a Roll_No:"))
            if s in z:
                c=z[s]
                print("Name:", c["Name"], "\nAge:", c["Age"], "\nClass:", c["Class"])

            f=input("Enter a delete option (Y/N)")
            if f=="y":
                del z[s]
                
                
                
        elif h==2:
            s=input("Enter a Name")
            for i,n in z.items():
                if s==n["Name"]:
                    print("Roll_no",i,"\nName:",n["Name"],"\nAge",n["Age"],"\nClass:",n["Class"])

                f=input("Enter a delete option (Y/N)")
                if f=="y":       
                   del z[i]
                   break
        elif h==3:
            s=input("Enter a Age:")
            for i,n in z.items():
                if n["Age"]==s:
                    print("Roll_no",i,"\nName:",n["Name"],"\nAge",n["Age"],"\nClass:",n["Class"])

                f=input("Enter a delete option (Y/N)")
                if f=="y":       
                   del z[i]
                   break
        elif h==4:
            s=input("Enter a Class:")
            for i,n in z.items():
                if n["Class"]==s:
                    print("Roll_no",i,"\nName:",n["Name"],"\nAge",n["Age"],"\nClass:",n["Class"])

                f=input("Enter a delete option (Y/N)")
                if f=="y":       
                   del z[i]
                   break
    
person=student()              
print(z)
        
        
        
        
        
        
    
    
