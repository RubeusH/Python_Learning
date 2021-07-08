number_of_summands = int(input("How many numbers do you want to add? "))
accumulator = 0.0
for i in range(number_of_summands):
	number = float(input("Enter a number here: "))
	accumulator += number
print("The sum of these numbers is:", accumulator)
