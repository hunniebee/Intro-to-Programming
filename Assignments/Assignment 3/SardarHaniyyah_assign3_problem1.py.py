"""
Haniyyah Sardar
Date Due: 2/15/2017
Class Section: 05
"""

# print out the title for user
print("Valid Triangle Tester")

#line break
print()

#prompt the user to enter the x and y coordinates of 3 sides of a triangle
#make sure they are floats!
p1x = float(input("Enter Point #1 - x position: "))
p1y = float(input("Enter Point #1 - y position: "))

p2x = float(input("Enter Point #2 - x position: "))
p2y = float(input("Enter Point #2 - y position: "))

p3x = float(input("Enter Point #3 - x position: "))
p3y = float(input("Enter Point #3 - y position: "))

#calculate the distance between the sides of the triangle
s1 = (((p1x - p2x)**2 + (p1y - p2y)**2))**0.5
s2 = (((p1x - p3x)**2 + (p1y - p3y)**2))**0.5
s3 = (((p2x - p3x)**2 + (p2y - p3y)**2))**0.5

#format the sides so that the answers are to 2 decimal places
fs1 = format(s1,".2f")
fs2 = format(s2,".2f")
fs3 = format(s3,".2f")

#line break
print()

#output the length of the sides for user
print("The length of each side of your test shape is:")

#line break
print()

print("Side 1:",fs1)
print("Side 2:",fs2)
print("Side 3:",fs3)

#line break
print()

#redefine the sides' values so they are evaluated to 2 decimal places
s1 = float(fs1)
s2 = float(fs2)
s3 = float(fs3)

#figure out of the triangle is valid
#also print what type of triangle it is

if (s1+s2)>s3 and (s2+s3)>s1 and (s3+s1)>s2:
    print("This is a valid triangle!")

    if s1==s2==s3:
        print("This is an equilateral triangle")

        #print out an equilateral triangle in turtle
        #thick black outline filled with blue
        import turtle
        turtle.setup(500,500)
        turtle.pensize(10)

        #set up fill color: blue
        turtle.fillcolor("blue")

        #ISSUE: triangle won't close
        #ISSUE: sometimes the code for this doens't work? see screenshot
        #ISSUE: if you move the cursor forward the length of the side there's
        #an overshoot
        
        #move pointer to the first point that the user entered
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(p1x,p1y)
        turtle.pendown()
        #turtle.forward(s1)
        turtle.goto(p2x,p2y)
        #turtle.forward(s2)
        turtle.goto(p3x,p3y)
        turtle.goto(p1x,p1y)
        #turtle.forward(s3)
        turtle.end_fill()
        
 #   if s1 == s2 and s2==s3 and s3==s1:
        
    elif ((s1==s2 or s1==s3 or s2==s3) and (s1!=s2 or s1!=s3 or s2!=s3)):
        print("This is an isoceles triangle")

        #print out an isoceles triangle in turtle
        #thick black outline filled with yellow
        import turtle
        turtle.setup(500,500)
        turtle.pensize(10)

        #set up fill color: yellow
        turtle.fillcolor("yellow")
        
        #move pointer to the first point that the user entered
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(p1x,p1y)
        turtle.pendown()
        #turtle.forward(s1)
        turtle.goto(p2x,p2y)
        #turtle.forward(s2)
        turtle.goto(p3x,p3y)
        turtle.goto(p1x,p1y)
        #turtle.back(s3)
        turtle.end_fill()

    elif s1 != s2 != s3:
        print("This is a scalene triangle")

        #print out an scalene triangle in turtle
        #thick black outline filled with green
        import turtle
        turtle.setup(500,500)
        turtle.pensize(10)

        #set up fill color: green
        turtle.fillcolor("green")
        
        #move pointer to the first point that the user entered
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(p1x,p1y)
        turtle.pendown()
        #turtle.forward(s1)
        turtle.goto(p2x,p2y)
        #turtle.forward(s2)
        turtle.goto(p3x,p3y)
        #turtle.forward(s3)
        turtle.goto(p1x,p1y)
        turtle.end_fill()

else:
    print("This is not a valid triangle")

"""
#extra credit
#equilateral triangle = thick black outline filled with blue
#isoceles triangle = thick black outline filled with yellow
# scalene triangle = thick black outline filled with green
import turtle

#set up the canvas
turtle.setup(500,500)

#make the lines thick
turtle.pensize(10)

#move pointer to the first point that the uder entered
turtle.penup()
turtle.goto(p1x,p1y)
turtle.pendown()
turtle.forward(s1)
turtle.goto(p2x,p2y)
turtle.forward(s2)
turtle.goto(p3x,p3y)
turtle.forward(s3)
"""




