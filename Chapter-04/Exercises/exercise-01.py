#This program solves the following problem:

#The Bug Collector Problem
#A bug collector collects bugs every day for five days. Write a program that keeps a running total
#of the number of bugs collected during the five days. The loop should ask for the number of
#bugs collected for each day, and when the loop is finished, the program should display the total
#number of bugs collected.

#first we declare our constants
DAYS = 5

#Then we initialize our accumulator variable
bugs_caught = 0

#Then we ask the collector for his daily catch
for day in range(DAYS):
	bugs_caught += int(input("How many bugs did you catch on day " + str(day + 1) + "? "))
print("The total number of bugs caught is:", bugs_caught)
