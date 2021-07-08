#This program solves the following problem:

#The county tax office calculates the annual taxes on property using the following formula:
#property tax=property value × 0.0065
#Every day, a clerk in the tax office gets a list of properties and has to calculate the tax for each
#property on the list. You have been asked to design a program that the clerk can use to perform these
#calculations.
#In your interview with the tax clerk, you learn that each property is assigned a lot number, and all lot
#numbers are 1 or greater. You decide to write a loop that uses the number 0 as a sentinel value.
#During each loop iteration, the program will ask the clerk to enter either a property’s lot number, or 0
#to end.

#Constants

TAX_MULTIPLIER = .0065 #Constant in the formula
END = 0 #Sentinel value

#Main body
lot_number = int(input("Please enter the lot number or 0 to end the program: "))

while lot_number != END:
	property_value = float(input("Please enter the value of lot" + " " + str(lot_number) + ": "))
	property_tax = TAX_MULTIPLIER * property_value
	print("The property tax associated with lot", lot_number, "is: $" + format(property_tax, '.2f'))
	lot_number = int(input("Please enter the lot number or 0 to end the program: "))
