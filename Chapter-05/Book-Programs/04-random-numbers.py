'''

This program solves the following problem:

Dr. Kimura teaches an introductory statistics class and has asked you to write a program that he can
use in class to simulate the rolling of dice. The program should randomly generate two numbers in
the range of 1 through 6 and display them. In your interview with Dr. Kimura, you learn that he
would like to use the program to simulate several rolls of the dice, one after the other. Here is the
pseudocode for the program:
While the user wants to roll the dice:
Display a random number in the range of 1 through 6
Display another random number in the range of 1 through 6
Ask the user if he or she wants to roll the dice again
You will write a while loop that simulates one roll of the dice and then asks the user if another roll
should be performed. As long as the user answers “y” for yes, the loop will repeat.

'''

#the random module is essential for simulating dice rolls
import random

#We define the upper and lower limits described the problem 
LOWER = 1
UPPER = 6

#This is the number of cases from the problem description
CASES = 2

#This function prints 'number_of_digits' random digits between lower and upper inclusive
def rand_numbers(lower, upper, number_of_digits):
	for i in range(number_of_digits):
		print(random.randint(lower, upper))

#here we display the two random numbers
rand_numbers(LOWER, UPPER, CASES)
roll_again = input("Would you like to roll again? (y/n) ")
while roll_again == "y":
	number_of_digits = int(input("How many random digits would you like to generate? "))
	rand_numbers(LOWER, UPPER, number_of_digits)
	roll_again = input("Would you like to roll again? (y/n) ")
