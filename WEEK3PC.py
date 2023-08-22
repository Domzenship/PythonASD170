"""
ASD201:Fundamentals of Python.
WEEK 3: Week3 Assignment - Programming challenge
Date: 6/10/2023.
Implement this program by using at least 3 user defined functions.

1) A value returning function

2) A function with parameter (s)

3) A function with both returning value and parameters. 

A “Make your pizza” program allows the user 
to see the available menu with different pizza sizes, 
various ingredients, and prices. The user can input 
one pizza topping at a time and returns a message that 
the user added [topping] to the pizza after each input. 
The program allows the user to indicate when they are finished 
adding toppings and finally outputs a message telling 
the user how many toppings were
 added to the imaginary pizza and its total cost.

"""

pizzasize = {1:"Small: $3.99", 2:"Medium: $5.99", 3:"Large: $7.99"}
toppinglist = ['1. Olives', '2. Pepperoni', '3. Sausage', '4. Anions', '5. Marshmallows', ' 6. Whipped cream', '7. strawberries']
addedtoppings=[]
pizzacost=0.00

def pizzasize1(x):     #return the pizza size
    if str(x)!='':
        return pizzasize[x]
    
def listaddedtoppings(): # return the list of toppings
    if len(addedtoppings)>0:
              i=0
              while i < len(addedtoppings):
                    print(addedtoppings[i].split()[1]) # display the added toppings
                    i=i+1
    return
             
def calculatetoppingcost(numberoftoppings):#calculate the cost of pizza
    toppingcost=(numberoftoppings *.75)     #calculate the cost of the toppings
    pizza_cost = pizzacost + toppingcost # 
    return pizza_cost

def main():
    #Display a list of pizza size
    print("Pizza Sizes:")
    print(pizzasize)  # Pizza size - select one size

    #input a list of pizza sizes
    pizza_size = int(input("Enter the number next to the pizza size:"))
    print('You have selected ', pizzasize1(pizza_size))   # this execute the pizza size

    #Display a menu of the pizza toppings
    print("Pizza Toppings $.75 for each topping:")
    print(toppinglist)

    #Allow user to exit when they enter
    while True:    #loop through the user's topping selection
        topping=input('Enter the number of toppings you want to add to your pizza:'\
                      '(hit the enter key to finish your order)')
        if str(topping)=="":  # exit when nothing is entered by user
            break
        elif int(topping)<=0 or int(topping)>int(len(toppinglist)-1):#validate the choice
             print("Invalid number, PLEASE TRY AGAIN:")
        else:
            print("You have added", toppinglist[int(topping)-1], " to your pizza.")# output the added topping to the customer
            addedtoppings.append(toppinglist[int(topping)-1]) # add topping to list

    # Display the pizza information
  
    print("You have chosen a ", pizzasize1(pizza_size), " size pizza, with", len(addedtoppings), "toppings:")
    listaddedtoppings()
    
    #Display the cost of the pizza
    print("The total charge for your pizza is:$", float((pizzasize[pizza_size].split("$"))[1]) + calculatetoppingcost(len(addedtoppings)))

main()   

        
