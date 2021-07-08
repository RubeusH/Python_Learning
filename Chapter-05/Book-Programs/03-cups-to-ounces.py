'''

This program solves the following problem:

Your friend Michael runs a catering company. Some of the ingredients that his recipes require are
measured in cups. When he goes to the grocery store to buy those ingredients, however, they are sold
only by the fluid ounce. He has asked you to write a simple program that converts cups to fluid
ounces.

You design the following algorithm:
1. Display an introductory screen that explains what the program does.
2. Get the number of cups.
3. Convert the number of cups to fluid ounces and display the result.

'''

FLUID_OUNCES = 10
#This is the intro function which displays a brief message explaining what the program does
def intro_message():
	print("Welcome to this silly program. It converts cups to fluid ounces")
def cups_to_ounces(cups):
	fl_ounces = cups * FLUID_OUNCES
	print(cups, "cups is equal to ", fl_ounces, "fluid ounces")
def main():
	intro_message()
	num_cups = float(input("Please enter the number of cups you want "))
	cups_to_ounces(num_cups)
	
main()

