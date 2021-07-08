#This program solves the following problem:

#Write a while loop that lets the user enter a number. The number should be multiplied by 10,
#and the result assigned to a variable named product . The loop should iterate as long as product
#is less than 100.

#First we define our constants
MULTIPLIER = 10.0
UPPER_LIMIT = 100.0
FORBIDDEN_VALUE = 0.0 #All values must be greater than 0

#Then we get the user input
user_number = float(input("Enter the number: "))

#Then we test it to make sure it is greater than zero to avoid an infinite loop
while user_number <= FORBIDDEN_VALUE:
	print("You have entered a forbidden value, please try again")
	user_number = float(input("Enter the number: "))

#Finally we multiply it by ten until its value is over 100
while user_number < UPPER_LIMIT:
	user_number *= MULTIPLIER

