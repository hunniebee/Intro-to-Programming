"""
Name: Haniyyah Sardar
Date Due: 2/8/17
Class Section: 05
Name: "PokeMath!"
"""

#print out the title and dashes
print("\tPokemon Distance Calculator")
print("------------------------------------------")

#line break
print()

#ask the user for name of 1st pokemon
first_pokemon = input("1. Enter name of first pokemon: ")

#ask the user for name of 2nd pokemon
second_pokemon = input("2. Enter name of second pokemon: ")

#ask for x and y coordinates of first pokemon. make sure to convert to float
xcoordinate_first = float(input("3. Enter x coordinate of first pokemon: "))
ycoordinate_first = float(input("4. Enter y coordinate of first pokemon: "))

#ask for x and y coordinates of second pokemon, converting to floats
xcoordinate_second = float(input("5. Enter x coordinate of second pokemon: "))
ycoordinate_second = float(input("6. Enter y coordinate of second pokemon: "))

#define the distance formula
distance = float(((xcoordinate_second - xcoordinate_first)**2 + (ycoordinate_second - ycoordinate_first)**2)**0.5)

#line break
print()

#output the distance for the user, to two decimals
print("\tThe distance between",first_pokemon,"and",second_pokemon,"is",format(distance,".2f"),"inches.")

