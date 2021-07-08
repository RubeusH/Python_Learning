#Areas of Rectangles
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for
#the length and width of two rectangles. The program should tell the user which rectangle has the
#greater area, or if the areas are the same.

#First we get the details from user
rect1_length = float(input("Give the length of the first rectangle: "))
rect1_width = float(input("Give the width of the first rectangle: "))
rect2_length = float(input("Give the length of the second rectangle: "))
rect2_width = float(input("Give the width of the second rectangle: "))

#Then we compute the areas
rect1_area = rect1_length * rect1_width
rect2_area = rect2_length * rect2_width

#then we compare the areas and display the according results
if rect1_area > rect2_area:
	print("Rectangle 1 is the larger object")
elif rect2_area > rect1_area:
	print("Rectangle 2 is the larger object")
else:
	print("The rectangles are of equal area")
