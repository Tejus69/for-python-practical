# #to understand Different List and tuple Operations using builtin functions

# list = [2,1,3,4]
# list2=[7,8,9]

# print("List at a start")
# print(list)

# #adding element in list 
# list.append(5)
# list.insert(4,6)#it inserts at a particular index
# list.extend(list2)
# print("List after Inserting")
# print(list)


# #Removing 
# list.remove(7)
# list.pop()
# print("list after Removing")
# print(list)

# #sorting opertaion on a list 

# list.sort() # isse se by default ascending order me print hoga
# print(list)
# list.sort(reverse=True) # descending
# print(list)


#Tupple

vehical = ("car","Bike","Truck","Bike")
tuple = (2,3,5,5)

print(vehical.index("Bike"))  # returns the index of the element
print(vehical.count("Bike"))  # returns the count of the element
print(len(vehical))
print(max(vehical))
print(min(vehical))
print(sum(tuple))
