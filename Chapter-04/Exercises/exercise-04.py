#This program solves the problem below:

#Distance Traveled
#The distance a vehicle travels can be calculated as follows:
#distan⁡ce = speed × time
#For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120
#miles. Write a program that asks the user for the speed of a vehicle (in miles per hour) and the
#number of hours it has traveled. It should then use a loop to display the distance the vehicle has
#traveled for each hour of that time period. Here is an example of the desired output:
#What is the speed of the vehicle in mph? 40
#How many hours has it traveled? 3
#Hour Distance Traveled
#1
#40
#2
#80
#3
#120

#First we obtain pertinent user data
speed = float(input("How fast are you travelling (mph)? "))
time = int(input("How long were you travelling for (hours)? "))

#Then we display the header
print("Hour Distance Travelled")
for hour in range(time):
	distance = speed * (hour + 1)	
	print(hour + 1, "\t", distance)
