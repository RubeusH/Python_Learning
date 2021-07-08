#This program solves the following problem

#A project currently underway at Chemical Labs, Inc. requires that a substance be continually heated
#in a vat. A technician must check the substance’s temperature every 15 minutes. If the substance’s
#temperature does not exceed 102.5 degrees Celsius, then the technician does nothing. However, if the
#temperature is greater than 102.5 degrees Celsius, the technician must turn down the vat’s
#thermostat, wait 5 minutes, and check the temperature again. The technician repeats these steps until
#the temperature does not exceed 102.5 degrees Celsius. The director of engineering has asked you to
#write a program that guides the technician through this process.

#First we declare our constants, MAX_TEMPERATURE is the highest temperature the substance can reach before the tech must cool the vat
MAX_TEMP = 102.5

#This loop checks if the temperature is acceptable
substance_temperature = float(input("Please enter the substance's temperature: "))
while substance_temperature > MAX_TEMP:
	print("Please turn down the temperature, wait five minutes, then check the temperature again.")
	substance_temperature = float(input("Please enter the substance's updated temperature: "))
print("The substance is acceptable for the time being, please check again in 15 minutes")
