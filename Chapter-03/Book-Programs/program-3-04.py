#comparing two names with the '<' operator in python

#first we ask for two names
name1 = input("Please enter the first name: ")
name2 = input("Please enter the second name: ")

#then we compare the two
if name1 > name2:
	print(name1 + " is the greater name")
if name2 == name1:
	print("The names are equal")
if name2 > name1:
	print(name2 + " is the greater name")
