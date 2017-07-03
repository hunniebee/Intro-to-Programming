"""
Haniyyah Sardar
Date Due: 2/27/17
Section: 05
"""

#data validation- user must enter a positive integer
col = 0
while True:
    num = int(input("How many columns? "))

    if num <= 0:
        print("Invalid entry, try again!")
        continue

    else:
        break

#first half of the arrow
#print out the number they entered worth of stars -1!
    
while col < (num-1):
    #the spaces are num-1, the last spot is occupied by the star
    print(" " * col,"*",sep="")
    #add one to the column so that the loop will stop eventually
    col += 1

#2nd half of the arrow INCLUDES the number entered worth of spaces and star
while num > 0:
    #print out num-1 spaces, the last space will be occupied by the *
    print(" " * (num-1), "*",sep="")
    #decrease the num by 1 so the loop will eventually stop
    num -= 1

    

