'''

This program solves the following problem:

How Much Insurance?
Many financial experts advise that property owners should insure their homes or buildings for at
least 80 percent of the amount it would cost to replace the structure. Write a program that asks
the user to enter the replacement cost of a building, then displays the minimum amount of
insurance he or she should buy for the property.

'''

#constants
MINIMUM_LEVEL = .8

#functions
def get_replacement_cost():
	return float(input("How much would it cost to replace your building? "))
def minimum_insurance(replacement_cost):
	return (replacement_cost * MINIMUM_LEVEL)
def main():
	print("The minimum insurance level is", '$' + format(minimum_insurance(get_replacement_cost()),'.2f'))
main()
