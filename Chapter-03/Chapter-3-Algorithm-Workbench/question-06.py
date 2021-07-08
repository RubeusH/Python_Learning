#This program solves the following question:
#"Write an if-else statement that displays 'Speed is normal' if the speed variable is within the
#range of 24 to 56. If the speed variable’s value is outside this range, display 'Speed is
#abnormal' ."

#First we set the bounds as constants to avoid magic numbers
SPEED_LOWER_BOUND = 24.0
SPEED_UPPER_BOUND = 56.0

#Then we ask the user for input
speed = float(input("What is your speed? "))

#Then we decide if it was normal or abnormal
if speed >= SPEED_LOWER_BOUND and speed <= SPEED_UPPER_BOUND:
	print("Speed is normal")
else:
	print("Speed in abnormal")

