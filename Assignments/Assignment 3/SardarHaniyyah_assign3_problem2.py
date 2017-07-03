"""
Haniyyah Sardar
Date Due: 2/15/2017
Section: 05
"""

#make available the random module
import random

#store a random secret number (int)
secret = random.randint(1,10)

#output intro to user
print("I'm thinking of a number between 1 and 10!")

#ask the user to guess a first number
first_guess = int(input("What's your guess? "))

#if the first guess is right
if first_guess == secret:
    print("You got it!")
    print("The secret number was ",secret,".",sep="")
    print("It took you 1 try to guess the number.")

#if the first guess is too low
if first_guess < secret:
    print("Too low, try again.")

    #ask user for a second guess
    second_guess = int(input("What's your guess? "))

    #see if the second guess = secret number
    if second_guess == secret:
        print("You got it!")
        print("The secret number was ",secret,".",sep="")
        print("It took you 2 tries to guess the number.")

    #if the second guess is too low again
    #let user know it's too low
    if second_guess < secret:
        print("Too low, try again.")

        #ask user for a third and final guess
        third_guess = int(input("What's your guess? "))

        #see if the third guess is right
        if third_guess == secret:
            print("You got it!")
            print("The secret number was ",secret,".",sep="")
            print("It took you 3 tries to guess the number.")

        #if third guess is not right, tell user they didn't get it right
        else:
            print("The secret number was ",secret,".",sep="")
            print("You didn't guess the number.")

    #if the second guess is too high
    #let user know that it's too high
    if second_guess > secret:
        print("Too high, try again.")

        #ask user for a third and final guess
        third_guess = int(input("What's your guess? "))

        if third_guess == secret:
            print("You got it!")
            print("The secret number was ",secret,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",secret,".",sep="")
            print("You didn't guess the number.")
            
                
        
if first_guess > secret:
    print("Too high, try again.")

    second_guess = int(input("What's your guess? "))
        
    if second_guess == secret:
        print("You got it!")
        print("The secret number was ",secret,".",sep="")
        print("It took you 2 tries to guess the number.")

    if second_guess < secret:
        print("Too low, try again.")

        third_guess = int(input("What's your guess? "))
        
        if third_guess == secret:
            print("You go it!")
            print("The secret number was ",secret,".",sep="")
            print("It took you 3 tries to guess the number.")

        else:
            print("The secret number was ",secret,".",sep="")
            print("You didn't guess the number.")
            
    if second_guess > secret:
        print("Too high, try again.")
        third_guess = int(input("What's your guess? "))

        if third_guess == secret:
            print("You got it!")
            print("The secret number was ",secret,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",secret,".",sep="")
            print("You didn't guess the number.")
    

