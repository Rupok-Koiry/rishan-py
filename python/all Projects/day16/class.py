# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape = ("turtle")
# timmy.color = ("red")
# timmy.forward(100)
# timmy.left(1200)
# timmy.forward(100)
# timmy.left(1200)
# timmy.forward(100)
# print("triangle")


# print(timmy)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# import turtle

# # Set up the screen and turtle
# screen = turtle.Screen()
# screen.bgcolor("white")
# pen = turtle.Turtle()
# pen.color("red")
# pen.pensize(3)
# pen.speed(3)

# # Move the turtle to start position
# pen.penup()
# pen.goto(0, -100)
# pen.pendown()

# # Draw the heart shape
# pen.begin_fill()
# pen.left(140)
# pen.forward(180)
# pen.circle(-90, 200)
# pen.left(120)
# pen.circle(-90, 200)
# pen.forward(180)
# pen.end_fill()

# # Hide the turtle and display the window
# pen.hideturtle()
# turtle.done()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column(
#     "Footballer", ["1) Ronaldo", "De bruyne", "Garnacho", "Neymar Jr", "Messi"])
# table.add_column("Second name", ["penaldo", "kodu", "gunga", "noob", 'popko'])
# print(table)
# class car:
#     def __init__(self):
#         print("new user being created")


# user1 = car()
# print("😁😁😁😁😁😁")
# import random
# "quiz game"
# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.",
#         "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]
# should_continue = True
# score = 0
# question = 0
# while should_continue:

#     comp = random.choice(question_data)
#     question += 1
#     print(f"{question})Question:{comp["text"]}")
#     user = input("Enter True Or False: ")
#     answer_checker = comp['answer']

#     if user == "False" and answer_checker == "True":
#         print("You lost That Was True😵.")
#         should_continue = False

#     elif user == "True" and answer_checker == "False":
#         print("You lost That Was False😵.")
#         should_continue = False
#     elif user == answer_checker:
#         print("Congratulations, You Win 😊.")

# print(f"You got {question} right And your score is {score}")
# import random


# class QuizGame:
#     def __init__(self, question_data):
#         self.question_data = question_data
#         self.score = 0

#     def play(self):
#       questions = random.sample(self.question_data, len(self.question_data))
#       for i, question in enumerate(questions, start=1):
#     # Your code here

#             print(f"{i}) Question: {question['text']}")
#             user_answer = input("Enter True or False: ")
#             if user_answer == question['answer']:
#                 print("Correct! 😊")
#                 self.score += 1
#             else:
#                 print(f"Wrong! The correct answer was {question['answer']} 😵")
#                 break
#       print(f"You answered {i} questions. Your final score is {self.score}.")


# # Example usage:
# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.",
#         "answer": "False"},
#     {"text": "A few ounces of chocolate can kill a small dog.", "answer": "True"}
# ]

# game = QuizGame(question_data)
# game.play()
# def find_prime(start, end):
#     prime = []
#     for num in range(start, end + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 prime.append(num)
#     print(prime)


# find_prime(1, 100)
'''answer angela'''


# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello my name is  {self.name} ")


# person1 = person("angela", "10")
# person1.greet()

# firs = int(input("Enter first number:"))
# secon = int(input("Enter your second number:"))
# su = input("Enter you subtraction:")


# class cal:
#     def __init__(self, first, second, sub):
#         self.first = first
#         self.second = second
#         self.sub = sub

#     def subtraction(self):
#         if self.sub == "+":
#             print(f"your answer is {self.first+self.second}")
#         elif self.sub == "-":
#             print(f"your answer is {self.first-self.second}")


# person1 = cal(firs, secon, su)
# person1.subtraction()
