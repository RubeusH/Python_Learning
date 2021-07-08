HIGH_SCORE = 95.0
score1 = float(input("Please enter the first score: "))
score2 = float(input("Please enter the second score: "))
score3 = float(input("Please enter the third score: "))
average = (score1+score2+score3)/3.0
print("The test average is:", format(average,'.2f'))
if average > HIGH_SCORE:
    print("Congratulations on this outstanding average!")

