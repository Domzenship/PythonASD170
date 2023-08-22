"""
ASD210:Fundamentals of Python.
WEEK 4: Hand-On From Pg. 291 of the textbook: 
Date: 6/12/2023
Author: Joseph Adjolohoun

Write a GUI-based program that plays
a guess-the-number game in which the roles of thecomputer and the user are the
reverse of what they arein the Case Study of this chapter. In this version
of the game,the computer guesses a number between 1 and 100 and the user
providesthe responses. The window should display the computer’s guesses
with a label.The user enters a hint in response, by selecting one of a
set of command buttons labeled Too small, Too large,and Correct.
When the game is over, you should disable
these buttons and wait for the user to click New game,as before.
"""

# import external modules
import random
from breezypythongui import EasyFrame

# initialize variables

class guessinggame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Guessing Game")
        self.lowerbound= 1
        self.upperbound=100
        self.count=0
        self.mynumber=(self.lowerbound + self.upperbound)//2
        guess = "Is the number " + str(self.mynumber) + "?"
        self.mylabel = self.addLabel(text = guess, row=0, column=0,sticky="NEEW", columnspan=4)
        self.small=self.addButton(text="Too Small", row=1, column=0, command=self.toosmall)
        self.large=self.addButton(text="Too Large", row=1, column=1, command=self.toolarge)
        self.correct=self.addButton(text="Correct", row=1, column=2, command=self.correct)
        self.newgame=self.addButton(text="New Game", row=1, column=3, command=self.newgame)

        
    def toosmall(self):# Too small Function
        # The computer guessing was too samll
        self.count +=1
        self.lowerbound=self.mynumber + 1
        self.mynumber=(self.lowerbound + self.upperbound)//2
        guess="Is the number" + str(self.mynumber) + "?"
        self.mylabel["text"] = guess 


    def toolarge(self): # Too large Function
        self.count +=1
        self.upperbound=self.mynumber - 1
        self.mynumber=(self.lowerbound + self.upperbound)//2
        guess="Is the number" + str(self.mynumber) + "?"
        self.mylabel["text"] = guess 

    def correct(self):# Correct guess function
        # compute guess is correct
        self.count +=1
        guess="The computer guess the number in " + str(self.count) + "Tries"
        self.mylabel["text"] = guess
        self.small["state"] = "disabled"
        self.large["state"] = "disabled"
        self.correct["state"] = "disabled"
    
    def newgame(self): #New game function
        #Reset the game
        self.lowerbound=0
        self.upperbound=200
        self.count=0
        self.mynumber=(self.lowerbound + self.upperbound)//2
        guess="Is the number " + str(self.mynumber) + "?"
        self.mylabel["text"] = guess 
        self.small["state"] = "normal"
        self.large["state"] = "normal"
        self.correct["state"] = "normal"

def main():
    #Run the game
    guessinggame().mainloop()

if __name__ =="__main__": 
    main()


        

        

        
