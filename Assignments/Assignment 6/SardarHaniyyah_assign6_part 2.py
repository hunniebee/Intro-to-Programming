"""
Haniyyah Sardar
Date Due: 3/29/17
Section 05
"""



def horizontal_line(width, character):
    
    horiz = character * width
    return horiz


def vertical_line(shift, height, character):
 #   bigline=""
    for i in range(height):
        line = " " * shift + character
        #print(line)
    return line

def two_vertical_lines(width, height, character):

    for i in range(height):
        line = character + " " * (width - 2) + character
        
        #print(line)
    return line


def number_0(width, character):
    top = horizontal_line(width, character)
    middle = two_vertical_lines(width, 3, character)
    bottom = horizontal_line(width, character)
    pattern=(top+'\n'+middle+'\n'+middle+'\n'+middle+'\n'+bottom)
    return pattern
#ASK ABOUT THE MIDDLE PART WHY DO I NEED TO ADd it 3 times to VARIABLe????!???

def number_1(width, character):
    pattern = vertical_line(width-1, 5, character)
    return (pattern+ '\n')*5

    
def number_2(width, character):
    pattern = horizontal_line(width, character)
    pattern2 = vertical_line(width-1, 1, character)
    pattern3 = horizontal_line(width, character)
    pattern4 = vertical_line(0, 1, character)
    pattern5 = horizontal_line(width, character)
    total_pattern = (pattern + '\n'+pattern2+ '\n'+pattern3+ '\n'+pattern4+ '\n'+pattern5)
    return total_pattern


def number_3(width, character):
    top = horizontal_line(width, character)
    side = vertical_line(width-1,1,character)
    pattern=(top+'\n'+side+'\n'+top+'\n'+side+'\n'+top)
    return pattern

def number_4(width, character):
    top = two_vertical_lines(width, 2, character)
    middle = horizontal_line(width, character)
    bottom = vertical_line(width-1,2,character)
    pattern=top+'\n'+top+'\n'+middle+'\n'+bottom+'\n'+bottom
    return pattern


def number_5(width, character):
    top = horizontal_line(width, character)
    middle = vertical_line(0,1,character)
    middle2 = vertical_line(width-1,1,character)
    pattern = top+'\n'+middle+'\n'+top+'\n'+middle2+'\n'+top
    return pattern


def number_6(width, character):
    top = horizontal_line(width, character)
    middle = vertical_line(0,1,character)
    middle2 = two_vertical_lines(width, 1, character)
    pattern=top+'\n'+middle+'\n'+top+'\n'+middle2+'\n'+top
    return pattern


def number_7(width, character):
    top = horizontal_line(width, character)
    bottom = vertical_line(width-1,4,character)
    #print(bottom)
    pattern=top+'\n'+bottom+'\n'+bottom+'\n'+bottom+'\n'+bottom
    return pattern


def number_8(width, character):
    top = horizontal_line(width, character)
    middle = two_vertical_lines(width,1,character)
    pattern=top+'\n'+middle+'\n'+top+'\n'+middle+'\n'+top
    return pattern


def number_9(width, character):
    top = horizontal_line(width, character)
    middle = two_vertical_lines(width,1,character)
    bottom=vertical_line(width-1,2,character)
    pattern = top+'\n'+middle+'\n'+top+'\n'+bottom+'\n'+bottom
    return pattern


def print_number(number, width, character):
    if number == 0:
        print(number_0(width, character))
    elif number == 1:
        print(number_1(width, character))
    elif number ==2:
        print(number_2(width, character))
    elif number == 3:
        print(number_3(width, character))
    elif number == 4:
        print(number_4(width, character))
    elif number == 5:
        print(number_5(width, character))
    elif number == 6:
        print(number_6(width, character))
    elif number == 7:
        print(number_7(width, character))
    elif number ==8:
        print(number_8(width, character))
    elif number == 9:
        print(number_9(width, character))
        
    
def plus(width, character):
    if width % 2 !=0:
        top = vertical_line(width//2, 1, character)
        middle = horizontal_line(width, character)
        pattern = top+'\n'+top+'\n'+middle+'\n'+top+'\n'+top
        return pattern
    elif width % 2 == 0:
        top = vertical_line(int( (width/2)-1 ),1,character+character)
        middle=horizontal_line(width, character)
        pattern = top+'\n'+top+'\n'+middle+'\n'+top+'\n'+top
        return pattern


def minus(width, character):
    top = ' '
    middle = horizontal_line(width, character)
    pattern = top+'\n'+top+'\n'+middle+'\n'+top+'\n'+top
    return pattern


def check_answer(num1,num2,ans,operator):
    if operator == '+':
        if num1 + num2 == ans:
            return True
        else:
            return False
    if operator == '-':
        if num1 - num2 == ans:
            return True
        else:
            return False








    
