'''

This program solves the following problem:

Write a function named times_ten . The function should accept an argument and display the
product of its argument multiplied times 10.

'''

#constants
FACTOR = 10

#function
def times_ten(number):
	print(number * FACTOR)
def main():
	user_input = float(input("Please enter a number to multiplied by ten: "))
	times_ten(user_input)
main()
