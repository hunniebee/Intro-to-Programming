"""
Haniyyah Sardar
Due: 5/8/17
Section 05
"""


word = input("Enter a word to test: ")

openreviews = open("movie_reviews.txt","r")

allreviews= openreviews.read()
allreviews = allreviews.lower()

splitreviews = allreviews.split("\n")


num_of_word = 0
score = 0

for eachreview in splitreviews:

    splitline = eachreview.split()
    for i in range(1,len(splitline)):
        
        if splitline[i] == word:
            #print(eachreview)
            num_of_word +=1
            score += int(splitline[0])
            
print("'",word,"' appears ",num_of_word, " times",sep='')

try:     
    avg = (score/num_of_word)
    
except:
    print("There is no average score for reviews containing the word '",word,"'",sep='')
    print("Cannot determine if this word is positive or negative")

else:
    print("The average score for reviews containing the word '",word,"' is ",avg,sep='')

    if avg >= 2.0:
        print("This is a positive word")
    else:
        print("This is a negative word")


    

