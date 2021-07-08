#Write a program that displays a table of the Celsius temperatures 0 through 20 and their
#Fahrenheit equivalents. The formula for converting a temperature from Celsius to Fahrenheit is
#F=(9/5)C+32
#where F is the Fahrenheit temperature, and C is the Celsius temperature. Your program must
#use a loop to display the table.
TEMPERATURE_RANGE = 21
CELSIUS_FACTOR = 9.0/5
CELSIUS_CONSTANT = 32
print("Celsius\t\tFahrenheit")
for temp in range(TEMPERATURE_RANGE):
	fahrenheit = format(CELSIUS_FACTOR * temp + CELSIUS_CONSTANT, '.2f')
	print(temp, "\t\t", fahrenheit)
