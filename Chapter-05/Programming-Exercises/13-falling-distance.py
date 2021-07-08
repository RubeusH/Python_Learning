'''

Falling Distance

When an object is falling because of gravity, the following formula can be used to determine the
distance the object falls in a specific time period:
d=12gt2
The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the
amount of time, in seconds, that the object has been falling.
Write a function named falling_distance that accepts an object’s falling time (in seconds) as
an argument. The function should return the distance, in meters, that the object has fallen during
that time interval. Write a program that calls the function in a loop that passes the values 1
through 10 as arguments and displays the return value.

'''
GRAVITY = 9.8
FACTOR = 12.0
def falling_distance(falling_time):
	return FACTOR * GRAVITY * falling_time ** 2
def get_time():
	return float(input("How long does the object fall for? "))
def get_iterations():
	return int(input("How many values do you want to enter? "))
def looper(iterations):
	for i in range(iterations):
		print(format(falling_distance(get_time()), '.2f'))
def main():
	looper(get_iterations())
main() 
