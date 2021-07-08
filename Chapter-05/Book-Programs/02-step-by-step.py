'''

Professional Appliance Service, Inc. offers maintenance and repair services for household
appliances. The owner wants to give each of the company’s service technicians a small handheld
computer that displays step-by-step instructions for many of the repairs that they perform. To see
how this might work, the owner has asked you to develop a program that displays the following
instructions for disassembling an Acme laundry dryer:
Step 1: Unplug the dryer and move it away from the wall.
Step 2: Remove the six screws from the back of the dryer.
Step 3: Remove the dryer’s back panel.
Step 4: Pull the top of the dryer straight up.
During your interview with the owner, you determine that the program should display the steps one
at a time. You decide that after each step is displayed, the user will be asked to press the Enter key to
288see the next step. Here is the algorithm in pseudocode:
Display a starting message, explaining what the program does.
Ask the user to press Enter to see step 1.
Display the instructions for step 1.
Ask the user to press Enter to see the next step.
Display the instructions for step 2.
Ask the user to press Enter to see the next step.
Display the instructions for step 3.
Ask the user to press Enter to see the next step.
Display the instructions for step 4.

'''
#Here we define main to execute the algorithm from problem description
def main():
	starting_message()
	next_step()	
	step_1()
	next_step()
	step_2()
	next_step()
	step_3()
	next_step()
	step_4()

#Here we define the individual steps of the algorithm
def starting_message():
	print("Welcome to the laundry repair instruction program. We give you instructions on how to repair laundry equipment!")
def next_step():
	input("Press enter to see next step!: ")
def step_1():
	print("Step 1: Unplug the dryer and move it away from the wall.")
def step_2():
	print("Step 2: Remove the six screws from the back of the dryer.")
def step_3():
	print("Step 3: Remove the dryer’s back panel.")
def step_4():
	print("Step 4: Pull the top of the dryer straight up.")

#Finally we execute the whole thing
main()
