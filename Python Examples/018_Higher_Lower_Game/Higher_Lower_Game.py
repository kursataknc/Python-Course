import HigherLower_Data as data
import random

print(data.logo)

end_game = False
score = 0


def random_choose():
	random_index = random.randint(0, len(data.data_dict) - 1)
	random_dict = data.data_dict[random_index]
	return random_dict


def compare(p1, p2):
	if p1["follower_count"] > p2["follower_count"]:
		return p1
	elif p1["follower_count"] < p2["follower_count"]:
		return p2
	else:
		return "Tie"


First_Person = random_choose()
while not end_game:
	print(f"Compare A: {First_Person['name']}, {First_Person['description']}, {First_Person['country']}")
	print(data.vs)
	Second_Person = random_choose()
	print(f"Against B: {Second_Person['name']}, {Second_Person['description']}, {Second_Person['country']}")
	compare(First_Person, Second_Person)
	answer = input("Who has more followers? Type 'A' or 'B': ")
	if answer == "A":
		answer = First_Person
	elif answer == "B":
		answer = Second_Person

	if answer == compare(First_Person, Second_Person):
		score += 1
		print(f"You Win! Your score is {score}")
		First_Person = Second_Person
	elif answer != compare(First_Person, Second_Person):
		end_game = True
		print(f"Your total score is {score}. You lost!")
