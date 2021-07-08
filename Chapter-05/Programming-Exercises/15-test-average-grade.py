'''

This program solves the following problem:

Test Average and Grade
Write a program that asks the user to enter five test scores. The program should display a letter
grade for each score and the average test score. Write the following functions in the program:
calc_average .
This function should accept five test scores as arguments and return the
average of the scores.

determine_grade .
This function should accept a test score as an argument and return a
letter grade for the score based on the following grading scale:
Score Letter Grade
90–100 A
80–89
B
70–79
C
60–69
D
Below 60 F

'''

A = 90
B = 80
C = 70
D = 60

NUM_SCORES = 5
def get_score():
	return float(input("What score did you get? "))
def calc_average(score1, score2, score3, score4, score5):
	return (score1 + score2 + score3 + score4 + score5) / NUM_SCORES
def determine_grade(test_score):
	if test_score >= A:
		grade = 'A'
	elif test_score >= B:
		grade = 'B'
	elif test_score >= C:
		grade = 'C'
	elif test_score >= D:
		grade = 'D'
	else:
		grade = 'F'
	return grade
def main():
	score1 = get_score()
	print(determine_grade(score1))
	score2 = get_score()
	print(determine_grade(score2))
	score3 = get_score()
	print(determine_grade(score3))
	score4 = get_score()
	print(determine_grade(score4))
	score5 = get_score()
	print(determine_grade(score5))
	print("The total average is:", format(calc_average(score1, score2, score3, score4, score5), '.2f'))
main()	
	
