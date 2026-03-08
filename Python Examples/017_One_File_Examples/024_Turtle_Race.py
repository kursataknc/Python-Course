import turtle as t
import random

screen = t.Screen()
screen.setup(width=1280, height=960)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color:")
colors = ["red", "blue", "pink", "green", "gray", "black", "white", "yellow", "magenta", "purple", "crimson",
		  "cadet blue", "aquamarine", "dark orange", "brown", "light blue", "light pink"]
y_positions = [-400, -350, -300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300, 350, 400]
turtles = []
for turtle_index in range(0, 17):
	tim = t.Turtle(shape="turtle")
	tim.shapesize(2)
	tim.color(colors[turtle_index])
	tim.penup()
	tim.speed("fastest")
	tim.goto(-600, y_positions[turtle_index])
	turtles.append(tim)
if user_bet:
	cont_game = True
while cont_game:
	for turtle in turtles:
		if turtle.xcor() > 580:
			cont_game = False
			winning_color = turtle.pencolor()
			if user_bet == winning_color:
				print(f"You won! The {winning_color} is the winning turtle!")
			else:
				print(f"You've lost! The {winning_color} is the winning turtle!")
		distance = random.randint(0, 80)
		turtle.forward(distance)
screen.exitonclick()
