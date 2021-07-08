#Day of the Week
#Write a program that asks the user for a number in the range of 1 through 7. The program
#should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 =
#Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should
#display an error message if the user enters a number that is outside the range of 1 through 7.

#First we map each number in range to a day of the week
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

#Then we get input
user_input = float(input("Enter an integer between 1 and 7: "))

#Then we test if it is in range
if user_input >= MONDAY and user_input <= SUNDAY:#if in range assign to appropriate day
	if user_input == MONDAY:
		print("Monday")
	elif user_input == TUESDAY:
		print("Tuesday")
	elif user_input == WEDNESDAY:
		print("Wednesday")
	elif user_input == THURSDAY:
		print("Thursday")
	elif user_input == FRIDAY:
		print("Friday")
	elif user_input == SATURDAY:
		print("Saturday")
	else:
		print("Sunday")	
else:#if not in range print error message
	print("Invalid input")
