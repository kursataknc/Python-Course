import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkeypress(player.go_up, "w")

game_is_on = True

while game_is_on:
	time.sleep(0.1)
	screen.update()

	car_manager.create_car()
	car_manager.move_cars()

	if player.is_at_finish_line():
		player.go_to_start()
		car_manager.level_up()
		scoreboard.increase_score()

	for car in car_manager.cars:
		if car.distance(player) < 20:
			game_is_on = False
			scoreboard.game_over()
			
screen.exitonclick()
