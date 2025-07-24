# There are three ways to fill the blanks in the python
# 1. Using string concatenation ex. 

name=input("Enter your name:")
age=input("Enter your age:")
print("Hello my name is: " + name + \
      " My age is : " +age) # \ is use to denote that we have write code next line

#2. Using {} and .format() ex.

name=input("Enter your name:")
age=input("Enter your age:")
print("Hello my name is: {}  My age is : {} " .format(name,age))

#3. Usning f before "" and placing var inside the {} inside "" ex.

name=input("Enter your name:")
age=input("Enter your age:")
print(f"Hello my name is: {name}  My age is : {age} ")


# Final program 

print ("Final code..")

adjective=input("Enter the name: ")
verb1=input("verb1:")
verb2=input("verb2:")

madlib=(f"Hello my name is {adjective} and i love to solve problems that comes into mhy daliy routine \
        also I love to do {verb1} with this i also enjoying doing {verb2}. ")

print(madlib)
