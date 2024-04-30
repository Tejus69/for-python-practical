# Write a python program to understand different types of inheritance

"""single inheritance"""

class Vehical :
   
   def __init__(self):
      print("use Public Transports")

    
class car(Vehical):
    def what(self):
       print("We are in car function")


class truck(car,Vehical):
   def what(self):
      print("Its a multiple inheritanse")

class bike(car):
   def what():
      print("its multilevel inheritance")



    

v1 = Vehical()
lambo = car()
volvo = truck()

volvo.what()

lambo.what()
