"""
Week 5 Programming Chalenge
ASD210:Fundamentals of Python.
Date: 6/24/2023
Author: Joseph Adjolohoun

"""
import threading
import time


class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def add_topping(self, topping):
        self.toppings.append(topping) # missing code

    def bake(self):
        print("Baking pizza...")
        time.sleep(5)
        print("Pizza is ready!")

    def __str__(self):
        toppings_str = ", ".join(self.toppings)
        return f"A {self.size}-inch pizza with {toppings_str} toppings"


class Order:
    def __init__(self):
        self.pizzas = []   #missing code

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def view_order(self):
        print("Current order:")
        for index, pizza in enumerate(self.pizzas):
            print(f"Pizza #{index + 1}: {pizza}")

    def bake_order(self):
        print("Baking all pizzas...")
        threads = []
        for pizza in self.pizzas:   #missing code    
            thread = threading.Thread(target=pizza.bake)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()          #missing code    
        print("Order is ready!")


def main():
    order = Order()
    while True:
        print("What would you like to do?")
        print("1. Add a pizza to the order")
        print("2. View the current order")
        print("3. Bake the order")
        print("4. Quit")
        choice = input("> ")
        if choice == "1":
            print("What size of pizza would you like?")
            size = int(input("> "))
            toppings = input("Enter toppings (separated by commas): ").split(",")
            pizza = Pizza(size, toppings)  #missing code
            order.add_pizza(pizza)
        elif choice == "2":
            print("Here is your order info:")
            order.view_order() #missing code
        elif choice == "3":
            print("Your order is in the oven:")
            order.bake_order() #missing code
            break
        elif choice == "4":
            break               #missing code
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
