'''
This program solves the following problem:

Sales Tax Program Refactoring
Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that exercise, you were
asked to write a program that calculates and displays the county and state sales tax on a
purchase. If you have already written that program, redesign it so the subtasks are in functions.
If you have not already written that program, write it using functions.

Chapter 2 Exercise 6:

Sales Prediction
A company has determined that its annual profit is typically 23 percent of total sales. Write a
program that asks the user to enter the projected amount of total sales, then displays the profit
that will be made from that amount.
The Sales Prediction Problem
Hint: Use the value 0.23 to represent 23 percent.

'''
#constants
PROFIT_FACTOR = .23
def get_projected_sales():
	return float(input("What is the projected amount of sales? "))
def predict_profit(sales):
	return (sales * PROFIT_FACTOR)
def main():
	print('The projected amount of profit is: ', format(predict_profit(get_projected_sales()), '.2f'))
main()
