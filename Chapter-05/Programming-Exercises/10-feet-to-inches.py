'''

This program solves the following problem:


The Feet to Inches Problem:

One foot equals 12 inches. Write a function named feet_to_inches that accepts a number of
feet as an argument and returns the number of inches in that many feet. Use the function in a
program that prompts the user to enter a number of feet then displays the number of inches in
that many feet.

'''
INCHES = 12
def get_feet():
	return float(input("Enter a distance in feet: "))
def convert_to_inches(feet):
	return feet * INCHES
def display(feet, inches):
	print(feet, "feet is", inches, "inches")
def main():
	feet = get_feet()
	inches = convert_to_inches(feet)
	display(feet, inches)
main()
