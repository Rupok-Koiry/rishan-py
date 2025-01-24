from turtle import Turtle, Screen
import time
import random

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DELAY = 0.2


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = RIGHT

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        if self.check_wall_collision():
            return False
        return True

    def up(self):
        if self.direction != DOWN:
            self.direction = UP
            self.head.setheading(UP)

    def down(self):
        if self.direction != UP:
            self.direction = DOWN
            self.head.setheading(DOWN)

    def left(self):
        if self.direction != RIGHT:
            self.direction = LEFT
            self.head.setheading(LEFT)

    def right(self):
        if self.direction != LEFT:
            self.direction = RIGHT
            self.head.setheading(RIGHT)

    def check_wall_collision(self):
        x, y = self.head.xcor(), self.head.ycor()
        if x < -290 or x > 290 or y < -290 or y > 290:
            return True
        return False


class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.goto(x, y)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            with open("data.txt", mode="w") as data:
                data.write("0")
            self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center",
                   font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
apple = Apple()
scoreboard = Scoreboard()


def go_up():
    snake.up()


def go_down():
    snake.down()


def go_left():
    snake.left()


def go_right():
    snake.right()


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    if not snake.move():
        game_is_on = False
        scoreboard.reset_score()
        scoreboard.goto(0, 0)
        scoreboard.write("Game Over", align="center",
                         font=("Courier", 24, "normal"))
    if snake.head.distance(apple) < 20:
        apple.refresh()
        snake.grow()
        scoreboard.increase_score()
    time.sleep(DELAY)

screen.mainloop()
