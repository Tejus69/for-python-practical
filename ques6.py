# To understand Polymorphism using Operator overloading, Method overloading, Method overriding in Python

# function Overloading 

def product(a, b):
    p = a * b
    print(p)
 
# Second product method
# Takes three argument and print their
# product
 
 
def product(a, b, c):
    p = a * b*c
    print(p)
 
# Uncommenting the below line shows an error
# product(4, 5)
 
 
# This line will call the second product method
product(4, 5, 5)


# Python program to demonstrate 
# method overriding 


# Defining parent class 
class Parent(): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Parent"
		
	# Parent's show method 
	def show(self): 
		print(self.value) 
		
# Defining child class 
class Child(Parent): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Child"
		
	# Child's show method 
	def show(self): 
		print(self.value) 
		
		
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show() 
obj2.show() 


# oeperator overloading



class example :

    def __init__(self,x):
        self.x = x

    def __add__(self,U) :
        return self.x + U.x
    
object_1 = example(int(input("Enter the fisrt no.")))
object_2 = example(int(input("Enter the second no.")))
print(": ", object_1 + object_2)
