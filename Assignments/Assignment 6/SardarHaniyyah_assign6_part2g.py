"""
Haniyyah Sardar
3/29/17
Section 5
"""


import myfunctions
import random

while True:
    num_problems = int(input("How many problems would you like to attempt? "))
    if num_problems <= 0:
        print("Invalid number, try again")
        print()
        continue
    else:
        break

while True:
    width = int(input("How wide do you want your digits to be? 5-10: "))
    if width < 5 or width > 10:
        print("Invalid width, try again")
        print()
        continue
    else:
        break

while True:
    character = input("What character would you like to use? ")
    if len(character) > 1:
        print("String too long, try again")
        print()
        continue
    elif len(character)==1:
        print()
        print("Here we go!")
        print()
        break

correct = 0


for problem in range(num_problems):
    print("What is .....")
    print()
    int1 = random.randint(0,9)
    int2 = random.randint(0,9)
    op = random.randint(1,2)

    myfunctions.print_number(int1, width, character)
    print()

    if op == 1:
        print(myfunctions.plus(width, character))
        real_ans = myfunctions.check_answer(int1,int2,(int1+int2),'+')
    else:
        print(myfunctions.minus(width, character))
        real_ans = myfunctions.check_answer(int1,int2,(int1-int2),'-')
        
    print()
    myfunctions.print_number(int2,width, character)

    if op == 1:
        user_ans = int(input('= '))
        user_check = myfunctions.check_answer(int1,int2,user_ans,'+')
        if user_check == real_ans:
            print("Correct!")
            print()
            correct += 1
            continue
        else:
            print("Sorry, that's not correct.")
            print()
    if op == 2:
        user_ans = int(input('= '))
        user_check = myfunctions.check_answer(int1,int2,user_ans,'-')
        if user_check == real_ans:
            print("Correct!")
            print()
            correct += 1
            continue
        else:
            print("Sorry, that's not correct.")
            print()


print("You got",correct,'out of',num_problems,'correct!')
    
        
