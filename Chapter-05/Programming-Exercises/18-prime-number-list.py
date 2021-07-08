'''

This program solves the following problem:

Prime Number List
This exercise assumes that you have already written the is_prime function in Programming
Exercise 17. Write another program that displays all of the prime numbers from 1 to 100. The
program should have a loop that calls the is_prime function.

'''
#constants
START = 1
END = 100

INCREMENT = 1
def is_prime(num):
	trials = 2
	isPrime = True
	while trials <= num:
		if num % trials == 0:
			isPrime = False
		trials += INCREMENT
	return isPrime
			
display()
	num = START
	while num <= END:
		if is_prime(num):
			print(num)
		num += INCREMENT
def main():
	display()
	
