"""
Haniyyah Sardar
Date Due: 3/22/17
Section 05
"""

#prompt user to enter budget for party
budget = float(input("Enter budget for your party: "))

#input cost per slice of pizza
single = float(input("Cost per slice of pizza: "))

#input cost per whole pizza pie
whole = float(input("Cost per whole pizza pie (8 slices): "))

#accumulators
accum_slices = 0
total_slices = 0
#input how many people are attending
#enter number of slices per person
#can't be a negative number, data validation
people = int(input("How many people will be attending your party? "))

#need a nested loop
#for loop to get the slices that each person wants
for i in range(1, people+1):
    total_slices=input("Enter number of slices for person #"+str(i)+": ")
    total_slices = int(total_slices)

    #data validation for if user enters a non-zero number
    while total_slices < 0:
        print("Not a valid entry, try again!")
        print()
        total_slices = input("Enter number of slices for person #"+str(i)+": ")
        total_slices = int(total_slices)
        if total_slices > 0:
            #break out of the while loop and back into the for loop
            break

        elif total_slices < 0:
            continue
    #accumulate the total slices to keep track
    if total_slices >= 0:
        accum_slices += total_slices
        people -= 1

#calculate all of the prices and pies/slices needed
whole_purchase = accum_slices // 8
single_purchase = accum_slices % 8
total = (whole*whole_purchase)+(single*single_purchase)

#3 scenarios
#if the person is under budget
if total < budget:
    print("You should purchase",whole_purchase,"pies and",single_purchase,"slices")
    print("Your total cost will be:",format(total,'.2f'))
    print("You will still have", format((budget-total),'.2f'),"left after your order")

#if user has used exactly all of the budget money
elif total == budget:
    print("You should purchase",whole_purchase,"pies and",single_purchase,"slices")
    print("Your total cost will be:",format(total,'.2f'))
    print("You will have no money left after your order.")

#if the user wants to get more than the budget allows
elif total > budget:
    print("Your order cannot be completed.")
    print("You would need to purchase",whole_purchase,"pies and",single_purchase,"slices")
    print("This would put you over budget by", format( (total-budget),'.2f' ) )


