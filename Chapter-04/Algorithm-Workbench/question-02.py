#This program solves the following problem

#Write a while loop that asks the user to enter two numbers. The numbers should be added and
#the sum displayed. The loop should ask the user if he or she wishes to perform the operation
#again. If so, the loop should repeat, otherwise it should terminate.

perform_loop = "yes"

while perform_loop == "yes":
	summand1 = float(input("Enter the first number here: "))
	summand2 = float(input("Enter the second number here: "))
	result = summand1 + summand2
	print("The sum of these two numbers is:", result)
	perform_loop = input("Would you like to enter more numbers (yes/no): ")
	while (perform_loop != "yes" and perform_loop != "no"):
		print("We need yes or no in that way specifically")
		perform_loop = input("Would you like to enter more numbers (yes/no): ")
