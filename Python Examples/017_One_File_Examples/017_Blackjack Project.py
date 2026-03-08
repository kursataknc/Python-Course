import random

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' and press enter: ")
if start_game == "y":
	print("Welcome to the Blackjack game!")
else:
	print("GİT BURDAN")
	exit()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_first_card = random.choice(cards)
your_second_card = random.choice(cards)
your_cards = [your_first_card, your_second_card]
your_sum = your_first_card + your_second_card
computers_first_card = random.choice(cards)
computers_second_card = random.choice(cards)
computers_cards = [computers_first_card, computers_second_card]
print(f"""Your cards:  [{your_first_card}, {your_second_card}], current score: {your_sum}
		Computer's first card: {computers_first_card}""")
computers_hidden_sum = computers_first_card + computers_second_card
cont_game = input("Type 'y' to draw another card, or 'n' to end the game.")
while your_sum < 21 and cont_game == "y":
	your_card = random.choice(cards)
	your_sum += your_card
	your_cards += [your_card]
	print(f"Your cards:  [{your_first_card}, {your_second_card}, {your_card}], current score: {your_sum}")
	print(f"Computer's first card: {computers_first_card}")
	if your_sum > 21:
		for x in your_cards:
			if x == 11:
				x = 1
			if your_sum > 21:
				print("You busted!")
				exit()
				cont_game = "n"
	cont_game = input("Type 'y' to draw another card, or 'n' to end the game.")
while computers_hidden_sum < 15:
	computers_card = random.choice(cards)
	computers_hidden_sum += computers_card
	computers_cards += [computers_card]
	if computers_hidden_sum > 21:
		break
if cont_game == "n":
	print(f"""
Computer's cards:  [{computers_cards}], 
Current computer score: {computers_hidden_sum}
		""")
	if computers_hidden_sum > 21 and your_sum <= 21:
		print("You win!")
	elif your_sum == 21:
		print("You win!")
	elif your_sum == computers_hidden_sum:
		print("You tied!")
	elif your_sum > computers_hidden_sum:
		print("You win!")
	elif your_sum < computers_hidden_sum:
		print("You lose!")
	else:
		print("You messed up!")
