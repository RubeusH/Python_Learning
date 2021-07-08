def summation(a, b):
	result = a + b
	return result
def get_first_summand():
	first_summand = float(input("Please enter the first number you want to add here: "))
	return first_summand
def get_second_summand():
	second_summand = float(input("Please enter the second number you want to add here: "))
	return second_summand
def main():
	summand1 = get_first_summand()
	summand2 = get_second_summand()
	print(summation(summand1, summand2))
main()
