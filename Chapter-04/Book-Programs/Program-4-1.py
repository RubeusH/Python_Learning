keepGoing = 'y'
while keepGoing == 'y':
	sales = float(input("How many sales? "))
	commissionRate = float(input("What is the commission rate? "))
	commission = sales * commissionRate
	print("The commission is: ", commission)
	keepGoing = input("Do you want to computer another commission (y/n)? ")
 
