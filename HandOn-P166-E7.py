"""
ASD210:Fundamentals of Python.
WEEK2: Hand-On (p.166 Ex7 textbook)
Date: 5/31/2023
Author: Joseph Adjolohoun

Write a program that inputs a text file. The program should print
the unique words in the file in alphabetical order.
"""

#Get the file name of the file to open
file1 = input("Enter the filename:")

#Open the file
f1 =open(file1,'r')
uword=[]   # initialize the unique words

# Add words to the unique list of words from the file
for line in f1:         #Loop through the list of words in the file
    word = line.split()   #Seperate the words
    for word in f1:
        if not word in uword:  # check to see if word exist in unique list
            uword.append(word) #
            
uword.sort()                  # perform a sort on list of words

#Print the unique list of words (sorted in alphabetical order)
for word in uword:
    print(word)
f1.close()
