#This program solves the following problem:

#Calculating the Factorial of a Number
#In mathematics, the notation n! represents the factorial of the nonnegative integer n. The
#factorial of n is the product of all the nonnegative integers from 1 to n. For example,
#7!=1×2×3×4×5×6×7=5,040
#and
#4!=1×2×3×4=24
#Write a program that lets the user enter a nonnegative integer then uses a loop to calculate the
#factorial of that number. Display the factorial.

#first we declare our constants
ZERO_CASE = 0#for when the input is zero we handle it with this special case of directly outputing 1
ZERO_CASE_RESULT = 1#What we output in the zero case
FACTORIAL_FACTOR = 1#What we increment our loop by in the non-zero case
MIN_VALUE = 1#End value for the non-zero loop case

#Then we get the number the user wants to perform the factorial operation on
factorial = int(input("Please enter a number to have the factorial operation executed on it: "))

#Then we execute the operation
if factorial == ZERO_CASE:#if the input is zero, we handle this case specially and output 1 (The value of ZERO_CASE_RESULT)
	print(ZERO_CASE_RESULT)
else:#else we use our loop to compute factorial
	index = factorial
	while index  > MIN_VALUE:
		factorial = factorial * (index - 1)
		index -= 1
	print(factorial)
