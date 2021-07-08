'''

This program solves the following problem:

Prime Numbers

A prime number is a number that is only evenly divisible by itself and 1. For example, the
number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however, is
not prime because it can be divided evenly by 1, 2, 3, and 6.
Write a Boolean function named is_prime which takes an integer as an argument and returns
true if the argument is a prime number, or false otherwise. Use the function in a program that
prompts the user to enter a number then displays a message indicating whether the number is
prime.

'''

def is_prime(num):
	isPrime = True
	trial = 2
	while trial < num:
		#print("The statement tests if", num, "is divisible by", trial)
		if num % trial == 0:
			#print("We find that", num, "is divisible by" trial)
			isPrime = False
			trial = num
		trial += 1
	return isPrime
def get_input():
	return int(input("Please enter an integer here: "))
def main():
	prime = get_input()
	if is_prime(prime):
		print(prime, "is prime")
	else:
		print(prime, "is not prime")
main()
