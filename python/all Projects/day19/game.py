import random
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def circle():

    # draw your circle
    tim.circle(100)
    # rotate so you are looking towards the centre of the circle
    tim.left(10)
    # lift the pen so no line is drawn

    tim.forward(10)
    # put pen down now (if you need to)

    # rotate back (if you need to)
    tim.right(10)


def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup
    tim.home
    tim.pendown()


screen.onkey(key="r", fun=turn_right)
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="c", fun=circle)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="o", fun=clear)
screen.exitonclick()

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)


if user_bet:
    race_on = True
else:
    race_on = False

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {
                      winning_color} turtle is the winner!")
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
