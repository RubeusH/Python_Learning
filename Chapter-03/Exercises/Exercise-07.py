#The colors red, blue, and yellow are known as the primary colors because they cannot be made
#by mixing other colors. When you mix two primary colors, you get a secondary color, as shown
#here:
#When you mix red and blue, you get purple.
#When you mix red and yellow, you get orange.
#When you mix blue and yellow, you get green.
#Design a program that prompts the user to enter the names of two primary colors to mix. If the
#user enters anything other than “red,” “blue,” or “yellow,” the program should display an error
#message. Otherwise, the program should display the name of the secondary color that results.

#First we name the essential variables
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

#Then we get the color
color1 = (input("Enter the first color: ")).lower()
color2 = (input("Enter the second color: ")).lower()

#Then we determine if it's valid or not. If it's valid we output the mixture result and if it's invalid we output an error
if ((color1 != RED and color1 != BLUE and color1 != YELLOW) or (color1 != RED and color1 != BLUE and color1 != YELLOW)):#if it is not a valid color
	print("Invalid colors")
else:
	if ((color1 == RED and color2 == BLUE) or (color1 == BLUE and color2 == RED)):
		print("Purple")
	elif ((color1 == RED and color2 == YELLOW) or (color1 == YELLOW and color2 == RED)):
		print("Orange")
	elif color1 == color2:
		print(color1)
	else:
		print("Green")
