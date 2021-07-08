#This program solves the problem below:

#Calories Burned
#Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a
#loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

#First we declare our constants
CALS_PER_MINUTE = 4.2
START = 10 #We start by displaying calories burned at ten minutes
STOP = 35 #We end by displaying calories burned at 30 minutes
STEP = 5 #Between the two we display calories burned in five minute intervals
#Then we display the values
for minute in range(START,STOP,STEP):
	calories_burned = minute * CALS_PER_MINUTE
	print("The number of calories burned after", minute, "minutes is:", calories_burned) 
