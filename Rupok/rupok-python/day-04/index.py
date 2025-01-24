# import random
# names = input('Enter the names: ')
# namesList = names.split(',')
# randomIndex = random.randint(0, len(namesList)-1)
# print(randomIndex)
# randomName = namesList[randomIndex]
# print(f'{randomName} will pay the bill!')
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# map[int(position[1])-1][int(position[0])-1] = "x"

# # Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game = [rock, paper, scissors]
# user_input = int(input('1 = Rock, 2 = Paper, 3 = Scissors: \t'))
# computer_input = random.randint(1, 3)
# result = ''

# if user_input == 1:
#     if computer_input == 1:
#         result = 'draw'
#     elif computer_input == 2:
#         result = 'lose'
#     elif computer_input == 3:
#         result = 'win'
# elif user_input == 2:
#     if computer_input == 1:
#         result = 'win'
#     elif computer_input == 2:
#         result = 'draw'
#     elif computer_input == 3:
#         result = 'lose'
# elif user_input == 3:
#     if computer_input == 1:
#         result = 'lose'
#     elif computer_input == 2:
#         result = 'win'
#     elif computer_input == 3:
#         result = 'draw'

# print(f"You choose {game[user_input-1]}")
# print(f"Computer choose {game[computer_input-1]}")

# if result == 'win':
#     print('You Won')
# elif result == 'lose':
#     print('You Lose')
# elif result == 'draw':
#     print('Draw')
