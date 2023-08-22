"""
ASD210:Fundamentals of Python.
Date: 5/31/2023
Author: Joseph Adjolohoun
Week 2 : Project #2 on page 165 textbook 
Write a program that allows the user to navigate the lines of text in a file.
The program should prompt the user for a filename
and input the lines of text into a list.
The program then enters a loop in which it prints the number of
lines in the file and prompts the user for a line number.
Actual line numbers range from 1 to the number of lines in the file.
If the input is 0, the program quits. Otherwise,
the program prints the line associated with that number.
"""
#Get the name of the text file to open
file1= input("Enter the name of the text file to open:")
opfile=open(file1,'r') # open the text file for read

lines = [] #Create an empty list

for line in opfile:  #loop through all the lines in text file
    lines.append(line) # Add the lines to the list

# Move through the lines until the user enters a "0"

while True:          #loop until there are no more values or the user exits the program
    print("This file has ", len(lines), " lines in it.")
    if len(lines) == 0: # if there are no lines in the file exit
        break
    linenum= int(input("Enter a line number [0 to quit:")) #enter a line number
    if linenum==0: # if the user enterd a 0 ends the program
        break
    elif linenum>=len(lines): #if user entered a value greater than the number of lines
        print("Error: line number must be less than:" , len(lines))
    else:
        print(linenum, ":", lines[linenum]) # print the line number selected by the user 
