#This program solves the following problem:
#Roulette Wheel Colors
#On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as
#follows:
#Pocket 0 is green.
#For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
#pockets are black.
#For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
#pockets are red.
#For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
#pockets are black.
#For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
#pockets are red.
#Write a program that asks the user to enter a pocket number and displays whether the pocket is
#green, red, or black. The program should display an error message if the user enters a number
#that is outside the range of 0 through 36.

#First we define our constants
LOWER = 0
UPPER = 36

#Then we get the roulette number
roulette_number = int(input("Please enter a pocket number here: "))

#Then we determine the validity of the output, rejecting it if invalid and assinging it a color if it is.
if roulette_number < LOWER or roulette_number > UPPER:
	print("This is invalid input")
else:
	if roulette_number == 0:
		print("Green")
	elif roulette_number <= 10:
		if roulette_number % 2 != 0:
			print("Red")
		else:
			print("Black")
	elif roulette_number >= 11 and roulette_number <= 18:
		if roulette_number % 2 != 0:
			print("Black")
		else:
			print("Red")
	elif roulette_number >= 19 and roulette_number <= 28:
		if roulette_number % 2 != 0:
			print("Red")
		else:
			print("Black")
	else:
		if roulette_number % 2 != 0:
			print("Black")
		else:
			print("Red")


