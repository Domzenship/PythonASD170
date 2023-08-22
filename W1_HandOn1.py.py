"""
Project 10 From Pg.63 of the textbook:
------------------
inputs the hourly wage, total regular hours,
and total overtime hours
and displays an employee's total weekly pay.
--------------------
Author: Joseph A
Date:5/22/23
"""

# Inputs for the algorithm
hourlywage = float(input("Enter the employee hourly wage:"))
reghours = float(input("Enter the regular hours worked per week:"))
overtimehours = float(input("Enter the overtime hours worked per week:"))

#Calculate the wages for the week
totalweeklypay = hourlywage * reghours  + overtimehours * 1.5 * hourlywage

#Output the total weekly pay
print("The employee's total weekly pay = $" + str(round(totalweeklypay,2)))

