#This program solves the following problem

#Write a loop that asks the user to enter a number. The loop should iterate 10 times and keep a
#running total of the numbers entered.
aggregate = 0
for i in range(9):
	user_number = float(input("Please enter a number: "))
	aggregate += user_number
print("The grand total of the numbers you entered is: ", aggregate)	
