#task
'''
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

'''
#task-2
'''
z={}

class students:
     def __init__(self):
         count=0
         for i in range(50):
             x=int(input("1.Enter Student Details,\n2.View Details,\n3.Exit,\n"))

             if x==1:
                 self.details()
                 count=1
                                    
             elif x==2:
                 if count==1:
                     self.option()
                 else:
                     print("enter atleast one value \n")
                
                
             elif x==3:
                 print("Exit....Bye")
                 break
             else:
                 print("enter a value")                

     def details(self):
         Roll_no=int(input("Enter a Roll_no:"))
         Name=input("Enter a Name:")
         Age=int(input("Enter a Age:"))
         Class=int(input("Enter a Class:"))
         z.update({Roll_no:{"Name":Name,"Age":Age,"Class":Class}})
         
     def option(self):
         h=int(input("1.Roll_No,\n2.Name,\n3Age,\n4Class"))

         if h==1:
             i=int(input("Enter a Roll_No:"))
             
             if self.i in z:
                  c=z[self.i]
                  print("Name:", c["Name"], "\nAge:", c["Age"], "\nClass:", c["Class"])
                  self.del_1()
                  
         elif h==2:
             s=input("Enter a Name")
             
             for self.i,n in z.items():
                 if s==n["Name"]:
                      print("Roll_no",self.i,"\nName:",n["Name"],"\nAge",n["Age"],"\nClass:",n["Class"])
                      self.del_1()  
                      break

         elif h==3:
              s=int(input("Enter a Age:"))

              for self.i,n in z.items():
                   if s==n["Age"]:
                        print("Roll_no",self.i,"\nName:",n["Name"],"\nAge",n["Age"],"\nClass:",n["Class"])
                        self.del_1()  
                        break
             
             
         elif h==4:
             s=int(input("Enter a Class:"))
             
             for self.i,n in z.items():
                 if s==n["Class"]:
                      print("Roll_no",self.i,"\nName:",n["Name"],"\nAge",n["Age"],"\nClass:",n["Class"])
                      self.del_1()  
                      break

class students_1(students):
     def del_1(self):
          f=input("Enter a delete option (Y/N)")
          if f=="y":
               del z[self.i]
          

#person_1=students()         
person=students_1()
print(z)
'''
#task-3
z={}

class student:
     def __init__(self):
          count=0
          for i in range(50):
               x=int(input("1.Enter Student Details,\n2.View Details,\n3.Exit,\n4.Delete,\n"))

               if x==1:
                    self.details()
                    count=1
                                    
               elif x==2:
                    if count==1:
                         self.choose()
                    else:
                         print("enter atleast one value \n")
                  
               elif x==3:
                    print("Exit....Bye")
                    break

               elif x==4:
                    if count==2:
                         self.del_1()
                    else:
                         print("enter atleast one value \n")
               
               else:
                    print("enter a value")                

     def details(self):
         self.Roll_no=int(input("Enter a Roll_no:"))
         self.Name=input("Enter a Name:")
         self.Age=int(input("Enter a Age:"))
         self.Class=int(input("Enter a Class:"))
         z.update({self.Roll_no:{"Name":self.Name,"Age":self.Age,"Class":self.Class}})

     def choose(self):
          h=int(input("1.Roll_No,\n2.Name,\n3Age,\n4Class"))

          if h==1:
               self.i=int(input("Enter a Roll_No:"))
             
               if self.i in z:
                    c=z[self.i]
                    print("Name:", c["Name"], "\nAge:", c["Age"], "\nClass:", c["Class"])
                  
          elif h==2:
               s=input("Enter a Name")
             
                    #for self.i,n in z.items():
               
               if s==z[self.Roll_no]["Name"]:
                    print("Roll_no",self.Roll_no,"\nName:",z[self.Roll_no]["Name"],"\nAge",z[self.Roll_no]["Age"],"\nClass:",z[self.Roll_no]["Class"])
                    
                   # print("Roll_no",self.i,"\nName:",n["Name"],"\nAge",n["Age"],"\nClass:",n["Class"])
                           
                         

          
class detail(student):
     def del_1(self):
          if x==4:
               del z[self.i]

person=student()
person.del_1()
          
     
