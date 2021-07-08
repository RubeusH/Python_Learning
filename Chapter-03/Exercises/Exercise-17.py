#This program implements a wifi flowchart from the book

print("Reboot the computer and try to connect")
feedback = (input("Did that help (yes/no)? ")).lower()
if feedback == "yes":
	print("Have a nice day!")
else:
	print("Reboot the router and try to connect")
	feedback = (input("Did that help (yes/no) ")).lower()
	if feedback == "yes":
		print("Have a nice day!")
	else:
		print("Make sure the cables between the router and the modem are tight")
		feedback = (input("Did that help? (yes/no) ")).lower()
		if feedback == "yes":
			print("Have a nice day!")
		else:
			print("Move the router to a new location and try to connect")	
			feedback = (input("Did that help (yes/no) ").lower())
			if (feedback == "yes"):
				print("Have a nice day!")
			else:
				print("Get a new router!")
