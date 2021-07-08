#This program solves the following problem

#Tuition Increase
#At one college, the tuition for a full-time student is $8,000 per semester. It has been announced
#that the tuition will increase by 3 percent each year for the next 5 years. Write a program with a
#loop that displays the projected semester tuition amount for the next 5 years.

#Here we declaire our constants and variables
TUITION_FACTOR = .03#Prediction of how high tuition will be
YEARS = 5#Number of years the program is expected to execute for

tuition = 8000#Initial tuition given in problem description

#Then we display the tuition
print("YEAR\tTUITION\n")#prints the header
for year in range(YEARS):
	print(year + 1, "\t", tuition)#prints the year and the tuition expected for that year
	tuition = tuition + tuition * TUITION_FACTOR#updates the tuition for the next year
