# Write a python program to understand built-in strings and set functions 
set = {1,2,3}

#adding elements

set.add(4)
set.add(5)
set.add(6)

print(set)

# removing elements

set.remove(2)
set.pop()

print(set)

#updating sets
set2 = {5,6,7,8}

set.update(set2) # it performs a union operation 
print("Updated set: ", set)

print(set.difference(set2)) #printing different elements from 2 sets

#STRINGS

string = "king"

print(string.capitalize())   # capitalize he first letter
print(string.casefold())     #convert string in lowercase
print(string.count("g"))     #count the elements 
print(string.center(34))     #adds horizontal padding 
print(string.upper())        #Converts all lowercase characters in a string into uppercase
print(string.lower())        #Converts all uppercase characters in a string into lowercase
