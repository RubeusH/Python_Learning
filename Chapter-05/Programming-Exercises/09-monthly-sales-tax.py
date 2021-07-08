'''

This program solves the following problem:

Monthly Sales Tax

A retail company must file a monthly sales tax report listing the total sales for the month, and
the amount of state and county sales tax collected. The state sales tax rate is 5 percent and the
county sales tax rate is 2.5 percent. Write a program that asks the user to enter the total sales for
the month. From this figure, the application should calculate and display the following:
The amount of county sales tax
The amount of state sales tax
The total sales tax (county plus state)

'''
#constants
STATE_TAX_RATE = .05
COUNTY_TAX_RATE = .025
#sales
def get_monthly_sales():
	return float(input("What are the monthly sales? "))
#taxes
def county_tax(sales):
	return COUNTY_TAX_RATE * sales
def state_tax(sales):
	return STATE_TAX_RATE * sales
def total_tax(county_taxes, state_taxes):
	return county_taxes + state_taxes
#display
def display_taxes(county, state, total):
	print("\nTotal taxes: $" + format(total, '.2f'))
	print("\tState taxes: $" + format(state, '.2f'))
	print("\tCounty taxes: $"+ format(county, '.2f'))
def main():
	monthly_sales = get_monthly_sales()
	county_taxes = county_tax(monthly_sales)
	state_taxes = state_tax(monthly_sales)
	display_taxes(county_taxes, state_taxes, total_tax(county_taxes, state_taxes))
main()
