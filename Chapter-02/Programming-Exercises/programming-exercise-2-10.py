SUGAR = 1.5
BUTTER = 1.0
FLOUR = 2.75
multiplier = float(input("How many cookies do you want? "))/48.0
print("You will need:","\n\t" + format(multiplier*SUGAR,'.2f') + " cups of sugar", "\n\t" + format(multiplier*BUTTER,'.2f') + " cups of butter", "\n\t" + format(multiplier*FLOUR, '.2f') + " cups of flour")
