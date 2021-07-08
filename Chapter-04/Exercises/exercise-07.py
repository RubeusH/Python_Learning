#This program solves the following problem

#Pennies for Pay
#Write a program that calculates the amount of money a person would earn over a period of time
#if his or her salary is one penny the first day, two pennies the second day, and continues to
#double each day. The program should ask the user for the number of days. Display a table
#showing what the salary was for each day, then show the total pay at the end of the period. The
#output should be displayed in a dollar amount, not the number of pennies.

#Define our constants
PENNIES_IN_DOLLAR = 100
SALARY_FACTOR = 2.0
#Then we get the number of days the salary will be collected for
job_duration = int(input("How many days will you do this job for? "))

#Then we compute the salary
salary = 1
total_salary = 0
for day in range(job_duration):
	print("For day", day + 1, "the salary is $" + str(salary / PENNIES_IN_DOLLAR))
	total_salary += salary
	salary *= SALARY_FACTOR
print("Your total earnings over this period is: $" + str(total_salary / PENNIES_IN_DOLLAR))
