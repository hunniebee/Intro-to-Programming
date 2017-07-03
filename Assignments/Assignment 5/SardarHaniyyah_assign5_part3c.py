"""
Haniyyah Sardar
Date Due: 3/22/17
Section 05
"""

#user input for start and end number
#start and end must be positive
#end > start


while True:
    start = int(input("Start number: "))
    end = int(input("End number: "))
    if start < 0 or end < 0:
        print("Start and end must be positive")
        print()
        continue
    if end < start:
        print("End number must be greater than start number")
        print()
        continue
    else:
        print()
        break

#determine if the num is a prime num
#prime nums only have divisors that are 1 and itself


# for every number within range start - end

for num in range(start,end+1):

    if num > 1:
    
        for j in range(2,num):
            if (num % j) == 0:
                break
        else:
            print(num)
                

              
    

        
