import random

# First Example
names_string = input("Give me the names of bitches! ")
names = names_string.split(", ")
print(names)
print(names[0])

# Second Example
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

randomint = random.randint(0, len(names)-1)
print(f"{names[randomint]} is going to buy the meal today!")
