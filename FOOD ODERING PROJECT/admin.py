import json as js
class admin:
  def __init__(self,name,discount):
       self.discount=discount
       self.name=name
       
  def add_item(self,menu):
      self.menu=menu
      fh=open("data.json","w")
      js.dump(self.menu,fh)
      fh.close()

      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
          print(i,j)
      fh.close()
      
  def show(self,foodid):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
         if i==foodid:
            print(foodid)

  def getname(self):
      print("ADMIN NAME :",self.name)  

  def view_item(self,itemid):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
        if i==itemid:
           print(i,j)

  def display_food(self):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
          print(i,j)
      fh.close() 

  def remove_item(self,itemid):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
        if i==itemid:
           r.remove(i)
           
