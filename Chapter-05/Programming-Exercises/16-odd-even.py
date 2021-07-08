'''

This program solves the following problem:

Odd/Even Counter
In this chapter, you saw an example of how to write an algorithm that determines whether a
number is even or odd. Write a program that generates 100 random numbers and keeps a count
of how many of those random numbers are even, and how many of them are odd.

'''
#constants
TRIALS = 100

import random
def is_even(num):	
	if num % 2 == 0:
		eveness = True
	else:
		eveness = False
	return eveness
def main():
	odd = 0
	even = 0
	for trial in range(TRIALS):
		if is_even(random.randint(1, TRIALS)):
			even += 1
		else:
			odd += 1
	print(even, "numbers are even")
	print(odd, "numbers are odd")

main()
