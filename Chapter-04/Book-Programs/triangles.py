#a program to print triangles

#first we get the base
base = int(input("Please enter base size: "))

#Then we draw the triangle
for i in range(base):
	for j in range(i + 1):
		print('*', end = "")
	print()
