'''

The following statement calls a function named half , which returns a value that is half that of
the argument. (Assume the number variable references a float value.) Write code for the
function.
351result = half(number)

'''
#constants
HALF_FACTOR = 2.0
def half(number):
	return number / HALF_FACTOR
def main():
	user_input = float(input("What number do you want to divide by two? "))
	print(half(user_input))
main()
