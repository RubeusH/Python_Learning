#This program solves the following question

#Average Rainfall
#Write a program that uses nested loops to collect data and calculate the average rainfall over a
#period of years. The program should first ask for the number of years. The outer loop will
#iterate once for each year. The inner loop will iterate twelve times, once for each month. Each
#iteration of the inner loop will ask the user for the inches of rainfall for that month. After all
#iterations, the program should display the number of months, the total inches of rainfall, and the
#average rainfall per month for the entire period.

#First we define our constants
MONTHS = 12

#Then we ask the user how many years they want to average
years = int(input("How many years do you want to enter data for? "))

#Then we initialize our accumulator variable
sigma = 0.0
#Then we compute the average
for year in range(years):
	print("For year", year + 1, ":")
	for month in range(MONTHS):
		sigma += float(input("What was the total rainfall (inches) in month " + str(month + 1) + "? "))#gets user input on rainfall per month
total = MONTHS * years #Total number of months
#Finally we print the header and data
#We print the header and data
print("\nMONTH\tTOTAL\tAVERAGE")
print(MONTHS * years, "\t", sigma, "\t", sigma / total) #displays number of months, total rainfall and average rainfall 	
