"""
Haniyyah Sardar
4/10/17
Section 05
"""

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


while True:

    process = input("(e)ncode, (d)ecode or (q)uit: ")

    if process == "e":

        while True:
            num = int(input("Enter a number between 1 and 5: "))
            if num >= 1 and num <= 5:
                break
            else:
                continue

        word = input("Enter a phrase to encode: ")

        encoded = add_letters(word,num)
        encodedfinal = shift_characters(encoded,num)

        print("Your encoded word is:",encodedfinal)
        print()

    elif process == "d":

        while True:
            num = int(input("Enter a number between 1 and 5: "))
                
            if 1 <= num <= 5:
                break
            else:
                continue

        word = input("Enter a phrase to decode: ")

        decoded = remove_letters(word,num)
        decodedfinal = shift_characters(decoded, -num)

        print("Your decoded word is:",decodedfinal)
        print()

    else:
        break
                
