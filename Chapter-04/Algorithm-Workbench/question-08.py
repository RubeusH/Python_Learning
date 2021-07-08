#Write code that prompts the user to enter a positive nonzero number and validates the input.
user_input = float(input("Please enter a positive nonzero number: "))

while user_input <= 0:
	if user_input == 0:
		print("We need a positive NONZERO number! You entered 0 and must try again!")
		user_input = float(input("Please enter a positive nonzero number: "))
	else:
		print("We need a POSITIVE nonzero number! You entered", user_input, "and must try again!")
		user_input = float(input("Please enter a positive nonzero number: "))
