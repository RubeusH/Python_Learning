#This program solves the following problem

#You have a group of friends coming to visit for your high school reunion, and you want to take
#them out to eat at a local restaurant. You aren’t sure if any of them have dietary restrictions, but
#your restaurant choices are as follows:
#Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
#Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
#Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
#Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
#The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
#Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-
#free, to which then displays only the restaurants to which you may take the group. Here is an
#example of the program’s output:
#Is anyone in your party a vegetarian? yes
#Is anyone in your party a vegan? no
#Is anyone in your party gluten-free? yes
#Here are your restaurant choices:
#Main Street Pizza Company
#Corner Cafe
#The Chef's Kitchen
#Here is another example of the program’s output:
#Is anyone in your party a vegetarian? yes
#Is anyone in your party a vegan? yes
#Is anyone in your party gluten-free? yes
#Here are your restaurant choices:
#Corner Cafe
#The Chef's Kitchen1

#Here we initialize our flags
isVegetarian = False
isVegan = False
isGlutenFree = False
#Here we ask about any dietary concerns
vegetarianQ = input("Is anyone in your party a vegentarian (yes/no): ")
veganQ = input("Is anyone in your party a vegan (yes/no): ")
gluten_freeQ = input("Is anyone in your party GF (yes/no): ")

#Then we update our flags
if vegetarianQ == "yes":
	isVegetarian = True
if veganQ == "yes":
	isVegan = True
if gluten_freeQ == "yes":
	isGlutenFree = True

#Finally we make a recommendation based on our input
if isVegetarian == True and isVegan == True and isGlutenFree == True:
	print("You should try:" + "\n\tThe Chef's Kitchen" + "\n\tThe Corner Cafe")
elif isVegetarian == True and isVegan == True and isGlutenFree == False:
	print("You should try:" + "\n\tThe Chef's Kitchen" + "\n\t\The Corner Cafe")
elif isVegetarian == True and isVegan == False and isGlutenFree == True:
	print("You should try:" + "\n\tThe Chef's Kitchen" + "\n\tThe Corner Cafe " + "\n\tMainsteet Pizza Company")
elif isVegetarian == False and isVegan == True and isGlutenFree == True:
	print("You should try:" + "\n\tCorner Cafe" + "The Chef's Kitchen")
elif isVegetarian == True and isVegan == False and isGlutenFree == False:
	print("You should try:" + "\n\tMainstreet Pizza Company" + "\n\tCorner Cafe" + "\n\tMama's Fine Italian" + "\n\tThe Chef's Kitchen")
elif isVegetarian == False and isVegan == True and isGlutenFree == False:
	print("You should try:" + "\n\tCorner Cafe" + "\n\tThe Chef's Kitchen")
elif isVegetarian == False and isVegan == False and isGlutenFree == True:
	print("You should try:" + "\n\tMainstreet Pizza Company" + "\n\tCorner Cafe" + "\n\tThe Chef's Kitchen")
else:
	print("You can go to any restaurant")

