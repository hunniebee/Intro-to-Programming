"""
Haniyyah Sardar
Date Due: 2/15/17
Section: 05
"""

#ask the user to enter his/her birthday
print("Intructions: Enter the start date and birthday for an employee to determine their age at the start of employment.")

#input start date
input("Enter start date MMDDYYYY: ")

#ask user to input their bday in MMDDYYYY format
bday = int(input("Enter birth date MMDDYYYY: "))

#isolate the year
onesplace_year = str(bday % 10)
tensplace_year = str(bday // 10 % 10)
hundredsplace_year = str(bday // 10 // 10 % 10)
thousandsplace_year = str(bday // 10 // 10 // 10 % 10)
year = int(thousandsplace_year + hundredsplace_year + tensplace_year + onesplace_year)

#isolate the day
onesplace_day = str(bday // 10 // 10 // 10 // 10 % 10)
tensplace_day = str(bday // 10 // 10 // 10 // 10 // 10 % 10)
day = int(tensplace_day + onesplace_day)

#assign proper suffix for the day user was born
#days that end in "st"
if day == 1 or day == 21 or day == 31:
#if day == 1 or 21 or 31:
    day_with_suffix = str(day) + "st"
    
#days that end in "nd"
if day == 2 or day == 22:
    day_with_suffix = str(day) + "nd"

#days that end in "rd"
if day == 3 or day == 23:
    day_with_suffix = str(day) + "rd"

#days that end in "th"
if (day >= 4 and day <= 20) or (day >= 24 and day <= 30):
    day_with_suffix = str(day) + "th"

#isolate the month
onesplace_month = str(bday // 10 // 10 // 10 // 10 // 10 // 10 % 10)
tensplace_month = str(bday // 10 // 10 // 10 // 10 // 10 // 10 // 10 % 10)
month = int(tensplace_month + onesplace_month)

#assign proper month to the month entered by user (MM)
if month == 1:
    word_month = "January"
elif month == 2:
    word_month = "February"
elif month == 3:
    word_month = "March"
elif month == 4:
    word_month = "April"
elif month == 5:
    word_month = "May"
elif month == 6:
    word_month = "June"
elif month == 7:
    word_month = "July"
elif month == 8:
    word_month = "August"
elif month == 9:
    word_month = "September"
elif month == 10:
    word_month = "October"
elif month == 11:
    word_month = "November"
elif month == 12:
    word_month = "December"

#output the date born for user
print("The contestant was born on ",word_month," ",day_with_suffix,", ",year,sep="")

#define eligibility
eligible = "ELIGIBLE: The contestant will be 21 by the time taping begins"
not_eligible = "NOT ELIGIBLE: The contestant won't be 21 by the time taping begins"

#figure out if user will be 21 by the time show starts
#if born during or before 1994 then automatically eligible
if year <= 1994:
    print(eligible)

# if born in 1995, then eligible if born in April or before
elif year == 1995:
    if (month >= 1 and month <= 4):
        print(eligible)
    #if born in the month of May, can be eligible if born on the 1st ONLY
    elif month == 5:
        if day == 1:
            print(eligible)
        else:
            print(not_eligible)
else:
    print(not_eligible)
    

