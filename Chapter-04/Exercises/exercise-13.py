#This program solves the following problem

#Population
#Write a program that predicts the approximate size of a population of organisms. The
#application should use text boxes to allow the user to enter the starting number of organisms,
#the average daily population increase (as a percentage), and the number of days the organisms
#will be left to multiply. For example, assume the user enters the following values:
#Starting number of organisms: 2
#Average daily increase: 30%
#Number of days to multiply: 10

#First we get the information from our user
starting_number = int(input("How many organisms do we start out with? "))
percent_growth = float(input("What percentage of growth do they show per day? "))
duration = int(input("How many days does the population have to grow? "))

#Then we make some space for separation between the prompt and the table
print("\n\n\n\n\n")

#Then we print the header
print("Day\tApproximate Population")

#Then we compute our values and display them
day_population = starting_number
for day in range(duration):
	print(str(day + 1) + '\t\t' + str(day_population))
	day_population = day_population + day_population * (percent_growth / 100)
