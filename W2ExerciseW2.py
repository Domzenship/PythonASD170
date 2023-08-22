"""
ASD210:Fundamentals of Python.
WEEK2: Exercise 2
Date: 6/2/2023
Author: Joseph Adjolohoun

#Take the input for file name
#Open the input file & #Read the data
#Generate a grade for each student record
#Print the report without duplicate records
"""
def grade(percent):
    grd=''
    if percent>= 90:
        grd='A'
    elif percent >= 80:
        grd='B'
    elif percent>= 70:
        grd='C'
    elif percent>= 60:
        grd='D'
    else:
        grd='F'
    return grd

filename=input("Enter the name of the file:")# Enter file name
f=open(filename,'r')  # Open file
# print(filename)
# exit()
lines=[]              # Create an empty list

for line in f:        #loop through the lines in the text file
    words = f.readlines() #.split
    for word in words:
        if not word in lines:
            lines.append(word) # append the lines to the list
lines.sort()
for word in lines:
    sp=word.split()
    #<student id> <last name> <total score> <letter grade>
    print (sp[0],sp[1], int(sp[2])+ int(sp[3])+ int(sp[4]), grade(int(sp[2])+int(sp[3])+int(sp[4])))
