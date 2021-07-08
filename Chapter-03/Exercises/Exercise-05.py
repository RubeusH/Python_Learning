#This program solves the problem below:

#Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the
#amount of mass of an object in kilograms, you can calculate its weight in newtons with the
#following formula:
#weight=mass×9.8
#Write a program that asks the user to enter an object’s mass, then calculates its weight. If the
#object weighs more than 500 newtons, display a message indicating that it is too heavy. If the
#object weighs less than 100 newtons, display a message indicating that it is too light.

#First we make the appropriate constants
UPPER = 500
LOWER = 100
GRAVITY = 9.8

#Then we get the mass in kg
mass = float(input("What is the mass(kg): "))

#Then we convert mass to weight
weight = mass * GRAVITY

#Then we evaluate the weight and output the appropriate message
if weight > UPPER:
	print("The object is too heavy")
elif weight < LOWER:
	print("The object is too light")
else:
	print("The weight is acceptable")

