"""
Haniyyah Sardar
Date Due: 3/22/17
Section 05
"""

#ask for num of students
#make sure it's pos: data validation!
while True:
    # ask for num of students in class
    total_students = int(input("How many students are in your class? "))
    if total_students > 0:
        break
    elif total_students <= 0:
        print("Invalid # of students, try again.")
        print()

#ask for total num of tests that are given
#make sure it's pos: data validation!
while True:
    # and total num of tests that are given
    total_tests = int(input("How many tests in this class? "))
    if total_tests > 0:
        print()
        print("Here we go!")
        print()
        break
    elif total_tests <= 0:
        print("Invalid # of tests, try again.")

# accum variables
all_avg = 0

# enter scores FOR EACH STUDENT
for i in range(1,total_students+1):
    print("**** Student #",i,"****",sep="")
    
    #need individ. student's score to reset for every student
    #accum INSIDE one of the loops (but outside the inner loop)
    student_score = 0
    for test in range(1,total_tests+1):
        while True:
            score = float(input("Enter score for test #"+str(test)+": "))
            if score >= 0:
                student_score += score
                break
            else:
                print("Invalid score, try again")
    #calculate avg for a student
    #also keep track of the total avg's for all students
    avg = student_score / total_tests
    all_avg += avg
    print("Average score for student #",i," is ",format(avg,'.2f'),sep="")
    print()

print("Average score for all students is:", format((all_avg / total_students),'.2f'))
# ensure that these are positive
# hint: a while loop inside a for loop
# once all students' scores have been collected, display that student's avg

# calculate the overall avg score for the ENTIRE CLASS

