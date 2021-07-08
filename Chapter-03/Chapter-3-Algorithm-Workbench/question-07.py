#This is a program designed to the specifications below:
#Write an if-else statement that determines whether the points variable is outside the range of
#9 to 51. If the variable’s value is outside this range it should display “Invalid points.”
#otherwise, it should display “Valid points.”

#First we set our point's range as constants
LOWER_BOUND = 9.0
UPPER_BOUND = 51.0

#Then we get the user's points
points = float(input("Please enter your points: "))

#Then we determine if they are valid or not
if points >= LOWER_BOUND and points <= UPPER_BOUND:
	print("Valid points")
else:
	print("Invalid points") 


