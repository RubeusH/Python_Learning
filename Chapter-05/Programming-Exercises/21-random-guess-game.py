'''

This program solves the following question:

Random Number Guessing Game

Write a program that generates a random number in the range of 1 through 100, and asks the
user to guess what the number is. If the user’s guess is higher than the random number, the
program should display “Too high, try again.” If the user’s guess is lower than the random
number, the program should display “Too low, try again.” If the user guesses the number, the
application should congratulate the user and generate a new random number so the game can
start over.

Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the
user makes. When the user correctly guesses the random number, the program should display
the number of guesses.

'''

import random

#constants
INCREMENT = 1

LOWER_BOUND = 1
UPPER_BOUND = 100

def generate_number():
	return random.randint(LOWER_BOUND, UPPER_BOUND)
def get_guess():
	return int(input("Guess what the number is: "))
def is_correct(guess, answer):
	if guess == answer:
		isCorrect = True
	else:
		isCorrect = False
	return isCorrect
def print_congratulations(guesses):
	print("\n\n\nCongratulations, you guessed the right number!")
	print("You got the right answer in", guesses, "guesses")
def print_consolement(guess, answer):
	#print("Sorry, you guessed the wrong number. Please try again")
	if guess > answer:
		print("Too high!")
	else:
		print("Too low!")
def main():
	answer = generate_number()
	guess = get_guess()
	number_of_guesses = 1
	while is_correct(guess, answer) != True:
		print_consolement(guess, answer)
		guess = get_guess()
		number_of_guesses += INCREMENT
	print_congratulations(number_of_guesses)
main()
