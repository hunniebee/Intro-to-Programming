"""
Haniyyah Sardar
Due: 4/10/17
Section 05
"""

# username conditions:
# only alphanumeric characters
# BETWEEN 8-15 characters long
# NO SPECIAL CHARACTERS
# first and last character CANT be a digit
# MUST have one uppercase
# MUST have one lowercase
# MUST have one number

while True:

    username = input("Enter a username: ")
    valid = 0

    print("* Length of username:",len(username))
    print("* All characters are alpha-numeric:",username.isalnum())
    if username.isalnum() == True:
        valid += 1
        
     #username[0].isnumeric() == False and username[-1].isnumeric() == False:
    print("* First & last characters are not digits:", (not(username[0].isdigit()) and not(username[-1].isdigit() ) ) ) 
    if not(username[0].isdigit()) and not(username[-1].isdigit() ) == True:
        valid += 1
          
    upper = 0
    lower = 0
    digit = 0
    for c in username:
        if c.isupper() == True:
            upper +=1
            if upper == 1:
               valid += 1
        if c.islower() == True:
            lower += 1
            if lower == 1:
                valid += 1
        if c.isnumeric() == True:
            digit += 1
            if digit == 1:
                valid += 1
            
            
    print("* # of uppercase characters in the username:",upper)

    print("* # of lowercase characters in the username:",lower)

    print("* # of digits in the username:",digit)

    if valid == 5:
        print("Username is valid!")
        break
    else:
        print("Username is invalid, please try again")
        print()
        
        



