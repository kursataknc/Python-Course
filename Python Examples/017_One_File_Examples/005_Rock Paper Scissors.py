rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
x = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if x == "0":
	print(rock)
if x == "1":
	print(paper)
if x == "2":
	print(scissors)

hand = [rock, paper, scissors]

random_int = random.randint(0, 2)
print(random_int)

y = hand[random_int]
print(y)

if x == y:
	print("Draw! Play again.")
elif x == "0" and y == paper:
	print("You lose!")
elif x == "0" and y == scissors:
	print("You win!")
elif x == "1" and y == rock:
	print("You win!")
elif x == "1" and y == scissors:
	print("You lose!")
elif x == "2" and y == paper:
	print("You win!")
elif x == "2" and y == rock:
	print ("You lose!")
