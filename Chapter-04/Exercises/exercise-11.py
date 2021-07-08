#This program solves the following problem:

#Weight Loss
#If a moderately active person cuts their calorie intake by 500 calories a day, they can typically
#lose about 4 pounds a month. Write a program that lets the user enter their starting weight, then
#creates and displays a table showing what their expected weight will be at the end of each
#month for the next 6 months if they stay on this diet.

#First we declare the constants
CALORIE_RESTRICTION = 500 #This is the caloric restriction detailed in the problem description
WEIGHT_LOSS = 4#This is the weight loss per month associated with a 500 calorie deficit.
DIET_DURATION = 6
#Then we get the user's starting weight
initial_weight = float(input("Please enter your weight in pounds: "))

#Then we display the table of values 
print("Month\tWeight\tWeight Loss")
for month in range(DIET_DURATION):
	weight_lost = WEIGHT_LOSS * (month + 1)
	print(month + 1, '\t', initial_weight - weight_lost, '\t', weight_lost)


