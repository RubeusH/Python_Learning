#This program solves the following problem

#The Fast Freight Shipping Company charges the following rates:
#Weight of Package
#Rate per Pound
#2 pounds or less
#$1.50
#Over 2 pounds but not more than 6 pounds $3.00
#Over 6 pounds but not more than 10 pounds $4.00
#Over 10 pounds
#$4.75
#Write a program that asks the user to enter the weight of a package then displays the shipping
#charges.

#First we declare our constants
#thresholds
THRESHOLD1 = 2
THRESHOLD2 = 6
THRESHOLD3 = 10

#Then we get the necessary input
weight = float(input("How much does your package weigh (lbs)? "))

#Then we evaluate it
if weight <= THRESHOLD1:
	print("Your rate is $1.50")
elif weight <= THRESHOLD2:
	print("Your rate is $3.00")
elif weight <= THRESHOLD3:
	print("Your rate is $4.00")
else:
	print("Your rate is $4.75")
 
