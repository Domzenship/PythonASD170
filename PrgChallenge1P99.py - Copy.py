"""
Write a program that accepts the lenghts of three sides of a trinagle
as inputs. The program output should indicate whether or not the triangle is an
equilateral triangle.
Author: Joseph A
Date: 5/22/23
Programming Challenge 9 page 99 textbook.
"""
# Input the three sides of the triangle
side1 = float(input("Enter the lenght of side1 of the triangle:"))
side2 = float(input("Enter the lenght of side2 of the triangle:"))
side3 = float(input("Enter the lenght of side3 of the triangle:"))

#Process the values of the triangle anddetermine if it is equilateral or not.
if side1 == side2 and side2 == side3:
    print("The triangle is equilateral!")
else:
    print("The triangle is NOT equilateral!")
