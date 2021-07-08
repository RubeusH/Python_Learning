'''

Maximum of Two Values
Write a function named max that accepts two integer values as arguments and returns the value
that is the greater of the two. For example, if 7 and 12 are passed as arguments to the function,
the function should return 12. Use the function in a program that prompts the user to enter two
integer values. The program should display the value that is the greater of the two.

'''

def max(val1, val2):
	if val1 > val2:
		max_val = val1
	elif val2 > val1:
		max_val = val2
	else:
		max_val = val1
	return max_val
def get_val1():
	return int(input("Enter the first integer here: "))
def get_val2():
	return int(input("Enter the second integer here: "))
def display_max(val1, val2):
	print("The larger of", val1, "and", val2, "is",  max(val1, val2))
def main():
	display_max(get_val1(), get_val2())
main()
