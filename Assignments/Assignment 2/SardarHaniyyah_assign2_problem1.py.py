"""
Name: Haniyyah Sardar
Date: 2/1/2017
Class Section: 05
Program: Dynamic Tip Calculator
"""

#print out the greeting for user
print("Hello! I'm here to help you calculate your tip.")
bill = float(input("How much was your bill? (Enter a numeric value without commas or dollar signs): "))
percent_tip = float(input("How much tip would you like to leave? (Enter an integer value - i.e. 15 = 15%): "))
people_in_group = int(input("How many individuals are splitting the bill? (Enter an integer value): "))

#calculate the values based on what the user inputs
tip = bill * (percent_tip / 100)
total = bill + tip
cost_per_person = total / people_in_group 

#format the values so that they are two decimal places
formatted_tip = format(tip, ".2f")
formatted_total = format(total, ".2f")
formatted_cost_per_person = format(cost_per_person, ".2f")

#line break
print()

#output a cute message to user about calculating the bill
print("Thanks!  Calculating your bill & tip ...")

#line break
print()

#output the values to user
print("You need to leave $" , formatted_tip , " as a tip." , sep="")
print("Your total bill will be $" , formatted_total , "." , sep = "")
print("Each individual should pay $", formatted_cost_per_person, ".", sep="")




            
