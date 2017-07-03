"""
Haniyyah Sardar
Due: 4/10/17
Section 05
"""
#PART 1B

# username conditions:
# only alphanumeric characters
# BETWEEN 8-15 characters long
# NO SPECIAL CHARACTERS
# first and last character CANT be a digit
# MUST have one uppercase
# MUST have one lowercase
# MUST have one number


while True:

    valid = 0
    username = input("Enter a username: ")
    if len(username) >= 8 and len(username) <= 15:
        valid += 1

    print("* Length of username:",len(username))
    print("* All characters are alpha-numeric:",username.isalnum())
    if username.isalnum() == True:
        valid += 1
        
    
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

    if valid == 6:
        print("Username is valid!")
        print()
        break
    else:
        print("Username is invalid, please try again")
        

        

#PASSWORD VALIDATOR

#AT LEAST 8 CHARACTERS long
# cannot contain the user's username
# at least one upper, one lower, one digit, and (#,$,%,&)
while True:
    password = input("Enter a password: ")
    validp = 0
    print("* Length of password:",len(password))
    if len(password) > 8:
        validp +=1

    if username in password:
        print("* Username is part of password: True")
    else:
        print("* Username is part of password: False")
        validp +=1


    upperp = 0
    lowerp = 0
    digitp = 0
    specialp = 0
    for c in password:
        if c.isupper() == True:
            upperp +=1
            if upperp == 1:
                validp += 1
        if c.islower() == True:
            lowerp += 1
            if lowerp == 1:
                validp += 1
        if c.isnumeric() == True:
            digitp += 1
            if digitp == 1:
                validp += 1
        if c in "#$%&":
            specialp += 1
            if specialp == 1:
                validp +=1

    print("* # of uppercase characters in the password:",upperp)

    print("* # of lowercase characters in the password:",lowerp)

    print("* # of digits in the password:",digitp)
    print("* # of special characters in the password:",specialp)

    if validp == 6:
        print("Password is valid!")
        
        break
    else:
        print("Password is invalid, please try again")
        print()



