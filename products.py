#task
#products
'''
class products:
    def detail(self):        #or
    #def __init__(self):
        self.Pr_Name=input("Enter Products Name:")
        self.Pr_id=int(input("Enter a Products Id:"))
        self.Pr_Exp=int(input("Enter a Products Exp_:"))
        self.Pr_price=int(input("Enter a Products Price:"))
        self.Pr_Quantity=int(input("Enter a Products Quantity:"))

    def print(self):
        print("Products_Name-",self.Pr_Name)
        print("Products_Id-",self.Pr_id)
        print("Products_Exp-",self.Pr_Exp)
        print("Products_price-",self.Pr_price)
        print("Products_Quantity-",self.Pr_Quantity)
        print("Total amount:",self.Pr_price*self.Pr_Quantity)

a=products()
a.detail()
#or
a.print()
'''
#task-2
class name:
    def rice(self):
        Qu=int(input("Enter a Products Quantity:"))
        print("Product_id",2001)
        print("Product_Exp","20/12/2025")
        print("Productprice",155)
        print("ProductQuantity",Qu)
        print("Total amount:",Qu*155)
        
class name1:
    def wheat(self):
        Qu=int(input("Enter a Products Quantity:"))
        print("Product_id",2002)
        print("Product_Exp","15/1/2025")
        print("Productprice",200)
        print("ProductQuantity",Qu)
        print("Total amount:",Qu*200)

class name2:
    def sugar(self):
        Qu=int(input("Enter a Products Quantity:"))
        print("Product_id",2003)
        print("Product_Exp","10/3/2025")
        print("Productprice",100)
        print("ProductQuantity",Qu)
        print("Total amount:",Qu*100)

        
class products(name,name1,name2):
    def detail(self):
        a=input("Enter a Products Name:")
        if a=="rice":
            self.rice()
        elif a=="wheat":
            self.wheat()
        elif a=="sugar":
            self.sugar()
            
        else:
            print("Not....Products")

z=products()
z.detail()

