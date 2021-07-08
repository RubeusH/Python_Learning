'''

Paint Job Estimator

A painting company has determined that for every 112 square feet of wall space, one gallon of
paint and eight hours of labor will be required. The company charges $35.00 per hour for labor.
Write a program that asks the user to enter the square feet of wall space to be painted and the
price of the paint per gallon. The program should display the following data:
The number of gallons of paint required
The hours of labor required
The cost of the paint
The labor charges
The total cost of the paint job

'''
import math

#constants
WALL_SPACE = 112
LABOR = 8
RATE = 35

#functions
#These two functions get user data
def get_space():
	return float(input("How much space in square feet will be painted? "))
def get_price():
	return float(input("What is the price of paint per gallon? "))
#These two functions computer how much paint and labor is used
def paint_used(space):
	return math.ceil(space / WALL_SPACE)
def labor_used(space):
	return LABOR * math.ceil(space / WALL_SPACE)
#These three functions compute cost
def paint_cost(price_of_paint, paint_used):
	return price_of_paint * paint_used
def labor_cost(labor_used):
	return labor_used * RATE
def total_cost(paint_cost, labor_cost):
	return paint_cost + labor_cost
def display(gallons_used, labor, paint_cost, labor_cost, total_cost):
	print("\nThe amount of paint used is:", gallons_used)
	print("\nThe hours of labor is:", labor)
	print("\nThe cost of the paint is: $" + format(paint_cost, '.2f'))
	print("\nThe cost of labor is: $" + format(labor_cost, '.2f'))
	print("\nThe total cost of the project is: $" + format(total_cost, '.2f'))
def main():
	area_painted = get_space()
	price_per_gallon = get_price()	
	hours_of_labor = labor_used(area_painted)
	gallons_of_paint = paint_used(area_painted)
	cost_of_paint = paint_cost(price_per_gallon, paint_used(area_painted))
	cost_of_labor = labor_cost(hours_of_labor)
	display(gallons_of_paint, hours_of_labor, cost_of_paint, cost_of_labor, total_cost(cost_of_paint, cost_of_labor))
main()
