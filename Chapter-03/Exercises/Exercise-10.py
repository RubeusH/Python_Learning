#This program solves the problem below:

#Money Counting Game
#Create a change-counting game that gets the user to enter the number of coins required to make
#exactly one dollar. The program should prompt the user to enter the number of pennies, nickels,
#dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program
#should congratulate the user for winning the game. Otherwise, the program should display a
#message indicating whether the amount entered was more than or less than one dollar.

#First we assign our constants
PENNIES = 1
NICKLES = 5
DIMES = 10
QUARTERS = 25
VICTORY = 100

#Then we get our user data
print("Welcome to the money counting game!")
num_of_pennies = int(input("Please enter the number of pennies: "))
num_of_nickles = int(input("Please enter the number of nickles: "))
num_of_dimes = int(input("Please enter the number of dimes: "))
num_of_quarters = int(input("Please enter the number of quarters: "))

#Then we sum the coins entered
total = num_of_pennies * PENNIES + num_of_nickles * NICKLES + num_of_dimes * DIMES + num_of_quarters * QUARTERS

#Then we decide if they won or not
if total == VICTORY:
	print("Congratulations, you have won the game!")
elif total > VICTORY:
	print("Too many coins, you need 100 but have", total)
else:
	print("Too few coins, you only have", total)
