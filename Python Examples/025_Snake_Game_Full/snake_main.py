from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

scoreboard = Scoreboard()

while game_is_on:
	screen.update()
	time.sleep(snake.snake_speed)
	snake.move()

	# Detect collision with food.
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.increase_score()
		snake.snake_speed *= 0.9
		print(snake.snake_speed)
	# Detect collision with wall.
	if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
		scoreboard.reset()
		snake.reset()

	# Detect collision with tail.
	for segment in snake.segments[1:]:
		if segment == snake.head:
			pass
		elif snake.head.distance(segment) < 10:
			scoreboard.reset()
			snake.reset()



screen.exitonclick()
