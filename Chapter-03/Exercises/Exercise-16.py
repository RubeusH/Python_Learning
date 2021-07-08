#This program solves the following problem:

#The month of February normally has 28 days. But if it is a leap year, February has 29 days.
#Write a program that asks the user to enter a year. The program should then display the number
#of days in February that year. Use the following criteria to identify leap years:
#1. Determine whether the year is divisible by 100. If it is, then it is a leap year if and only if it
#is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
#2. If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4. For
#example, 2008 is a leap year, but 2009 is not.

#Here we declare our constants
TEST1 = 100
SUBTEST1 = 400
TEST2 = 4
DIVIDES = 0

#Gets user input
year = int(input("Enter a year here: "))

#Test the year
if year % TEST1 == DIVIDES:
	if year % TEST2 == DIVIDES:
		print(year, "was a leap year")
	else:
		print(year, "was not a leap year")
else:
	if year % TEST2 == DIVIDES:
		print(year, "was a leap year")
	else:
		print(year, "was not a leap year")
