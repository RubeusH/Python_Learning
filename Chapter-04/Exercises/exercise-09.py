#This program solves the following problems:

#Ocean Levels
#Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
#application that displays the number of millimeters that the ocean will have risen each year for
#the next 25 years.

YEARS = 25
RISING_RATE = 1.6
print("YEAR\tLEVEL OF RISING\n")
for year in range(YEARS):
	print(year + 1,"\t",format(RISING_RATE * (year + 1),'.2f'))
