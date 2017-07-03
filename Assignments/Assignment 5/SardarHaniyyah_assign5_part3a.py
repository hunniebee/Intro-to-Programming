"""
Haniyyah Sardar
Date Due: 3/22/17
Section 05
"""

# user enters in a positive number
#data validation; only positive numbers, no zeroes
while True:
    pos = int(input("Enter a positive number to test: "))
    if pos > 0:
        print()
        break
    else:
        print("Not a valid number; positive integers only please!!")


#determine if the num is a prime num
#prime nums only have divisors that are 1 and itself

for i in range(2,pos):

    if pos % i != 0:
        print(i,"is NOT a divisor of",pos,"... continuing")

        if i == pos-1:
            print()
            print(pos,"is a prime number!")
            break
        
    elif pos % i == 0:
        print(i,"is a divisor of",pos,"... stopping")
        print()
        print(pos,"is not a prime number.")
        break
    
        
    


        
