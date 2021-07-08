#This program solves the following problem:

#Write code that prompts the user to enter a number in the range of 1 through 100 and validates
#the input.

user_input = float(input("Please enter a number in the range of 1 to 100 inclusive: "))

while user_input < 1 or user_input > 100:
	print("The number is out the range, please try again!")
	user_input = float(input("Please enter a number in the range of 1 to 100 inclusive: "))
