'''

Rock, Paper, Scissors Game

Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.

The program should work as follows:

1. When the program begins, a random number in the range of 1 through 3 is generated. If the
number is 1, then the computer has chosen rock. If the number is 2, then the computer has
chosen paper. If the number is 3, then the computer has chosen scissors. (Don’t display the
computer’s choice yet.)

2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.

3. The computer’s choice is displayed.

4. A winner is selected according to the following rules:

If one player chooses rock and the other player chooses scissors, then rock wins.
(Rock smashes scissors.)
If one player chooses scissors and the other player chooses paper, then scissors wins.
(Scissors cuts paper.)
If one player chooses paper and the other player chooses rock, then paper wins. (Paper
wraps rock.)
If both players make the same choice, the game must be played again to determine the
winner.

'''
import random

#constants
ROCK = 1
PAPER = 2
SCISSORS = 3

COMPUTER_WIN = 2
USER_WIN = 1
DRAW = 0

def assign_computer_weapon():
	return random.randint(1,3)
def get_user_weapon():
	return int(input("Please make a choice (1 = rock 2 = paper 3 = scissors): "))
def number_to_weapon(number):
	if number == ROCK:
		weapon = 'Rock'
	elif number == PAPER:
		weapon = 'Paper'
	else:
		weapon = 'Scissors'
	return weapon
def display_computer_weapon(weapon):
	print("The computer used:", weapon)
def display_computer_victory():
	print("The computer wins!")
def display_user_victory():
	print("The user wins!")
def display_draw():
	print("A draw!\nWe play again!")
def determine_winner(user_weapon, computer_weapon):
	if user_weapon == ROCK:
		if computer_weapon == SCISSORS:
			result = USER_WIN
		elif computer_weapon == PAPER:
			result = COMPUTER_WIN
		else:
			result = DRAW
	elif user_weapon == PAPER:
		if computer_weapon == ROCK:
			result = USER_WIN
		elif computer_weapon == PAPER:
			result = DRAW
		else:
			result = COMPUTER_WIN
	else:
		if computer_weapon == ROCK:
			result = COMPUTER_WIN
		elif computer_weapon == PAPER:
			result = USER_WIN
		else:
			result = DRAW
	return result
def display_result(result):
	if result == DRAW:
		display_draw()
	elif result == USER_WIN:
		display_user_victory()
	else:
		display_computer_victory()
def main():
	result = DRAW
	while result == DRAW:
		computer_weapon = assign_computer_weapon()
		user_weapon = get_user_weapon()
		display_computer_weapon(number_to_weapon(computer_weapon))
		result = determine_winner(user_weapon, computer_weapon)
		display_result(result)
main()
