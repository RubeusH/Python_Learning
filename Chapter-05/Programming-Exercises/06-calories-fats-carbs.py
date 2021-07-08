'''

This program solves the following problem:

Calories from Fat and Carbohydrates

A nutritionist who works for a fitness club helps members by evaluating their diets. As part of
her evaluation, she asks members for the number of fat grams and carbohydrate grams that they
consumed in a day. Then, she calculates the number of calories that result from the fat, using the
following formula:
calories from fat=fat grams×9
Next, she calculates the number of calories that result from the carbohydrates, using the
following formula:
calories from carbs=carb grams × 4
The nutritionist asks you to write a program that will make these calculations.

'''

#constants
FAT_FACTOR = 9
CARB_FACTOR = 4

#functions
def get_fat():
	return float(input("How many grams of fat? "))
def get_carbs():
	return float(input("How many grams of carbs? "))
def cals_fat(fat):
	return FAT_FACTOR * fat
def cals_carb(carb):
	return CARB_FACTOR * carb
def display_carb_cals(cals_carb):
	print("\nThe calories from carbs are: ", format(cals_carb, '.2f'))
def display_fat_cals(cals_fat):
	print("\nThe calories from fats are: ", format(cals_fat, '.2f'))
def main():
	display_fat_cals(cals_fat(get_fat()))
	display_carb_cals(cals_carb(get_carbs()))
main()
