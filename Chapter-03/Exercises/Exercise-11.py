#This program solves the problem below which I believe is a fairly dumb one but w/e:

#Serendipity Booksellers has a book club that awards points to its customers based on the
#number of books purchased each month. The points are awarded as follows:
#If a customer purchases 0 books, he or she earns 0 points.
#If a customer purchases 2 books, he or she earns 5 points.
#If a customer purchases 4 books, he or she earns 15 points.
#If a customer purchases 6 books, he or she earns 30 points.
#If a customer purchases 8 or more books, he or she earns 60 points.
#Write a program that asks the user to enter the number of books that he or she has purchased
#this month, then displays the number of points awarded.

#First we declare our constants
LEVEL1 = 2
LEVEL2 = 4
LEVEL3 = 6
LEVEL4 = 8

#Then we get the input
books_read = int(input("How many books did you buy this month? "))

#Then we evaluate the input and display the appropriate result
if books_read < LEVEL1:
	print("You receive 0 points")
elif books_read == LEVEL1:
	print("You receive 5 points")
elif books_read == LEVEL2:
	print("You receive 15 points")
elif books_read == LEVEL3:
	print("You receive 30 points")
else:
	print("You receive 60 points") 
