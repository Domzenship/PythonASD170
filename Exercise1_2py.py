"""
ASD210:Fundamentals of Python.
WEEK2: Exercise 2
Date: 6/2/2023
Author: Joseph Adjolohoun
The goal of this program is to generate a student grade report without
duplicates.

Input:
A file in which each line has the form
<student id> <last name> <score for quiz> <score for homework> <score for final exam>

Output:
A report has the form:

<student id> <last name> <total score> <letter grade>

"""
#Take the input for file name
fileName = input("Enter the file name: ")

#Open the input file
inputFile = open(fileName, 'r')
   

#Read the data
text = inputFile.read()

for line in inputFile:
    inputFile = line.split()
    for data in inputFile:
        studentId = inputFile[0]
        lastName = inputFile[1]
        quizScore = inputFile[2]
        homeworkScore = inputFile[3]
        finalScore =  inputFile[4]
        totalScore = quizScore + homeworkScore + finalScore
    
#Generate a grade for each student record
quizScore = int(input("Enter the quiz score:"))
homeworkScore = int(input("Enter the homework score:"))
finalScore =int(input("Enter the final score:"))        
print("The totalScore is", quizScore + homeworkScore + finalScore)
totalScore = int(input("Enter the totalScore:"))
if totalScore >= 90:
        letter  = 'A'
elif totalScore >= 80: 
        letter = 'B'
elif totalScore >= 70:  
        letter = 'C'
elif totalScore >= 60:
        letter = 'D'
else:         
        letter = 'F'
        
print("The letter grade is", letter)
    
print("%-15s%15s%15s%15s%15.2f" % (studentId, lastNname, totalScore, letter))


