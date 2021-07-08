length = float(input("Enter your penis length: "))#Gets the length of the user's dick
circumference = float(input("Enter your penis width here: "))#Gets the circumference of the user's dick
PI = 3.14159 #named constant for the mathematical constant pi
area = PI*((circumference / (2*PI)))**2 #this gets us the area of a cross section of the penis which will be used to approximate volume
volume = length*area #computer volume of a cylinder according to height x area
print("The volume of your dick is:", volume) 
