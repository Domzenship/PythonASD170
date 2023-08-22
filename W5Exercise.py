''' Week 5 Exercise
ASD210:Fundamentals of Python.
Date: 6/20/2023
Author: Joseph Adjolohoun

#refer to the textbook page 365 for the starting point on this project.
# Import required module for  threading
# Define a custom class that extends Thread
# Constructor
# Call the constructor of the superclass
# Set the name and num attributes
# Set the finished attribute to False 
# Main thread method
# Loop from num to 0
# Print the countdown
# Sleep for one second
# Set the finished attribute to True
# Additional method to check if thread has finished
# Create five instances of the MyThread class
# Start them threads
# Wait for both threads to finish before continuing
# Check if each thread has finished
# Print a message to indicate that the program has finished'''

from  threading import *

import time

class thread1(Thread):

    def __init__(self, name, num1):
        #Thread.__init__(self, name="thread"+str(num1))
        
        super().__init__()
        self.name = name
        self.num=num1
        self.finish = False

    def finished(self):
        return self.finish

    def mainmeth(self):
        #Loop from num to 0
        for x in range(self.num, 1, -1):
            print(f"{self.name} t-- {x}")
            self.finish = True
            
#main thread method
    def run(self):
        #Loop from num to 0
        for x in range(self.num, -1, -1):
            print(f"\n{self.name} {x}\n")

        self.finish- True
        time.sleep(1)
        

def main(): # Build 5 threads
    thread2 = []
    thread2.append(thread1("trd1",1))
    thread2.append(thread1("trd2",2))
    thread2.append(thread1("trd3",3))
    thread2.append(thread1("trd4",4))
    thread2.append(thread1("trd5",5))

#Start the threads
    for t in thread2:
        t.start()

#Check if each thread has finished
        for t in thread2:
            print(f"{t.name} {t.finished()}")
            print(f"{t.name} finished= {t.finished()}")
            print("All done!") 

    
if __name__=="__main__":
    main()
 
