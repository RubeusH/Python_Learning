num_steps = int(input("How many steps do you want? "))

for i in range(num_steps):
	for j in range(i):
		print(" ", end = '')
	print("#")
