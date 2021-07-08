'''
This program solves the following problem:

Math Quiz
Write a program that gives simple math quizzes. The program should display two random
numbers that are to be added, such as:
  247
+ 129

The program should allow the student to enter the answer. If the answer is correct, a message of
congratulations should be displayed. If the answer is incorrect, a message showing the correct
answer should be displayed.

'''
import random

MAX = 999
MIN = 100
def generate_first_summand():
	return random.randint(MIN, MAX)
def generate_second_summand():
	return random.randint(MIN, MAX)
def display_problem(rand1, rand2):
	print("What is", rand1, "+", rand2)
def get_answer():
	return float(input("Your answer: "))
def display(answer, summand1, summand2):
	if answer == summand1 + summand2:
		print("Congrats, you got the right answer!")
	else:
		print("Sorry, but you are retarded. The correct answer is:", summand1 + summand2)
def main():
	summand1 = generate_first_summand()
	summand2 = generate_second_summand()
	display_problem(summand1, summand2)
	user_answer = get_answer()
	display(user_answer, summand1, summand2)
main()
