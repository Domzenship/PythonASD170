"""
ASD210:Fundamentals of Python.
WEEK 4: AssignmentPg. 291 of the textbook:   
Date: 6/12/2023
Author: Joseph Adjolohoun
Program 3: Write a GUI-based program that allows the user to convert
temperature values between degrees Fahrenheit and degrees Celsius.
The interface should have labeled entry fields for these two values.
These components should be arranged in a grid where the labels occupy the
first row and the corresponding fields occupy the second row. At start-up,
the Fahrenheit field should contain 32.0, and the Celsius field should contain
0.0. The third row in the window contains two command buttons,
labeled >>>> and <<<<. When the user presses the first but- ton,
the program should use the data in the Fahrenheit field to compute
the Celsius value, which should then be output to the Celsius field.
The second button should perform the inverse function. 
"""

from breezypythongui import EasyFrame

class temperature(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temp Converter ")


        self.addLabel(text="Celsius", row=0, column=0)
        self.celsiusfield=self.addFloatField(value=0.0, row=1, column=0, precision=2)
        self.addLabel(text="Fahrenheit", row=0, column=1)
        self.fahrenheitfield=self.addFloatField(value=32.0, row=1, column=1, precision=2)

        #fahrenheit's button
        self.addButton(text=">>>>", row = 2, column=0, command=self.calcfahr)

        #Celsius' button
        self.addButton(text="<<<<", row = 2, column=1, command=self.calccels)

    def calcfahr(self):
        degrees = self.celsiusfield.getNumber()
        degrees = degrees*9/5+32
        self.fahrenheitfield.setNumber(degrees)

    def calccels(self):
        degrees = self.fahrenheitfield.getNumber()
        degrees = (degrees - 32)*5/9
        self.celsiusfield.setNumber(degrees)


def main():
    temperature().mainloop()

if __name__ =="__main__": 
    main()
        

        
        
    
