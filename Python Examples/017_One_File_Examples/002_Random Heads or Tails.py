import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


#Note that random.seed() function sets the value of randint function constant according to the seed that you gave. 
integer = random.randint(0,1)
if integer == 1:
	print("Heads")
else:
	print("Tails")