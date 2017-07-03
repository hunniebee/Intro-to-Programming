"""
Haniyyah Sardar
4/10/17
Section 05
"""

#word = input("Enter a word: ")
#number = int(input("Enter a number: "))

def add_letters(word,num):

    import random
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    x = random.randint(1,2)
    new_word=""
    

    for c in word:
        characters = ""
        
        for i in range(num):
            if x == 1:
                characters += upper[random.randint(0,25)]
            else:
                characters += lower[random.randint(0,25)]
        new_word += c+characters
        
    return new_word


def remove_letters(word,num):

 

    new_word = word[::num+1]
    
    return new_word



def shift_characters(word,num):

    new_word=""

    for c in word:
        new_word += chr( ( ord(c) + num ) )

    return new_word


                
