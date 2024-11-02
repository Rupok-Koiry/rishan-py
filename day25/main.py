# import csv

# file_name = r'C:\Users\USER\Desktop\python\day25\weather_dat.csv'

# with open(file_name, "r") as file:
#     data = file.readlines()
#     tempatuers = []
#     for row in data:
#         if row[1] != "temp":
#             tempatuers.append(row[1])
#     print(tempatuers)
# import pandas as broooo
# data = broooo.read_csv("day25/weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# average_temp_pandas = data["temp"].mean()
# average_temppandas = data["temp"].max()
# print(data["condition"])
# print(average_temp_pandas)
# print(average_temppandas)
# print(data[data.day == "Monday"])
# import pandas as pd


# data = pd.read_csv(
#     "D:\\Rupok\\udemy\\python\\25. Day 25 - Intermediate - Working with CSV Data and the Pandas Library\\4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


# color_counts = data['Primary Fur Color'].value_counts()
# print(color_counts)
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        turtle_pen = turtle.Turtle()
        turtle_pen.hideturtle()
        turtle_pen.penup()
        turtle_pen.goto(int(state_data.x), int(state_data.y))
        turtle_pen.write(answer_state)

screen.mainloop()
