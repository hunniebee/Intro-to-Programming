"""
Name:Haniyyah Sardar
Date: 2/01/2017
Class Section: 05
Program Name: Place Value Madness!!
"""

# ask the user for 2 integers
# assume user will enter a positive whole number between 0-10,000
value1 = input("Enter value 1: ")
value2 = input("Enter value 2: ")

#convert the values from strings into integers so we can work with them
int_value1 = int(value1)
int_value2 = int(value2)

#define the ones places values for each number entered
onesplace_value1 = int_value1 % 10
onesplace_value2 = int_value2 % 10
total_ones = onesplace_value1 + onesplace_value2

#define the tens places values for each number entered
tensplace_value1 = int_value1 // 10 % 10
tensplace_value2 = int_value2 // 10 % 10
total_tens = tensplace_value1 + tensplace_value2

#define the hundreds places values for each number entered
hundredsplace_value1 = int_value1 // 10 // 10 % 10
hundredsplace_value2 = int_value2 // 10 // 10 % 10
total_hundreds = hundredsplace_value1 + hundredsplace_value2

#define the thousands places values for each number the user enters
thousandsplace_value1 = int_value1 // 10 // 10 // 10
thousandsplace_value2 = int_value2 // 10 // 10 // 10
total_thousands = thousandsplace_value1 + thousandsplace_value2


#line break
print()

#print "Place Value Totals:"
print("Print Value Totals:")

#line break
print()

#calculate the place values
#make sure the totals will all be one tab in

print("\t",onesplace_value1, "+",onesplace_value2,"=",total_ones,"one(s)")
print("\t",tensplace_value1,"+",tensplace_value2,"=",total_tens,"ten(s)")
print("\t",hundredsplace_value1, "+", hundredsplace_value2, "=", total_hundreds, "hundred(s)")
print("\t",thousandsplace_value1, "+", thousandsplace_value2, "=", total_thousands, "thousand(s)")






