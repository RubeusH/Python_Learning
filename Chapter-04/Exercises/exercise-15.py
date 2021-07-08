'''

This program solves the following question:

Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #
#      #
#       #
#        #

'''
#Here we define our constants
FIRST_CHARACTER = 0

#here we get the user input because we made the program more fancy
triangle_height = int(input("How high do you want the triangle? "))
triangle_symbol = input("Enter one character you want to make the pyramid out of (WARNING: if you're cheeky and enter a big string I'll just take the first char): ")

#then we print some space and a header so that the triangle is separated from the input prompts
print('\n\n\nBEHOLD, YOUR TRIANGLE!\n\n')

#then we draw the triangle
for i in range(triangle_height):
	print(triangle_symbol[FIRST_CHARACTER], end = '')
	for j in range(i):
		print(' ', end = '')
	print(triangle_symbol[FIRST_CHARACTER])
