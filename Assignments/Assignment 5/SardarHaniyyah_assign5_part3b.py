"""
Haniyyah Sardar
Date Due: 3/22/17
Section 05
"""

#determine if the num is a prime num
#prime nums only have divisors that are 1 and itself

  
# for every number within range 1-1000

for i in range(1,1000):

    if i == 1:
        print("1 is technically not a prime number.")
        
    for j in range(2,i):

        if j == i-1:
            if i <= 11:
                print(i,"is a prime number!")
                
            if i == 13:
                print()
                print("... cut ...")
                print()

            if i >= 977:
                print(i,"is a prime number!")
                
        if i % j != 0:
            continue
        
        elif i % j == 0:
            break
                
    

        
