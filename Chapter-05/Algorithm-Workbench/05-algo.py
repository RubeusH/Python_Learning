'''

Look at the following function definition:
def my_function(a, b, c):
d = (a + c) / b
print(d)
1. Write a statement that calls this function and uses keyword arguments to pass 2 into a , 4
into b , and 6 into c .
2. What value will be displayed when the function call executes?

'''

def my_function(a, b, c):
	d = (a + c) / b
	print(d)
my_function(a = 2, b = 4, c = 6)

