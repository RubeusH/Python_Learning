#This program solves the problem below:

#Write a program that asks the user to enter a number of seconds and works as follows:
#There are 60 seconds in a minute. If the number of seconds entered by the user is greater
#than or equal to 60, the program should convert the number of seconds to minutes and
#seconds.
#There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater
#218than or equal to 3,600, the program should convert the number of seconds to hours,
#minutes, and seconds.
#There are 86,400 seconds in a day. If the number of seconds entered by the user is greater
#than or equal to 86,400, the program should convert the number of seconds to days, hours,
#minutes, and seconds.

#First we define our constants
MINUTE = 60
HOUR = 3600
DAY = 86400

#Then we ask the user for a number of seconds
seconds = int(input("Please enter a number: "))

#Finally we evaluate and output
if seconds < 0:
	print("invalid input")
elif seconds < MINUTE:
	print(seconds, "seconds")
elif seconds < HOUR:
	minutes = seconds // MINUTE
	seconds = seconds - minutes * MINUTE	
	print(minutes, "m", seconds, "s")
elif seconds < DAY:
	hours = seconds // HOUR
	seconds = seconds - hours * HOUR
	minutes = seconds // MINUTE
	seconds = seconds - minutes * MINUTE
	print(hours, "h", minutes, "m", seconds, "s")
else:
	days = seconds // DAY
	seconds = seconds - days * DAY
	hours = seconds // HOUR
	seconds = seconds - hours * HOUR
	minutes = seconds // MINUTE
	seconds = seconds - minutes * MINUTE
	print(days, "d", hours, "h", minutes, "m", seconds, "s")
