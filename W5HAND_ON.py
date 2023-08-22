"""
ASD210:Fundamentals of Python.
WEEK 5: Chapter 3 Project 11 P101 textbook:
Date: 6/19/2023
Author: Joseph Adjolohoun

In the game of Lucky Sevens, the player rolls a pair of dice.
If the dots add up to 7, the player wins $4; otherwise,
the player loses $1.
Suppose that, to entice the gullible,
a casino tells players that there are lots of ways to win:
(1, 6), (2, 5),
and so on.
A little mathematical analysis reveals that there are not enough
ways to win to make the game worthwhile; however,
because many people’s eyes glaze over at the first mention of mathematics,
 your challenge is to write a program that demonstrates
 the futility of playing the game.
 ------------------------------------------------------------------
 Your program should take as input the amount of money that the player wants
 to put into the pot,and play the game until the pot is empty. At that point,
 the program should print the number of rolls it took
 to break the player, as well as maximum amount of money in the pot. 
"""
#Modify your program from Page 101  (listed below),
#use the exact program requirements, and apply OOP design to it.
#Your new program should contain at least two classes.

import random #use the random module
countmax = 0
maxdollars = 0


#create two classes
class rollDice(object):  #A class to roll dice
    def __init__(self, name):
        self.name=name
        self.dice1=""
        self.dice2=""
    def getdice1(self):  # to roll dice1
        dice1 = random.randint(1,6)
        self.dice1 = dice1
        return(self.dice1)
    def getdice2(self): #roll dice2
        dice2 = random.randint(1,6)
        self.dice2 = dice2
        return(self.dice2)

class calcnumrolls(object): # class to calculate number of rolls
    def __init__(self, name):
        self.name=name
        
        countmax = 0
        maxdollars = 0
    def calcwins(self, other): #calculate winnings or losses
        wincalc = rollDice("")
        dollars=int(other)
        maxdollars = dollars
        count = 0
        countmax = 0
        
        while dollars > 0:
             count +=1
             d1=wincalc.getdice1()
             d2=wincalc.getdice2()

             rolltotal= d1 + d2
             if rolltotal ==7:
                dollars +=4
             else:
                 dollars -=1
             if dollars > maxdollars:
                 maxdollars = dollars
                 countmax = count
                 
        print("You are broke now after " + str(count) + " rolls.\n" +  
                  "You should have quit after " + str(countmax) + \
                  " rolls when you had $" + str(maxdollars) + ".")
        return 
    
def main():
    dollars = int(input(" How many dollars do you have?"))
    cw=calcnumrolls("")
    rd=cw.calcwins(dollars)

if __name__ == "__main__":   
    main()




    
