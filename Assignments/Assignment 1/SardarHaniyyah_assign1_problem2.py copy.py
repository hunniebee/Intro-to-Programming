"""
Haniyyah Sardar
Date: 2/1/2017
Class Section: 05
Program: "Possible Orders of Three Names"

Description: In this program we are asking the user for three names. Those
names are then outputted in every possible order for the user in two different
formatting styles.
"""

#ask the user for three names, and store them in 3 separate variables
name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 = input("Please enter name #3: ")

#line break
print()

#print the three names for the user;
#tell user "Here are your names in every possible order:"
print("Here are your names in every possible order:")

#line of dashes
#--------------------------------------------
print("--------------------------------------------")

#line break
print()

#the names will all be separated with commas
print("1. ",name1,", ", name2, ", ", name3, sep="")

#line break
print()

#names will be separated with commas
print("2. ",name1,", ", name3, ", ", name2, sep="")

#line break
print()

#names separated with commas
print("3. ",name2, ", ", name1, ", " , name3, sep="")

#line break
print()

#names each on a separate line
print("4.", name2)
print(name3)
print(name1)

#line break
print()

#names are each on a separate line
print("5.", name3)
print(name2)
print(name1)

#line break
print()

#names are each on a separate line
print("6.", name3)
print(name1)
print(name2)

