import time
import random
from turtle import Screen, Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DELAY = 0.5
WALLS = [(-290, -290, 290, -290), (290, -290, 290, 290),
         (-290, -290, -290, 290), (-290, 290, 290, 290)]


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}",
                   align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


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
        segment.color("yellow")
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
        if self.check_wall_collision() or self.check_self_collision():
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

    def check_self_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    game_is_on = snake.move()
    time.sleep(DELAY)

    # Check if the snake has eaten the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    # Check for collisions
    if not game_is_on:
        scoreboard.game_over()

screen.exitonclick()
