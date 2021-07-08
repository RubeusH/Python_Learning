#This program solves the following problem

'''

Write a program that uses nested loops to draw this pattern:
*******
******
*****
****
***
**
*

'''

for i in range(7,0,-1):
	for j in range(i):
		print('*', end = '')
	print()
