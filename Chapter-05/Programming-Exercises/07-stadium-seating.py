'''

This program solves the following problem:

There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15,
and Class C seats cost $10. Write a program that asks how many tickets for each class of seats
were sold, then displays the amount of income generated from ticket sales.

'''

#constants
CLASS_A = 20
CLASS_B = 15
CLASS_C = 10

#functions
def class_a():
	return int(input("How many class A sales? "))
def class_b():
	return int(input("How many class B sales? "))
def class_c():
	return int(input("How many class C sales? "))
def ticket_sales():
	sales = class_a() * CLASS_A + class_b() * CLASS_B + class_c() * CLASS_C
	print("\nThe total sales is: $" + format(sales, '.2f'))
ticket_sales()
