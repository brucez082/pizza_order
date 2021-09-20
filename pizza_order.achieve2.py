#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brucez.19233
#
# Created:     20/09/2021
# Copyright:   (c) brucez.19233 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
from datetime import date

def force_name(message, lower, upper):
    while True:
        name = str(input(message))
        if len(name) >= lower and len(name) <= upper and name.isalpha():
            break
        else:
            print("Please enter in a valid name, e.g the number of letters has to be between {} - {}".format(lower, upper))
    return name

def force_number(message, lower, upper):
    while True:
        try:
            number = int(input(message))
            if number >= lower and number <= upper:
                break
            else:
                print("Please enter a number between {} - {}".format(lower, upper))
        except:
            print("Please enter a number instead of a piece of string")
    return number

def force_cellphone(message, lower, upper):
    while True:
        try:
            cellphone = int(input(message))
            if cellphone >= lower and cellphone <= upper:
                break
            else:
                print("ERROR, please enter a valid cellphone number between {} - {}.".format(lower, upper))
        except:
            print("ERROR, please enter a valid cellphone number instead of texts")
    return cellphone

def unique_code_generator(first_name, last_name):
    number = random.randint(1000, 9999)
    number = str(number)
    lname_slice = last_name[0:2]
    user_name = " " + lname_slice + first_name + number
    return user_name.lower()

def new_order(pizza_list):
    pizza_order=[]   #empty list to hold the entire order
    total_cost = 0
    first_name=force_name("Please enter your first name",2,20)
    last_name=force_name("Please enter your last name",2,30)
    code = unique_code_generator(first_name, last_name) #This calls the unique code generator
    """unique_code = code_generator(first_name,last_name) #CALLS UP UNIQUE CODE"""
    pizza_order.append("First name: {}".format(first_name))
    pizza_order.append("Last name: {}".format(last_name))
    pizza_order.append("Booking code: {}.".format(code))
    """pizza_order.append("Unique code {}". format(unique_code))   """
    pick_up=force_number("Type 1 for pickup or 2 for delivery",1,2)
    if pick_up==1:
        pizza_order.append("Pickup")
    if pick_up==2:
        cell_number=force_cellphone("Please enter your cellphone",9,12)
        street_number = str(input("Please enter in your street number"))
        street_name = force_name("Please enter in your street name",2,30)
        suburb = force_name("Please enter in your street suburb",2,15)
        total_cost += 8    #adding on the delivery fee
        pizza_order.append("Cellphone: {}".format(cell_number))
        pizza_order.append("Street number: {}".format(street_number))
        pizza_order.append("Street name: {}".format(street_name))
        pizza_order.append("Suburb: {}".format(suburb))
    #asking which pizza they wish to order
    pizza_number = force_name("Which number pizza would you like to book? (1-12) \n 1:Pepperoni \n 2:Meat",1,12)
    pizza_number = pizza_number*2-2  #this finds the name of the pizza that they want
    quantity = force_number("How many {} pizzas would you like?".format(pizza_list[pizza_number]),1,5)
    total_cost += pizza_list[pizza_number+1]*quantity     #calculates the total cost
    print ("Total cost is $ {}".format(total_cost))       #prints the total price
    pizza_order.append("Pizza: {}".format(pizza_list[pizza_number]))    #adds the pizza name to the order list
    pizza_order.append("Qantity: {}".format(quantity))      #adds the pizza qauntity to the order list
    pizza_order.append("Total cost: ${:.2f}".format(total_cost)) #adds the total price to the order list
    print ("******* Pete's Pizzeria ***********")
    outF = open("orders.txt", "a") #opens the text file
    outF.write("*******Pete's Pizzeria *******")
    for item in pizza_order:    #prints each item on the pizza order list
        outF.write("{}\n.".format(item))
        print(item)
    print("********* Order complete ***********")
    today = date.today() #this calls the function to generate a time stamp
    outF.write("*******Order complete: {} *******. \n".format(today))
    outF.close() #this will close the text file


def pizza_prices(pizza_list):
    print("These are the prices for our cars....")
    count = 0
    while count <len(pizza_list):
        print(int(count/2+1), " ", pizza_list[count], "${:.2f}".format(pizza_list[count + 1]))
        count += 2
    print("*"*20)



def main_menu():
    pizza_list = ["Pepperoni",8.50, "Meat",8.50, "Margherita",8.50, "BBQ chicken",8.50, "Hawaiian",8.50, "Buffalo",8.50, "Cheese",8.50, "Veggie",13.50, "Supreme",13.50, "The works",13.50, "BBQ sausage",13.50, "Beef & onion",13.50,]
    print("Welcome to Pete's Pizzeria")
    while True:
        choice = force_number("Please enter your choice: \n 1 for prices \n 2 for a booking \n 0 TO QUIT",0,2)
        if choice == 1:
            pizza_prices(pizza_list)
        if choice ==2:
            new_order(pizza_list)
        if choice == 0:
            break
    print("********PROGRAM ENDS*********")
    quit() #This quits the program

#the main program
main_menu()

