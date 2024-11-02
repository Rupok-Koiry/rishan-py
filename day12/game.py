
# import random


# def com():
#     print("Hmm I Guessed A Number ...")


# com()

# user_live = input("Do You Want To Play Hard Or Easy? (hard/easy) ?: ")


# def user():
#     if user_live == "hard":
#         lives = 5
#     else:
#         lives = 10

#     game = True
#     computer = random.randint(1, 100)
#     print(f"You Have {lives} Lives")

#     while game and lives > 0:
#         user_input = int(input("Enter A Guess Number: "))

#         if user_input == computer:
#             print("Good! I Lost, You Win.")
#             print(f"You had {lives} Lives left.")
#             game = False
#         elif user_input > computer:
#             lives -= 1
#             print("Guess Lower.")
#         elif user_input < computer:
#             lives -= 1
#             print("Guess Higher.")

#         if lives > 0 and game:
#             print(f"You Have {lives} Lives Left.")
#         elif lives == 0:
#             print("Out of Lives! You Lost.")
#             print(f"The correct number was {computer}.")


# user()
