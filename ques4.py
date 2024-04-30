# 4. To understand Constructors, Inner class and Static method

class student :                          
   name = "Raju"
   age = "19"

   def __init__(self,name ,age ):               #constrctor
     self.name = name 
     self.age = age

   def show(self):
      print(self.name,self.age)

   @staticmethod                               #static method
   def getSchool(): 
     print("A.M. School")
     


   class laptop :                               # inner class
      brand = "Dell"
      ram = 16
     
      def show(self):
       print(self.brand,self.ram)

      


stud1 = student("VAdapav",20)

stud1.show()
stud2 = student.laptop()
stud2.show()

stud1.getSchool()
student.getSchool()
