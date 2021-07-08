#This program solves the following problem:

#Write a program that calculates and displays a person’s body mass index (BMI). The BMI is
#often used to determine whether a person is overweight or underweight for his or her height. A
#person’s BMI is calculated with the following formula:
#BMI=weight×703/height2
#where weight is measured in pounds and height is measured in inches. The program should ask
#the user to enter his or her weight and height, then display the user’s BMI. The program should
#also display a message indicating whether the person has optimal weight, is underweight, or is
#overweight. A person’s weight is considered to be optimal if his or her BMI is between 18.5 and
#25. If the BMI is less than 18.5, the person is considered to be underweight. If the BMI value is
#greater than 25, the person is considered to be overweight.

#First we define the appropriate constants
BMI_FORMULA_CONSTANT = 703.0
UNDERWEIGHT = 18.5
OVERWEIGHT = 25.0

#Then we get the height and weight
height = float(input("Please enter your height in inches: "))
weight = float(input("Please enter your weight in pounds: "))

#Then we compute the BMI
BMI = (weight * BMI_FORMULA_CONSTANT)/(height * height)

#Finally we evaluate the BMI and output our results
if BMI < UNDERWEIGHT:
	print("Thin queen slay")
elif BMI > OVERWEIGHT:
	print("Get on the track bitch")
else:
	print("Acceptable but stay diligent and strive for better. A shadow looms over your tummy, the shadow of obesity!")
