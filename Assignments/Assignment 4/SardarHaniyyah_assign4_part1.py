"""
Haniyyah Sardar
Date Due: 2/27/17
Section: 05
"""
import random

#ask the user how many sides of the dice they want
#can only be the numbers listed!!!

#accumulator for number of tries, doubles, and the total of the dies
numtries = 0
doubles = 0
die1_total = 0
die2_total = 0

while True: 
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))

    #data validation
    
    if sides==4 or sides==6 or sides==8 or sides==10 or sides==12 or sides==20:
        print()
        print("Thanks! Here we go ...")
        break
    else:
        print("Sorry, that's not a valid size.")
        

#4 sided die
while sides == 4:

    #let the two dice get random rolls
    die1 = random.randint(1,4)
    die2 = random.randint(1,4)
    #increase the tries by one
    numtries += 1
    #increase the totals of the dice 
    die1_total += die1
    die2_total += die2

    #count num of times that doubles are rolled
    if die1==die2:
        doubles += 1

    #formatting the program, only show 4 lines of tries
    if numtries <= 4:
        print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")

    #if greater than 4 tries, then there needs to be a "continue" shown
    if numtries == 4:
       print(". . . continue . . .")

    #once we roll snake eyes
    #print the outcomes of each of the first four rolls of the dice
    #print out the avg
    #print out the percentages
    if die1==die2==1:
        if numtries <=4:
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )
            break
     #print out the outcome of the snake eyes roll along with relevant values/numbers
        elif numtries !=4:
            print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )
            break

#6 sided die
while sides == 6:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    numtries += 1
    die1_total += die1
    die2_total += die2
    
    if die1==die2:
        doubles += 1
        
    if numtries <= 4:
        print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
        
    if numtries == 4:
       print(". . . continue . . .")

    if die1==die2==1:
        if numtries <=4:
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )

            break
 
        elif numtries !=4:
            print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )
            break
        
#8 sided die
while sides == 8:
    die1 = random.randint(1,8)
    die2 = random.randint(1,8)
    numtries += 1
    die1_total += die1
    die2_total += die2
    
    if die1==die2:
        doubles += 1
        
    if numtries <= 4:
        print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
        
    if numtries == 4:
       print(". . . continue . . .")

    if die1==die2==1:
        if numtries <=4:
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )

            break
 
        elif numtries !=4:

            print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )
            break

#10 sided die
while sides == 10:
    die1 = random.randint(1,10)
    die2 = random.randint(1,10)
    numtries += 1
    die1_total += die1
    die2_total += die2
    
    if die1==die2:
        doubles += 1
        
    if numtries <= 4:
        print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
        
    if numtries == 4:
       print(". . . continue . . .")

    if die1==die2==1:
        if numtries <=4:
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )

            break
 
        elif numtries !=4:
            
            print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )
            break

#12 sided die
while sides == 12:
    die1 = random.randint(1,12)
    die2 = random.randint(1,12)
    numtries += 1
    die1_total += die1
    die2_total += die2
    
    if die1==die2:
        doubles += 1
        
    if numtries <= 4:
        print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
        
    if numtries == 4:
       print(". . . continue . . .")

    if die1==die2==1:
        if numtries <=4:
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )

            break
 
        elif numtries !=4:

            print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )
            break

#20 sided die
while sides == 20:
    die1 = random.randint(1,20)
    die2 = random.randint(1,20)
    numtries += 1
    die1_total += die1
    die2_total += die2
    
    if die1==die2:
        doubles += 1
        
    if numtries <= 4:
        print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
        
    if numtries == 4:
       print(". . . continue . . .")

    if die1==die2==1:
        if numtries <=4:
            print()
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )

            break
 
        elif numtries !=4:
            print()
            print(numtries,". die number 1 is ",die1," and"," die number 2 is ",die2,".",sep="")
            print("You got snake eyes! Finally! On try number ",numtries,"!",sep="")
            print("Along the way you rolled doubles ",doubles," times (",format(((doubles/numtries)*100),".2f"),"% of all rolls were doubles)",sep="")
            print("The average roll for die #1 was",format( (die1_total/numtries),".2f" ) )
            print("The average roll for die #2 was",format( (die2_total/numtries),".2f" ) )
            break
