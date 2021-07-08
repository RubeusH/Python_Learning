'''

Write a statement that generates a random number in the range of 1 through 100 and assigns it
to a variable named rand .

'''

import random

rand = random.randint(1,100)
while rand != 100:
	rand = random.randint(1,100)
print(rand)
