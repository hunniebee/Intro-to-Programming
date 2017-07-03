"""
Name: Haniyyah Sardar
Date: 2/1/2017
Class Section: 05
Program Name: Conversions of mL to other units!

"""
#we're creating a program that will let us convert 250 mL into different fluid units!
#we're going to first set a title in between two lines of dashes

#add a line of just dashes (62 total)

print("--------------------------------------------------------------")

#next line "mL to US Fluid Volume Units", this is two tabs in

print("\t\tmL to US Fluid Volume Units")

#next line is just dashes (62). this will complete the title area

print("--------------------------------------------------------------")

#define all the variables
#everything is being converted from 250.0mL into the new unit

ml = 250.0
tsp = ml*.202884
tbsp = tsp/3
cup = tbsp/16
pint = cup/2
quart = pint/2
gallon = quart/4
floz = ml/29.5735

#print the answers for the user
#first column is all one tab in
#second column is pretty much all two tabs in (minus one space), with the exception of pints, quarts and gallons columns

print("\tmL:\t\t",ml,sep="")
print("\ttsp:\t\t",tsp,sep="")
print("\ttbsp:\t\t",tbsp,sep="")
print("\tcup(s):\t\t",cup,sep="")
print("\tpint(s):\t",pint,sep="")
print("\tquart(s):\t",quart,sep="")
print("\tgallon(s):\t",gallon,sep="")
print("\tfl oz:\t\t",floz,sep="")

#finish the program with another set of dashes, the same as above
print("-"*62)

