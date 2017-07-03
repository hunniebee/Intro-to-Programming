"""
Haniyyah Sardar
4/10/17
Section 05
"""

def string_length(word):
    count = 0
    for c in word:
        count += 1

    return count


def string_isalpha(word):

    if word == "":
        return False

    for c in word:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            continue
        else:
            return False

    return True


def string_isupper(word):

    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if word == "":
        return False

    for c in word:
        if c in upper:
            continue
        else:
            return False
    return True


def string_isdigit(word):

    if word == "":
        return False

    for c in word:
        if c in "1234567890":
            continue
        else:
            return False
    return True


def string_swapcase(word):
    new_word = ""
    
    for c in word:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_word += chr ( ord(c) + 32 )

        elif c in "abcdefghijklmnopqrstuvwxyz":
            new_word += chr ( ord (c) - 32 )

        else:
            new_word += c

    return new_word


def string_lower(word):
    new_word = ""

    for c in word:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_word += chr ( ord(c) + 32 )
        else:
            new_word += c
    return new_word
        
