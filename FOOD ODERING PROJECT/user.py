import json as js
import admin
class user:
  def __init__(self):
      self.userid=1
      self.detail={}
 
  def show(self,name,mobno,email,address,password):
      self.name=name
      self.mobno=mobno
      self.email=email
      self.address=address
      self.password=password
      self.detail[self.userid]=[ name,mobno,email, address,password]       
      print(self.detail)

  def log_in(self):
      name=input("ENTER THE NAME FOR LOG IN:  ")
      password=input("ENTER THE PASSWORD:     ") 
      if name==self.name and password==self.password:
         print("YOUR ARE LOG IN SUCCESSFULLY ")
         print("****WELCOME TO MY RESTAURANT****")
      else:
         print("WRONG ID AND PASSWORD PLEASE TRY AGAIN.") 

  def display(self,ch): 
      if self.ch==1:
         fh=open("data.json")
         r=js.load(fh)
         for i,j in r.items():
             print(i,j)
         fh.close()
      t=[]
      n=int(input("ENTER THE HOW MUCH DO YOU WANT TO ORDER:    "))
      for i in range(n):
          self.id=int(input("ARE YOU WANT TO PLACE A NEW ORDER AT THE RESTAURANT:   "))
          t.append(self.id)
          print(t)
          for i,j in r.items():
            if i==self.id:   
               print(i,j)
               return True 
      fh.close()        

  
      if self.ch==3:  
        for i,j in self.detail.items():
         if i==self.userid:
            self.name=input("ENTER THE FULL NAME:    ")
            self.mobno=input("ENTER THE MOBILE NUMBER:   ")
            self.email=input("ENTER THE EMAIL ID :   ")
            self.address=input("ENTER THE ADDRESS:    ")
            self.password=input("ENTER THE PASSWORD:    ")
            self.detail[self.userid]=[ self.name,self.mobno,self.email, self.address,self.password]       
            print(self.detail)     
