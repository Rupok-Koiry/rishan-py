import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("Bangladesh Divisions Game")
screen.setup(width=800, height=600)

# Correct paths to your files
# Provide the correct path to your CSV
csv_file = r"day25\us-states-game-start\bd_divisions.csv"
image_file = r"day25\us-states-game-start\bdd.gif"  # Path to the GIF file

screen.addshape(image_file)
turtle.shape(image_file)

data = pd.read_csv(csv_file)

all_divisions = data['Division'].to_list()
guessed_divisions = []

# Simulate input in the top-right corner using padding
while len(guessed_divisions) < len(all_divisions):
    # Add padding with spaces to simulate input alignment to the right
    answer_division = screen.textinput(
        title=" " * 70 + f"{len(guessed_divisions)
                            }/{len(all_divisions)} Divisions Correct",
        prompt=" " * 70 + "Guess a division:"
    )

    if answer_division:
        answer_division = answer_division.title()

        if answer_division in all_divisions and answer_division not in guessed_divisions:
            guessed_divisions.append(answer_division)
            division_data = data[data['Division'] == answer_division]

            x = division_data['x'].values[0]
            y = division_data['y'].values[0]

            # Check if coordinates are available
            if pd.isna(x) or pd.isna(y):
                print(f"Coordinates for {answer_division} are missing.")
                continue

            # Create a turtle to write the division name on the map
            turtle_pen = turtle.Turtle()
            turtle_pen.hideturtle()
            turtle_pen.penup()
            turtle_pen.goto(int(x), int(y))
            turtle_pen.color("black")
            turtle_pen.write(answer_division, align="center",
                             font=("Arial", 12, "bold"))

screen.mainloop()
