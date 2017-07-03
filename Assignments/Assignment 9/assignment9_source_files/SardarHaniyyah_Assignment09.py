"""
Haniyyah Sardar
Due: 5/1/17
Section 05
"""
while True:
    

    try:
        filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")
        filenametxt = filename + ".txt"
        f = open(filenametxt,"r")
        #file=f.read()
            

    except:
        print("File cannot be found.")
        print()
            
    else:
        print("Successfully opened ", filenametxt,sep='')
        print()
        break

file = f.read()

splitdata = file.split("\n")
#print(splitdata)

#for line in splitdata:

#    splitline = line.split(",")
    
print("**** ANALYZING ****")
print()
#count = 0
#N = 0
#invalid=0
answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answerkey = answerkey.split(",")

invalid = 0
good = 0
grades = [ ]
valid_lines = []
final = []
for line in splitdata:
    
    splitline = line.split(",")
    
    count = 0
    N = 0
    
    invalid_line = 0
    
    for each in splitline:
 #       good +=1
        #print(each)
        if count == 0:
            if each[0] != "N" or len(each) != 9 or each[1:].isnumeric() == False:
                print("Invalid line of data: N# is invalid")
                print(splitline)
                print()
                invalid += 1
                invalid_line += 1
            #continue
               
        count+=1


       
    if count != 26:
        print("Invalid line of data: does not contain exactly 26 values:")
        print(splitline)
        print()
        invalid += 1
        invalid_line += 1

    if invalid_line == 0:
        valid_lines.append(splitline)
        good += 1
        final.append(splitline[0])

        

    
if invalid == 0:
    #if good == len(splitline) and N == 1
    print("No errors found!")
    print()

print("**** REPORT ****")
print()
print("Total valid lines of data:",good)
print("Total invalid lines of data:",invalid)
print()

for splitline in valid_lines:
    correct = 0
    for i in range(len(splitline)-1):
        if splitline[i+1] == answerkey[i]:
            correct +=4
        elif splitline[i+1] == "":
            correct += 0
        elif splitline[i+1] != answerkey[i]:
            correct -= 1
    grades.append(correct)

grades2 = []
for grade in grades:
    grades2.append(grade)
grades2.sort()


sum_of_grades = sum(grades)
avg = (sum_of_grades / len(grades))
print("Mean (average) score:",format(avg,".2f"))
print("Highest score:",max(grades))
print("Lowest score:",min(grades))
print("Range of scores:", (max(grades) - min(grades)))

if len(grades) % 2 != 0:
    grades2.sort()
    print("Median score:",grades2[int(len(grades)//2+1)])
else:
    grades2.sort()
    median = (grades2[int(len(grades)/2-1)] + grades2[int(len(grades)/2)])/2 
    print("Median score:", median)

unique=[]
seen=[]

for i in range(len(grades)):
    if grades[i] not in unique:
        unique.append(grades[i])
        seen.append(1)
    else:
        position = unique.index(grades[i])
        seen[position] += 1
      
mode = max(seen)
loc = seen.index(mode)
mode_list=[ ]

for i in range(len(seen)):
    if seen[i] == mode:
        mode_list += [unique[i]]
        


print("Mode score(s): ",end="")
for item in mode_list:
    print(item,"",end="")


final_grades  = filename + "_grades.txt"
grades_file = open(final_grades,'w')
for i in range(len(final)):
    forfile = (final[i] + ','+ str(grades[i])+'\n')
    grades_file.write(forfile)
    
grades_file.close()

print()
curveq = input("Would you like to apply a curve to the scores? (y)es or (n)o?: ")
if curveq == "y":
    newavg = float(input("Enter desired mean score: "))
    
    adding = newavg - avg
    
    curved_grades = []
    for i in range(len(grades)):
        new_score = grades[i] + adding
        new_score = format(new_score,'.2f')
        curved_grades.append(new_score)
        
    curved_file = filename + "_grades_with_curve.txt"
    curved_grade = open(curved_file,'w')
    for i in range(len(final)):
        forcurvedfile = (final[i] + ',' + str(grades[i]) + ',' + str(curved_grades[i]) + '\n')
        curved_grade.write(forcurvedfile)
    curved_grade.close()
    print("Done! A new grade file has been written (",curved_file,")",sep='')


    
