males = float(input("How many males in the class? "))
females = float(input("How many females in the class? "))
total = males + females
print("The percentage of males in the class is: " + format((males/total)*100.0,'.2f') + "%","\nThe percentage of females in the class is: " + format((females/total) * 100.0,'.2f') + "%") 
