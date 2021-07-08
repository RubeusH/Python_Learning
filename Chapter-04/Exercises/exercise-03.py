#This program solves the following problem:

#Write a program that asks the user to enter the amount that he or she has budgeted for a month.
#A loop should then prompt the user to enter each of his or her expenses for the month and keep
#a running total. When the loop finishes, the program should display the amount that the user is
#over or under budget.

#First we get the user's budget
budget = float(input("What is your budget? "))
#Then we initalize our accumulator variable
expenses = 0.0
expense = 0.0
#Finally we collect the user's expenses
while expense >= 0:
	expense = float(input("Please enter an expense (or a negative number to exit): "))
	if expense >= 0:#if it is a non sentinel input we add it to the expense
		expenses += expense
if expenses < budget:
	print("You are under your budget by: ", budget - expenses)
elif expenses > budget:
	print("You are over your budget by: ", expenses - budget)
else:
	print("You are exactly on budget")
	
