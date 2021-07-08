#This program is for a simple nested loop exercise involving a teacher inputing a student and submitting n marks

#first we get the number of students
num_students = int(input("Enter the number of students"))

for student in range(num_students):
	num_marks = int(input("How many marks are you submitting? "))
	average = 0.0
	for score in range(num_marks):
		average += int(input("Please enter a score: "))
	print("The average of the student is:", average / num_marks)

