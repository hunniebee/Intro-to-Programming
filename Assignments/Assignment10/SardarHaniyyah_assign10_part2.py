"""
Haniyyah Sardar
Due 5/8/17
section 05
"""

import time 
openreviews = open("movie_reviews.txt","r")

allreviews= openreviews.read()
allreviews = allreviews.lower()

splitreviews = allreviews.split("\n")

words = {}

timebefore = time.time()
for eachreview in splitreviews:

    splitline = eachreview.split()
    for i in range(1,len(splitline)):
            
        if splitline[i] not in words:
            words[splitline[i]] = [int(splitline[0]),1]
            #print(words)
            #print(words)
            
        else:
 #           for i in range(len(words[splitline[i]])):
            words[splitline[i]][0] += int(splitline[0])
            words[splitline[i]][1]  += 1
        #print(words)

timeafter = time.time()

time = format(timeafter-timebefore,'.2f')

print("Initializing sentiment database")
print("Sentiment database initialization complete")
print("Total unique words analyzed:",len(words))
print("Analysis took",time,"seconds to complete")
print()

test = input("Enter a phrase to test: ")

splittest = test.split(" ")

words_in_phrase = 0
total_avg = 0
for item in splittest:
    if item not in words:
        print("* '",item,"' does not appear in any moview reviews",sep='')
    else:
        count = words[item][1]
        avg = words[item][0] / count
        print("* '",item,"' appears ",count," times with an average score of ",avg,sep='')
        words_in_phrase += 1
        total_avg += avg
        
if words_in_phrase > 0:
    print("Average score for this phrase is:",total_avg/words_in_phrase)
    if total_avg/words_in_phrase >= 2.00:
        print("This is a POSITIVE phrase")
    else:
        print("This is a NEGATIVE phrase")

else:
    print("Not enough words to determine the sentiment.")
