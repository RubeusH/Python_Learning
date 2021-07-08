'''

This program solves the following problem:

Hal owns a business named Make Your Own Music, which sells guitars, drums, banjos, synthesizers,
and many other musical instruments. Hal’s sales staff works strictly on commission. At the end of
the month, each salesperson’s commission is calculated according to Table 5-1.

Table 5-1 Sales commission rates
Sales This Month Commission Rate
Less than $10,000 10%
$10,000–14,999 12%
$15,000–17,999 14%
$18,000–21,999 16%
$22,000 or more 18%

For example, a salesperson with $16,000 in monthly sales will earn a 14 percent commission
($2,240). Another salesperson with $18,000 in monthly sales will earn a 16 percent commission
($2,880). A person with $30,000 in sales will earn an 18 percent commission ($5,400).
Because the staff gets paid once per month, Hal allows each employee to take up to $2,000 per
month in advance. When sales commissions are calculated, the amount of each employee’s advanced
pay is subtracted from the commission. If any salesperson’s commissions are less than the amount of
their advance, they must reimburse Hal for the difference. To calculate a salesperson’s monthly pay,
Hal uses the following formula:

pay = sales × commission rate − advanced pay

Hal has asked you to write a program that makes this calculation for him. The following general
algorithm outlines the steps the program must take.

1. Get the salesperson's monthly sales.
2. Get the amount of advanced pay.
3. Use the amount of monthly sales to determine the commission rate.
4. Calculate the salesperson's pay using the formula previously shown. If the amount is negative,
indicate that the salesperson must reimburse the company. 

'''
#constants
COMMISSION_1 = .1
COMMISSION_2 = .12
COMMISSION_3 = .14
COMMISSION_4 = .16
COMMISSION_5 = .18

SALES_LEVEL_1 = 10000
SALES_LEVEL_2 = 15000
SALES_LEVEL_3 = 18000
SALES_LEVEL_4 = 22000


def monthly_sales():
	return float(input("How many dollars in sales did you make this month? "))
def advanced_pay():
	return float(input("How much pay was advanced to you this month? "))
def commission_rate(monthly_sales):
	if monthly_sales < SALES_LEVEL_1:
		commission = COMMISSION_1
	elif monthly_sales < SALES_LEVEL_2:
		commission = COMMISSION_2
	elif monthly_sales < SALES_LEVEL_3:
		commission = COMMISSION_3
	elif monthly_sales < SALES_LEVEL_4:
		commission = COMMISSION_4
	else:
		commission = COMMISSION_5
	return commission
def final_pay(sales, commission_rate, advanced_pay):
	return sales * commission_rate - advanced_pay
def main():
	sales = monthly_sales()
	advance_pay = advanced_pay()
	rate = commission_rate(sales)
	print("Your final pay is:", final_pay(sales, rate, advance_pay))
main()
