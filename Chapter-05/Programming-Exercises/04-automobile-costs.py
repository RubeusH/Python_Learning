'''
This program solves the following problem:

Automobile Costs

Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses, and the
total annual cost of these expenses.

'''
#CONSTANTS
YEARS = 12

#FUNCTIONS
def loan_payment():
	return float(input("How much are you paying per month in loan costs? "))
def insurance():
	return float(input("How much do you pay per month in insurance? "))
def gas():
	return float(input("How much do you spend per month in gas? "))
def oil():
	return float(input("How much do you spend per month in oil "))
def tires():
	return float(input("How much do you spend per month in tires "))
def maintenance():
	return float(input("How much do you spend per month in maintenance "))
def display_monthly_costs(loan, insurance, gas, oil, tires, maintenance):
	print("The total monthly costs of this car are: $" + format(loan + insurance + gas + oil + tires + maintenance,'.2f'))
def display_annual_costs(loan, insurance, gas, oil, tires, maintenance):
	print("The total yearly costs of this car are: $" + format(YEARS * (loan + insurance + gas + oil + tires + maintenance),'.2f'))
def display_costs(loan, insurance, gas, oil, tires, maintenance):
	display_monthly_costs(loan, insurance, gas, oil, tires, maintenance)
	display_annual_costs(loan, insurance, gas, oil, tires, maintenance)
def main():
	display_costs(loan_payment(), insurance(), gas(), oil(), tires(), maintenance())
main()
	
