#This program solves the following question:

#Roman Numerals
#Write a program that prompts the user to enter a number within the range of 1 through 10. The
#program should display the Roman numeral version of that number. If the number is outside the
#range of 1 through 10, the program should display an error message.

#First we make the appropriate constants
UPPER = 10
LOWER = 1
I = 1
II = 2
III = 3
IV = 4
V = 5
VI = 6
VII = 7
VIII = 8
IX = 9
X = 10

#Then we get the user input
user_input = float(input("Please enter an integer to convert: "))

#Then we assign it a value if it is in range and return an error message if it isn't
if user_input >= LOWER and user_input <= UPPER:#If the value is in range, assign it the appropriate numeral
	if user_input == I:
		print("I")
	elif user_input == II:
		print("II")
	elif user_input == III:
		print("III")
	elif user_input == IV:
		print("IV")
	elif user_input == V:
		print("V")
	elif user_input == VI:
		print("VI")
	elif user_input == VII:
		print("VII")
	elif user_input == VIII:
		print("VIII")
	elif user_input == IX:
		print("IX")
	else:
		print("X")
else:#else thrown an error
	print("Invalid input")	
