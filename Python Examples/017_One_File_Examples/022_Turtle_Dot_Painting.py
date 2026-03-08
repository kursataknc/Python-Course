import turtle as turtle_m
import random

turtle_m.colormode(255)
tim = turtle_m.Turtle()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.shape("turtle")
tim.speed("fastest")


def draw():
	for i in range(9):
		tim.dot(20, random.choice(color_list))
		tim.forward(50)
    
	tim.dot(20, random.choice(color_list))


def turn_left():
	tim.left(90)
	tim.dot(20, random.choice(color_list))
	tim.forward(50)
	tim.left(90)


def turn_right():
	tim.right(90)
	tim.dot(20, random.choice(color_list))
	tim.forward(50)
	tim.right(90)


tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_rows = int(input("How many rows do you want in your painting?"))

# Çift sayı satırlar için
if number_of_rows % 2 == 0:
    for i in range(int(number_of_rows / 2)):
        draw()
        turn_left()
        draw()
        turn_right()
# Tek sayı satırlar için
else:
    for i in range(int(number_of_rows / 2)):
        draw()
        turn_left()
        draw()
        turn_right()
    draw()

screen = turtle_m.Screen()
screen.exitonclick()
