"""
ASD201:Fundamentals of Python.
WEEK 3:Exercise 
Date: 6/10/2023
Author: Joseph Adjolohoun
Week 3 Exercise - Turtle
Design a program with user-defined functions that allow the creation
of different shapes and custom sizes based on the user's 
selection for the following: 
Circle, Star, Square, and Hexagon. 
"""
import math
from turtle import Turtle

#Initialize the variables
#Create Shape Functions
#Circle
def drawCircle(t,x,y, radius):
    """ This draws a circle with the given center point and radius"""
    t.up()
    t.goto(x +radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)

#Star
def drawStar(t,x):
            for i in range(5): # execute loop 5 times for a star
                t.forward(x) # moving turtle 100 units forward
                t.right(144) # rotate turtle 100 degree right
#Square:
def drawSquare(t, side): # Lenght of each side
    # Drawing first side
    t.forward(side)# Forward turtle by x units
    t.left(90) # turn turtle by 90 degrees
    
    #Drawing second side
    t.forward(side)# Forward turtle by x units
    t.left(90) # turn turtle by 90 degrees

    #Drawing third side
    t.forward(side)# Forward turtle by x units
    t.left(90) # turn turtle by 90 degrees
    
    #Drawing fourth side
    t.forward(side) # forward turtle by x units back to the original position

#Hexagon
def drawHexagon(t, x):
    for i in range(6): # executing loop 6 times for 6 sides
        t.forward(x) # Move forward by 90 units
        t.left(300) # Turn left the turtlr by 300 degrees
def main():
    while True:
        print("Choose from Square, Circle, Star, and Hexagon for the shape:")
        print("Enter "" to exit:")
        shape=input("Select the shape you want to draw:") # Users enter shape
        if str(shape) == "Circle":
            break
            exit()
        Size = int(input("Select the size for the shape:")) # users enter size
        if str(shape) =="":
            # drawCircle(Turtle(), x, y, radius)
            x = 0
            y = 0 # Set the center of the shape
            drawCircle(Turtle(), x, y, Size)
        elif str(shape)=="square":
            drawSquare(Turtle(), Size)
        elif str(shape) == "star":
            drawStar(Turtle(), Size)
        elif str(shape) =="hexagon":
            drawHexagon(Turtle(), Size)

if __name__== "__main__":
    main()

    

        
        
    
