"""
Write a program that receives a series of numbers from the user and allows the
user to press the enter key to indicate that he or she is finished providing
inputs. After the user presses the enter key, the program should print the sum
of the numbers and their average.
Author: Joseph A
Date: 5/23/23
Programming Challenge 9 p101 textbook.
"""
thesum =0           #initialize the variable
count =0            #initialize the variable
while True:         # while True loop condition
    number=input("Enter a number, press the enter key to quit:")
    if number=="":
        break                #this is a break if the user enter nothing 
    thesum +=float(number)   # add the next user number to the previous number
    count +=1                # add 1 more to the count
print("The sum of the numbers entered =", thesum)
if count>0:
    print("The average of the numbers entered =", thesum/count)


