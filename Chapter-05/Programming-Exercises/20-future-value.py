'''

This program solves the following problem:

Future Value:

Suppose you have a certain amount of money in a savings account that earns compound
monthly interest, and you want to calculate the amount that you will have after a specific
number of months. The formula is as follows:

F=P×(1+i)t

The terms in the formula are:

F is the future value of the account after the specified time period.
P is the present value of the account.
i is the monthly interest rate.
t is the number of months.

Write a program that prompts the user to enter the account’s present value, monthly interest
rate, and the number of months that the money will be left in the account. The program should
pass these values to a function that returns the future value of the account, after the specified
number of months. The program should display the account’s future value.

'''
INTEREST_FACTOR = 1
INTEREST_QUOTIENT = 100.0

def get_present_value():
	return float(input("What is the present value of the account? "))
def get_interest():
	return float(input("What is the interest rate on the account? "))
def get_duration():
	return float(input("How many months will the money remain in the account? "))
def future_value(present_value, interest, duration):
	#print("We multiply", present_value, "by (", INTEREST_FACTOR, "plus", interest/INTEREST_QUOTIENT, ") to the power of ", duration) 
	#print("And we compute: ", present_value * ((INTEREST_FACTOR + interest/INTEREST_QUOTIENT) ** duration))
	#print("We comput brackets to the power of duration and get", (INTEREST_FACTOR + interest/INTEREST_QUOTIENT) ** duration)
	return present_value * ((INTEREST_FACTOR + interest/INTEREST_QUOTIENT) ** duration)
def display_future_value(future_value):
	print("The future value of the account is: $" + format(future_value, '.2f'))
def main():
	display_future_value(future_value(get_present_value(), get_interest(), get_duration()))
main()
