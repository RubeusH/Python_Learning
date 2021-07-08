#This program solves the following problem:
#Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
#program that calculates the number of packages of hot dogs and the number of packages of hot
#dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask
#the user for the number of people attending the cookout and the number of hot dogs each person
#will be given. The program should display the following details:
#The minimum number of packages of hot dogs required
#216The minimum number of packages of hot dog buns required
#The number of hot dogs that will be left over
#The number of hot dog buns that will be left over

#First we set the important constants
HOTDOGS = 10
BUNS = 8

#Then we determine the number of people
guests = int(input("How many guests at the party: "))

#Then we computer how many hot dogs and buns are needed
#First we do hotdogs
if guests <= HOTDOGS:
	hotdogs_needed = 1 
else:
	if guests % HOTDOGS == 0:
		hotdogs_needed = int(guests / HOTDOGS)
	else:
		hotdogs_needed = int((guests // HOTDOGS) + 1)
#Then we do the buns
if guests <= BUNS:
	buns_needed = 1
else:
	if guests % BUNS == 0:
		buns_needed = int(guests / BUNS)
	else: 
		buns_needed = int((guests // BUNS) + 1)	
#Then we compute the leftovers
buns_leftover = int(buns_needed * BUNS - guests)
hotdogs_leftover = int(hotdogs_needed * HOTDOGS - guests)
#Then we display the results
print("This gathering required:")
print("\t", hotdogs_needed, "packs of hotdogs")
print("\t", buns_needed, "packs of buns")
print("This gathering wasted:")
print("\t", hotdogs_leftover, "hotdogs")
print("\t", buns_leftover, "buns")
