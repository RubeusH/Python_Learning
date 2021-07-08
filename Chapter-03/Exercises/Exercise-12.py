#This program solves the problem below:

#Software Sales
#A software company sells a package that retails for $99. Quantity discounts are given according
#to the following table:
#Quantity Discount
#10–19
#10%
#20–49
#20%
#50–99
#30%
#100 or more 40%
#Write a program that asks the user to enter the number of packages purchased. The program
#should then display the amount of the discount (if any) and the total amount of the purchase
#after the discount.

#First we define our constants
#These four are the thresholds for the discount
DISCOUNT_THRESH1 = 10
DISCOUNT_THRESH2 = 20
DISCOUNT_THRESH3= 50
DISCOUNT_THRESH4 = 100
#These are the discounts
DISCOUNT1 = .10
DISCOUNT2 = .20
DISCOUNT3 = .30
DISCOUNT4 = .40
#Finally the price
PRICE = 99.0

#Then we get the input
quantity = int(input("How many computers are you buying? "))

#Then we evaluate the quantity for a discount
if quantity < DISCOUNT_THRESH1:
	print("You did not order enough to qualify for a discount")
	print("Your bill is:", '$' +  format(quantity*PRICE, '.2f'))
elif quantity < DISCOUNT_THRESH2:
	print("You receive a 10% discount")
	print("After applying the discount, your bill is:", '$' +  format(quantity * PRICE * DISCOUNT1, '.2f'))
elif quantity < DISCOUNT_THRESH3:
	print("You receive a 20% discount")
	print("After applying the discount, your bill is:", '$' + format(quantity * PRICE * DISCOUNT2, '.2f'))
elif quantity < DISCOUNT_THRESH4:
	print("You receive a 30% discount")
	print("After applying the discount, your bill is:", '$' + format(quantity * PRICE * DISCOUNT3, '.2f'))
else:
	print("You receive the maximum 40% discount")
	print("After applying the discount, your bill is:", '$' + format(quantity * PRICE * DISCOUNT4, '.2f'))

