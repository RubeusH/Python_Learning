PASSWORD = "gM7653&$" #the password as a constant
#Immediately below, we ask the user for their password
password = input("Enter your password please: ")
#We then use an if structure to determine if the entered password is correct
if PASSWORD == password:
	print("Successful login")
else:
	print("Incorrect password!")
