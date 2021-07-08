#The following program solves the problem below:

#Magic Dates
#The date June 10, 1960, is special because when it is written in the following format, the month
#times the day equals the year:
#6/10/60
#Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit
#year. The program should then determine whether the month times the day equals the year. If
#so, it should display a message saying the date is magic. Otherwise, it should display a message
#saying the date is not magic.

#First we get the relevant data from the user
month = int(input("Enter the month here: "))
day = int(input("Enter the day here: "))
year = int(input("Enter the year here: "))

#Then we compute the month day number
month_x_day = month * day

#Finally we compare it to the year to determine its magical properties (if any exist)
if month_x_day == year:
	print("This date is magical")
else:
	print("This date is not magical")

