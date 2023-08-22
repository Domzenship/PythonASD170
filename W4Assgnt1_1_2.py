"""
ASD210:Fundamentals of Python.
WEEK 4:Ch 9 project 1 P349 textbook: 
Date: 6/13/2023
Author: Joseph Adjolohoun

1- Add three methods to the Student class that compare two Student objects.
One method should test for equality. A second method should test for less than.
The third method should test for greater than or equal to. In each case,
the method returns the result of the comparison of the two students’ names.
Include a main function that tests all of the comparison operators.

2-This project assumes that you have completed Project 1 (above).
Place several Student objects into a list and shuffle it.Then run the sort method
with this list and display all of the students’ information.

"""
class Student(object): # """Represents a student."""
    def __init__(self, name, number):
        self.name = name
        self.scores = []
        
        for count in range(number):
            self.scores.append(0)

    def getName(self): #"""Returns the student's name."""
        return self.name

    def setScore(self, i, score): #"""Resets the ith score, counting from 1.""" 
        self.scores[i - 1] = score

    def getScore(self, i): #Returns the ith score, counting from 1 
         return self.scores[i - 1]

    def __str__(self): #Returns the string representation of the student.
       return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other): #Equal to
        if self is other:
            return True    # Capital T
        elif type(self) != type(other):
            return False   # Capital F
        else:
            return self.name == other.name

    def __lt__(self, other):# Less than 
        return self.name < other.name

    def __ge__(self, other):# Greater than or equal to
        return self.name >= other.name 

            
        

def main():
    N=Student("Nathan",1)
    P=Student("Joseph",2)
    U=Student("Darrick",3)
    J=Student("Julissa",4)
    Y=Student("Yasim",4)
    L=Student("Letrel",5)
    
    studentlist=[]
    
    studentlist.append(N)
    studentlist.append(P)
    studentlist.append(U)
    studentlist.append(J)
    studentlist.append(Y)
    studentlist.append(L)
    
    #Equal to
    print(N==P)
    print(P==N)
    #Less than
    print(N<P)
    print(P<N)
    #Greater than or equal to
    print(N>=P)
    print(P>=N)

    print("Unsorted list")

    for i in studentlist:
        print(i)
    print("--------------")
    studentlist.sort()

    for i in studentlist:
        print(i)

 
if __name__ == "__main__":
    main()
                   
            
        
        
    
