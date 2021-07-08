'''

Dr. Kimura was so happy with the dice rolling simulator that you wrote for him, he has asked you to
write one more program. He would like a program that he can use to simulate ten coin tosses, one
after the other. Each time the program simulates a coin toss, it should randomly display either
“Heads” or “Tails”.
You decide that you can simulate the tossing of a coin by randomly generating a number in the range
of 1 through 2. You will write an if statement that displays “Heads” if the random number is 1, or
“Tails” otherwise. Here is the pseudocode:
Repeat 10 times:
If a random number in the range of 1 through 2 equals 1 then:
Display ‘Heads’
Else:
Display ‘Tails’
Because the program should simulate 10 tosses of a coin you decide to use a for loop.

'''
#We user random to simluate the coin toss
import random

#Here we define our constants
HEADS = 1
TAILS = 2
TRIALS = 10

for trial in range(TRIALS):
	coin_toss = random.randint(HEADS, TAILS)
	if coin_toss == HEADS:
		print("The result of trial", trial + 1, "is:")
		print("Heads")
	else:
		print("The result of trial", trial + 1, "is:")
		print("Tails")
