'''
This program solves the following problem:

The Kilometer Converter Problem
Write a program that asks the user to enter a distance in kilometers, then converts that distance
to miles. The conversion formula is as follows:
Miles=Kilometers×0.6214

'''

#constants
FACTOR = 0.6214

#functions
def get_kms():
	return float(input("Please enter a distance in kilometers: "))
def kms_to_miles(distance_kilometers):
	return (distance_kilometers * FACTOR)
def main():
	print(format(kms_to_miles(get_kms()), '.2f'))
main()
