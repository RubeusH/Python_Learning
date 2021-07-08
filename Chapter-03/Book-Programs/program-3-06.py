#A program to determine the user's grade

#Here we set the points needed for the grade
A = 90.0
B = 80.0
C = 70.0
D = 60.0

#Then we get the user's score
user_score = float(input("Please enter your score "))

#Then we determine the grade
if user_score >= A:
	print("You have received the grade of A")
else:
	if user_score >= B:
		print("You have received the grade of B")
	else:
		if user_score >= C:
			print("You have received the grade of C")
		else:
			if user_score >= D:
				print("You have received the grade of D")
			else:
				print("You are gay!")
