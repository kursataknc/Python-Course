import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard'")

difficulty = input()
end_game = False
rand_number = random.randint(1, 100)
def comparenumbers():
	global rand_number, guessed_number
	if guessed_number < rand_number:
		print("Too low!")
	elif guessed_number > rand_number:
		print("Too high!")
	elif guessed_number == rand_number:
		print("You win!")

if difficulty == "easy":
	attempt = 10
elif difficulty == "hard":
	attempt = 5
	
print(f"You have {attempt} attempts left!")

while not end_game:
		guessed_number = int(input("Make a guess:"))
		if guessed_number != rand_number:
			attempt -= 1
			comparenumbers()
			print(f"You have {attempt} attempts left!")
		elif guessed_number == rand_number:
			print("You win!")
			end_game = True
		if attempt == 0:
			end_game = True
			print("You lose!")