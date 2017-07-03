"""
Haniyyah Sardar
Date Due: 2/27/17

Section: 05
"""

#data validation
#ask user for a number of sticks between 10-100
# keep track of each player's turn 
sticks = 0
take = 0
turn = 0

while True:
    #ask user for sticks between 10-100
    sticks = int(input("How many sticks (10-100)? "))

    #if the number entered is between 10-100 then continue w program/break loop
    if sticks <= 100 and sticks >=10:
        print("Great Let's play ...")
        print()
        break
    #if sticks are too low, let them know and re prompt user
    elif sticks < 10:
        print("Sorry that's too few sticks. Try again.")
        continue
    #if sticks are too high, let them know and re prompt user
    elif sticks > 100:
        print("Sorry that's too many sticks. Try again.")
        continue

# everything else in a loop
# until all sticks are gone
while True:
    #keep track of whose turn it is, start with player 1
    if turn % 2 == 0:
        print("Turn: Player 1")
        print("There are",sticks,"sticks on the table.")
    else:
        print("Turn: Player 2")
        print("There are",sticks,"sticks on the table.")

    # output number of sticks so that user(s) know at the end of every turn
    #print("There are",sticks,"sticks on the table.")

    #ask user for how many sticks
    take = int(input("How many sticks do you want to take (1, 2 or 3)? "))

    # can only enter 1,2,3
    if take == 1 or take == 2 or take == 3:
        if (sticks-take) > 0:

            # now calculate the number of sticks left if valid num entered
            sticks -= take
            #increase turn by 1
            turn += 1
            print()
            continue

        # if take is 1,2, or 3 but total sticks will be negative, then reprompt
        if (sticks-take) < 0:
            print ("Sorry, that's not a valid number.")
            print()
            continue
        
        #if num of sticks = 0 then game is over
        elif (sticks-take) == 0:
            print ()
            print("There are no sticks left on the table. Game over!")

            #since take was +1 each correct time, calculate who won
            if take-1 % 2 == 0:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

            break

    #if user entered a num other than 1,2, or 3
    elif take != 1 or take != 2 or take !=3:
        print("Sorry, that's not a valid number.")
        print()
        

