#This program solves the following problem:

#Sum of Numbers
#Write a program with a loop that asks the user to enter a series of positive numbers. The user
#should enter a negative number to signal the end of the series. After all the positive numbers
#have been entered, the program should display their sum.

MINIMUM_VALUE = 0

positive_number = int(input("Please enter a positive integer to add (or a negative to terminate the program): "))
summation = 0
while positive_number >= MINIMUM_VALUE:
	summation += positive_number
	positive_number = int(input("Please enter a positive integer to add (or a negative to terminate the program): "))
print("\nThe final sum is: ", summation)
