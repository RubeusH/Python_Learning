#This program solves the question below:

#Age Classifier
#Write a program that asks the user to enter a person’s age. The program should display a
#message indicating whether the person is an infant, a child, a teenager, or an adult. Following
#are the guidelines:
#If the person is 1 year old or less, he or she is an infant.
#If the person is older than 1 year, but younger than 13 years, he or she is a child.
#If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
#If the person is at least 20 years old, he or she is an adult.

#First we make the appropriate constants to avoid magic numbers
INFANT = 1
CHILD = 13
TEENAGER = 20

#Then I get the the user's age
age = float(input("Please enter your age: "))

#Finally, we evaluate the input and output the appropriate message
if age <= INFANT:
	print("You are a baby!")
elif age < CHILD:
	print("You are a child!")
elif age < TEENAGER:
	print("You are a teenager")
else:
	print("You are an adult")
