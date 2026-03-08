import turtle
import pandas
import os

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=726, height=491) 

# Betiğin bulunduğu dizini al ve resim dosyasının tam yolunu oluştur
script_directory = os.path.dirname(__file__)
image_path = os.path.join(script_directory, "blank_states_img.gif")
csv_path = os.path.join(script_directory, "50_states.csv")

screen.addshape(image_path)
turtle.shape(image_path)
data = pandas.read_csv(csv_path)
states = len(data["state"])
score = 0
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
	answer_state = screen.textinput(title=f"{score}/{states} Guess the State",
	                                prompt="What's another state's name?").title()
	if answer_state in all_states:
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer_state]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(state_data.state.item())
		score += 1
	if answer_state == "Exit":
		missing_states = [state for state in all_states if state not in guessed_states]
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break
