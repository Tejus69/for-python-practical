# Write a python program to understand different file handling operations.

import os 

try :
    f=open("C:\\Users\\tejsh\\OneDrive\\Desktop\\Python\\pracForCollege\A.txt","r")

    # f.write("Hey Its Teja bhai ayt \n  hlwoooo")

    print(f.readline())  # for reading single line 
    print(f.readlines())  # for reading all line 

    print("File created")

except: print("File error")


else:  
    f.close()
    print("file closed")



if os.path.exists("C:\\Users\\tejsh\\OneDrive\\Desktop\\Python\\pracForCollege\A.txt"):
    os.remove("C:\\Users\\tejsh\\OneDrive\\Desktop\\Python\\pracForCollege\A.txt")

else: 
    print("File not availbale")


"""
file ko khalisave karna ho to 'x'  
file ko write karna ho to "w"
file ko read karna ho to r"    """
