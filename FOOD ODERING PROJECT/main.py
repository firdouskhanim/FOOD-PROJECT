import admin
import user
import sys

class main:
 def execution(self,choice):    
    if choice==1:
       data={}
    n=2
    for i in range(n):
        foodid=int(input("ENTER THE FOOD ID :"))
        item=input("ENTER THE ADD FOOD ITEM:    ")
        price=input("ENTER THE  ADD FOOD ITEM PRICE:  ")
        qty=input("ENTER THE FOOD  OF QUANTITY:  ")
        data[foodid]=[item,price,qty]
        print(data)   
    obj.add_item(data)

    id=int(input("ENTER THE FOOD ID: "))
    obj.show(id)
    print("YOUR ID GENERATE SUCCESSFULLY")

    obj.getname()

    n=input("ENTER THE SEARCH FOOD ITEM ID:   ")
    obj.view_item(n)

    print("SHOW THE MENU")
    obj.display_food()

    id=int(input("ARE YOU WANT TO DELETE ITEM IN MENU:   "))
    obj.remove_item(id)
    print("SUCCESSFULLY DELETE IN MENU")  

    if choice==2:
      a=input("ENTER THE FULL NAME:    ")
      b=input("ENTER THE MOBILE NUMBER:   ")
      c=input("ENTER THE EMAIL ID :   ")
      d=input("ENTER THE ADDRESS:    ")
      e=input("ENTER THE PASSWORD:    ")
      obj1.show(a,b,c,d,e)
      obj1.log_in()
      value=int(input("[1.] PLACE NEW ORDER [2.] ORDER HISTORY [3.] UPDATE PROFILE \nENTER YOUR CHOICE:     "))
      obj1.display(value)
      sys.exit()  
       
if __name__=="__name__":
   obj=admin("ashish",5)
   obj1=user()
   obj2=main()
   while True:
      print("****WELCOME TO MY RESTAURANT****")
      print("[1.] ADMIN \n[2.] USER")
      choice=int(input("Please select your operation:     "))
      obj2.execution(choice)                    