#This program determines if the user qualifies for a loan

#Here we set the minimum salary and years needed for the loan
salary_min = 30000.0
exp_min = 2.0
#Then we ask for the user's salary
salary =float(input("Please enter your salary: "))
#Then we determine if they have the salary and experience to qualify for the program
if salary >= salary_min:
	exp = float(input("How many years of experience do you have? "))
	if exp >= exp_min:
		print("You qualify for the loan!")
	else:
		print("You lack the experience for the loan")
else:
	print("You lack the salary to qualify for the loan :(") 
