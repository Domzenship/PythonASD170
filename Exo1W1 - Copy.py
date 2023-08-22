"""
Chapter 3 Project 11
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

import random #use the random module
money = int(input("Enter the amount of dollars:")) # let the user enter total
maxdollar = money
count = 0
maxcount = 0

#this is the beginning of a loop
while money>0:
    count +=1
    #this is the random dice game portion of the program
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    #determine if the dice created a win(7) or a loss
    if dice1+dice2 == 7:
        money +=4
    else:
        money -=1
    #check to see if the maxdollar value has been reached or exceeded
    if money>maxdollar:
     maxdollar=money
     maxcount=count

    #display the results
print("All money was lost after " + str(count) + " number of rolls.\n" +\
               "The player should have stopped at " + str(maxcount) + \
               " dice rolls when the player had $" + str(maxdollar) )
