
# print("HELLO SIR/MADAM WELCOME TO THE BAND NAME GENARATOR.\n")
# a = input("Enter your City Name YOU GROW UP IN:\n")
# b = input("Enter your pet Name:\n")
# c = a + b
# a = ("YOUR BAND NAME IS ")
# print(a, c)


# print("HELLO WORLD!")
# print('HELLO WORLD OF PYTHON PROGRAMMING LANGUAGE!\nRISHAN KOIRY...')


# print("Day-1Python Print Function")
# print("hello world\nhello world")
# a = input('ENTER YOUR NAME :')
# print(f"hello{a}")
# a = input("ENTER YOUR NAME:")
# b = len(a)
# print(f"your name have {b} alphabet")
# a = int(input("enter your number:"))
# b = int(input("enter your number:"))
# c = a
# a = b
# b = c

# print(a, b)

# print("WELCOME TO THE TIP CALCULATOR.")
# n = input("ENTER YOUR CURRENCY NAME:")
# a = float(input("WHAT IS THE TOTAL BILL? :"))
# b = int(input("HOW MANY PEOPLE TO SPILT THE BILL? :"))
# c = float(input("what percentage tip do you like to give :"))


# x = (a+a*(c/100))/b


# if c == 0:
#     print("EACH PERSON SHOULD PAY ", a, n)

# else:
#     print("EACH PERSON SHOULD PAY", x, n)
# name = len(input('enter your name'))
# # print(f"your name has {name} cracter")
# name = len(input('enter your name'))
# # print(f"your name has {name} cracter")
# a = float(123)
# print(type(a))
# a = input("enter your NUMBER :")
# b = a[0]
# c = a[1]
# result = int(b)+int(c)
# print(result)
# a = float(input("ENTER YOUR HEIGHT:"))
# b = float(input("ENTER YOUR WEIGHT:"))
# c = float(b*b)
# v = float(a/c)
# print(f"your body mass is {v}")
# age = int(input("ENTER your age   :"))
# year = 90-age
# month = year*12
# week = year*52
# day = year*365
# print(f"you need {year} year to get 90 years old ")
# print(f"you need {month} month to get 90 years old ")
# print(f"you need {week} week to get 90 years old ")
# print(f"you need {day}  day to get 90 years old ")
# You have 12410 days, 1768 weeks, and 408 months left.
# height = int(input('enter you heigh in cm :'))
# if height >= 120:
#     print("you can ride rollarcloster")

# else:
#     print("you can not ride rolarcoster")
'''my new odd even program'''
# number = int(input("ENTER YOUR NUMBER -__-  :"))
# if number % 2 == 0:
#     print(f"THE NUMBER {number} IS EVEN-__-")


# else:
#     print(f"THE NUMBER {number} IS ODD-__-")
# year = int(input("ENTER YOUR YEAR:"))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("IT`S A LEAP YEAR")
# else:
#     print("IT`S NOT A LEAP YEAR")
# print("Hey sir, welcome to Pizza Rishan!")

# # Get the size of the pizza
# size = input(
#     "Which size pizza do you want? Enter 's' for small, 'm' for medium, 'l' for large: ")

# # Get the preference for onions
# onion = input(
#     "Do you want onions in your pizza? Enter 's' for some, 'm' for medium, 'v' for very much: ")

# # Get the preference for extra cheese
# cheese = input(
#     "Do you want extra cheese on your pizza? Enter 'y' for yes, 'n' for no: ")

# # Initialize the bill
# bill = 0

# # Calculate the cost based on pizza size
# if size == 's':
#     bill += 100
#     size_name = "small"
# elif size == 'm':
#     bill += 300
#     size_name = "medium"
# elif size == 'l':
#     bill += 500
#     size_name = "large"
# else:
#     print("Invalid size selected!")
#     size_name = None

# # If a valid size was selected, proceed with additional options
# if size_name:
#     # Calculate the cost based on onion preference
#     if onion == 's':
#         bill += 10
#         onion_amount = "some"
#     elif onion == 'm':
#         bill += 20
#         onion_amount = "medium"
#     elif onion == 'v':
#         bill += 30
#         onion_amount = "very much"
#     else:
#         print("Invalid onion amount selected!")
#         onion_amount = None

#     # Calculate the cost based on extra cheese preference
#     if cheese == 'y':
#         bill += 40
#         cheese_extra = "with extra cheese"
#     elif cheese == 'n':
#         cheese_extra = "without extra cheese"
#     else:
#         print("Invalid cheese option selected!")
#         cheese_extra = None

#     # Print the final bill if all options were valid
#     if onion_amount and cheese_extra:
#         print(f"You ordered a {size_name} pizza {
#               cheese_extra} and {onion_amount} onions.")
#         print(f"Your total bill is {bill} tk.")

# # Output in case of invalid options
# if not size_name or not onion_amount or not cheese_extra:
#     print("There was an error with your order. Please try again.")
# import random
# size = input("ENTER YOUR PIZZA SIZE  SMALL OR MEDIUM OR LARGE:")
# onion = input("DO YOU WANT ONION IN PIZZA :")
# chess = input("DO YOU NEED CHESS IN PIZZA :")
# bill = 0
# if size == "small":
#     print("small size pizza is 100 tk")
#     bill = bill+100
# elif size == "medium":
#     print("medium size pizza is 250tk")
#     bill = bill+250
# elif size == "large":
#     print("large size pizza is 500tk")
#     bill = bill+500
# if onion == "some":
#     print("your onion price 5tk")
#     bill = bill+5
# elif onion == "medium":
#     print("your onion price 15tk")
#     bill = bill+15
# elif onion == "so much":
#     print("your onion price 50tk")
#     bill = bill+50
# if chess == "some":
#     print("your chess price 10tk")
#     bill = bill+10
# elif chess == "medium":
#     print("your chess price 20tk")
#     bill = bill+20
# elif chess == "so much":
#     print("your chess price 50tk")
#     bill = bill+50
# v = input("SIR IS THAT YOUR ORDER.")
# print(f"SIR YOUR BILL IS {bill}")
# bill = 0

# a = int(input("ENTER YOUR HEIGHT IN CM:"))
# if a > 120:
#     print("you can ride rolar closter")
#     b = int(input("enter your age:"))
#     if b <= 5:
#         print("your need  5$")
#         bill += 5
#     elif b >= 6:
#         print("your need  10$")
#         bill += 10
#     elif b > 20:
#         print("you need 20$")
#         bill += 20
#     p = input("do you want a photo:")
#     if p == "yes":
#         print("you need 3 $")
#         bill += 3
#     elif p == "no":
#         print("ok")
#     print(f" thanks, your total bill is {bill}$")
# elif a < 120:
#     print("you can not ride rolar closter")
# print("WELCOME TO THE LOVE CALCULATOR")

# name = input("enter your name:")
# name1 = input("enter her name:")
# n = name+name1
# lower = n.lower()

# t = lower.count("t")
# r = lower.count("r")
# u = lower.count("u")
# e = lower.count("e")
# true = t+r+u+e
# l = lower.count("l")
# o = lower.count("o")
# v = lower.count("v")
# e = lower.count("e")
# love = l+o+v+e
# x = str(true)+str(love)
# v = int(x)


# if v > 20:
#     print(f"{name} love is good to {name1}")
# elif v > 50:
#     print(f"{name} you are best with {name1}")
# else:
#     print("100% love love love o 100% love love love ")
# print("its a trusure island game.")
# print("think you are in a island")
# road = input("enter do you wnt to go right or left:")
# if road == "right":
#     print("you lose")
# elif road == "left":
#     print("you are in  a small island now ")
#     b = input("do you wnt to swim into the village or wait for a boat:")
#     if b == "swim":
#         print("you lose")
#     elif b == "wait":
#         print("now you are in a village  you have 3 doors red and blue and yellow")
#         l = input("which door do you want to go:")
#         if l == "red":
#             print("you lose")
#         elif l == "blue":
#             print("you lose")
#         else:
#             print("you won the game and you won a tesure")
#             print(''' you get a truaser chest


#         _________________________
#        /#########################\\
#       /############################\\
#      /##############################\\
#     |####### ______   ______  #######|
#     |###### /      \\ /      \\ #######|
#     |######|  $$$$$$|$$$$$$  |#######|
#     |######| $$ | $$|$$ | $$ |#######|
#     |######| $$ | $$|$$ | $$ |#######|
#     |######| $$__/ $$| $$__/  |#######|
#     |###### \\$$    $$| $$     |#######|
#     |####### \\$$$$$$ | $$$$$$ |#######|
#     |########################### ######|
#     |########################### ######|
#     |### /-------------------------\\ ###|
#     \\##/                           \\##/
#       /                             \\
#      /_______________________________\\

# ''')
# import random
# roadcomp = random.choice(["left", "right"])
# print("its a trusure island game.")
# print("think you are in a island")
# road = input("enter do you wnt to go right or left:")
# xv = random.choice(["wait", "swim"])
# chest = random.choice(["red", "blue", "yellow"])
# print(xv, chest, roadcomp)
# if road == roadcomp:
#     print("you lose sharks eat you")
# elif road != roadcomp:
#     print("you are in  a small island now ")
#     b = input("do you wnt to swim into the village or wait for a boat:")
#     if b == "swim" == xv:
#         print("you lose octopus eat")
#     elif b == "wait" != xv:
#         print("now you are in a village  you have 3 doors red and blue and yellow")
#         l = input("which door do you want to go:")
#         if l == "red" or "blue" or "yellow" == chest:
#             print("you won")
#         elif l == "blue" or "red " or "yellow" != chest:
#             print("you lost")
#         else:
#             print("you won the game and you won a tesure")
#             print(''' you get a truaser chest


#         _________________________
#        /#########################\\
#       /############################\\
#      /##############################\\
#     |####### ______   ______  #######|
#     |###### /      \\ /      \\ #######|
#     |######|  $$$$$$|$$$$$$  |#######|
#     |######| $$ | $$|$$ | $$ |#######|
#     |######| $$ | $$|$$ | $$ |#######|
#     |######| $$__/ $$| $$__/  |#######|
#     |###### \\$$    $$| $$     |#######|
#     |####### \\$$$$$$ | $$$$$$ |#######|
#     |########################### ######|
#     |########################### ######|
#     |### /-------------------------\\ ###|
#     \\##/                           \\##/
#       /                             \\
#      /_______________________________\\

# ''')
# import random
# b=input("head or tail")
# c=random.choice(["head","tail"])
# if b==c:
#     print("that was a tie"
#           )
# elif b=="head" and c=="tail":
# import random
# number=random.randint(1,5)
# user=int(input("enter yor number t :"))
# if
# city_of_bd = ["dhaka", "london", "barishal", "chittogong"]
# a = city_of_bd[3] = "dhaka"
# print(city_of_bd)
# print(a)

# import random
# print("WELCOME TO THE WHO IS PAY THE BILL CALCULATOR")
# name1 = input("Enter your members name:")
# a = len(name1)
# # v = print(a)
# name12 = name1.split(", ")
# comp = random.randint(0, a-1)
# person = name1[comp]
# print(f"{person} IS GOING TO PAY THE MEAL")
# import random

# print("WELCOME TO THE WHO WILL PAY THE BILL CALCULATOR")

# # Input names separated by commas
# names = input("Enter your members' names separated by commas: ")

# # Split the input string into a list of names
# name_list = names.split(", ")

# # Get the length of the list
# length_of_list = len(name_list)

# # Select a random index from the list
# random_index = random.randint(0, length_of_list - 1)

# # Get the name of the person who will pay
# person = name_list[random_index]

# print(f"{person} IS GOING TO PAY THE MEAL")
# import random

# print("WELCOME TO THE WHO WILL PAY THE BILL CALCULATOR")

# # Input names separated by commas
# names = input("Enter your members' names separated by commas: ")

# # Split the input string into a list of names
# name_list = names.split(", ")

# # Check if the list is empty
# if not name_list or all(name.strip() == "" for name in name_list):
#     print("No valid names entered. Please try again.")
# else:
#     # Select a random index from the list
#     random_index = random.randint(0, len(name_list) - 1)

#     # Get the name of the person who will pay
#     person = name_list[random_index].strip()

#     print(f"{person} IS GOING TO PAY THE MEAL")
# import random
# user = input("enter your name:")
# c = random.choices([user])
# print(c)
# 🚨 Don't change the code below 👇
# import random
# user = int(input("Enter 0 for rock 1 for paper 2 for siscor :"))
# comp = random.randint(0, 2)
# print(f"computer chose {comp}")
# print(f"you chose {user}")

# if user == comp:
#     print("That was a tie")
# if user == comp:
#     ("That was a tie")

# elif user == 0 and comp == 1:
#     print('''you chose:
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ''')
#     print('''comp chose:
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# ''')
#     print("computer win")
# elif user == 1 and comp == 2:
#     print('''you chose:
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# ''')
#     print(''' you chose:
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# ''')
#     print("you  lost")
# elif user == 2 and comp == 1:
#     print(''' you chose:
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# ''')
#     print('''comp chose:
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# ''')
#     print("you  win")

# elif user == 2 and comp == 0:
#     print(''' comp chose:
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# ''')
#     print('''computer chose:
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#           )
#     print("you  lose")
# elif user == 0 and comp == 2:
#     print('''you chose:
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)

# ''')
#     print(''' comp chose:
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# ''')
#     print("you  win")
# elif user == 1 and comp == 0:
#     print('''you chose:
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#           )
#     print(''' comp chose:
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ''')
#     print("you  lost")
# elif user == 2 and comp == 0:
#     print(''' you chose:
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#           )
#     print(''' comp chose:
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#           )
#     print("you  win")
#     print(f"computer chose {comp}")
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# totalheight = 0
# for height in student_heights:
#     totalheight += height
#     print(totalheight)
# number = 0
# for student in student_heights:
#     number += 1
#     print(number)
# avarage = round(totalheight/number)
# print(avarage)
# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
# student_scores = [20, 40, 30]
# # Write your code below this row 👇
# highschore = 0
# for i in student_scores:
#     if i > highschore:
#         highschore = i
# print(f"the highest schore is {highschore} ")
# for i in range(1, 200):
#     print(i)
# a = int(input("Enter your first digit to start"))
# b = int(input("Enter your last digit to end"))
# for i in range(a, b):

#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} is an fizz an buzz number")

#     elif i % 3 == 0:
#         print(f"{i} is an fizz number")
#     elif i % 5 == 0:
#         print(f"{i} is an buzz number")
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)
# def my_function():
#     a = ("hello ")
#     b = ("Rishan Koiry ...")
#     print(a + b)


# my_function()
# print("This is a luck game ")
'''
def moveing():
    move()


def turn_right():
    turn_left()


def turn_righ():
    turn_left()
    turn_left()
    turn_left()



moveing()
turn_right()
moveing()
turn_righ()
moveing()
turn_righ()
moveing()

turn_right()
moveing()
turn_right()
moveing()
turn_righ()
moveing()
turn_righ()
moveing()
turn_right()
moveing()
turn_right()
moveing()
turn_righ()
moveing()
turn_righ()
moveing()
turn_right()
moveing()
turn_right()
moveing()
turn_righ()
moveing()
turn_righ()
moveing()
turn_right()
moveing()
turn_right()
moveing()
turn_righ()
moveing()
turn_righ()
moveing()
turn_right()
moveing()
turn_right()
moveing()

turn_righ()
moveing()
turn_righ()
moveing()

'''

# i = 0


# def maxNum1(maxNum):

#     for i in (maxNum):
#         if i > maxNum:
#             maxNum = i


# maxNum([3, 2, 4, 3])
# numbers = [1, 2, 3, 4, -3, -3, -2, -100, 100]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
# print(positive_number_count)
# n = int(input("Enter your number:"))
# # even_number = 0
# # for i in range(n):
# #     if i % 2 == 0:
# #         even_number += 1
# # print(f"even number is {even_number}")
# for i in range(n, 11):
#     v = (n, "x", i, '=', n*i)
#     print(v)
# n = 10
# n1 = int(input("enter your len"))
# for i in range(n, n1):
#     x = (f"{n}X{i}={n*i}")
#     print(x)
# a = "teethacacd"
# for char in a:
#     print(char)
#     if a.count(char) == 1:
#         print("char is:", char)
#         break
# numb = 5
# fac = 1
# while numb > 0:
#     fac *= numb
#     numb = numb-1
# print(fac)
# for i in range(2, 100):
#     if i > 1:
#         if i % i == 0:
#             print(f" {i} is a prime number")
#             break

# print(i)
# colour = ["blur", "yellow", "pink"]
# for i in colour:
#     print(i)
# for i in range(1, 20, 2):

#     print(i)

# import random
# user = input("Enter a alphabet  :").lower()
# word = ["ardavark", "baboon", "camel"]
# comp = random.choice(word)
# for letter in cn = int(input("enter your number:"))
# n = int(input("enter :"))
# is_prime = True

# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print("The number is a prime number")
# else:
#     print("The number is not a prime number")
# # Hello World!!
# Hello World!!
# Hello World!!
# Hello World!!


# import random
# word_list = ["apple", "mango ", "banana"]
# comp = random.choice(word_list)
# print(f"The soloution is {comp}")
# display = []
# word_len = len(comp)
# for _ in range(word_len):
#     display += "_"

# print(display)
# guess = input("Enter a Letter:").lower()
# for position in range(word_len):
#     letter = comp[position]
#     if letter == guess:
#         display[position] = letter
# print(display)
# if "_" not in display:
#     end_of_game = True
#     print("You win")

# for i in range(1,100):
#     print(i)
# for i in range(100, 1):

#     print(i)
# n = 5
# sum = 0
# for i in range(1, n+1):
#     print(i)
#     sum += 1
# print(sum)
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= 1
#     print(f"factorial is {fact}")
# name = (input("enter your name:"))
# m = 0
# while m <= 10:
#     print(f"{name}")
#     m += 1
# number = int(input("Enter your number to print table:\n"))
# plus = 1
# while plus <= 10:
#     print(f" {number} X {plus} = {number*plus}")
#     plus += 1
#     break
# else:
# #     print("Here is your multipicaton table")
# for i in range(1, 10):
#     i += 1
#     print(i)
# m = int(input("Enter your number:\n\n"))b
# for i in range(-1, m):
#     m -= 1
#     print(i)
# for i in range(1, 100):
#     i += 1
#     if i % 3 == 0:
#         print(i)
# year = [2012, 2013, 2024]
# for i in year:
#     if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
#         print(f" {i} is a leap year. ")

#     else:
#         print(f" {i} is not a leap year")
# year = [2012, 2013, 2024]
# leap_years = []
# not_leap_years = []
# for i in year:
#     if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
#         leap_years.append(i)
#     else:
#         not_leap_years.append(i)
# print("Not leap year:", not_leap_years)
# print("Leap years:", leap_years)
# a = 10
# b = 10


# def cal(a, b):
#     summ = a+b
#     print(summ)


# cal(1, 2)

# def avg(a):
#     divide = a/2
#     print(divide)


# avg(10)
# avg(3)
# print("rishan", end="")
# print("koiry")
# number = [1, 2, 3, 4, 5, 5, 6, 8]


# def lenth_of_Number(list):
#     print(len(list))


# lenth_of_Number(number)
# n = 10

# b = 1


# def factorial(n):
#     for i in range(b, n):
#         print(1*n)
#         b += 1


# factorial(b,n)
# money = int(input("Enter your money  : "))


# def converter():
#     convert = (money*110)
#     print(convert)


# converter()
# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
# for i in range(2, 100):
#     if i % 1 == 0:
#         break
#     else:
#         print(i)


# import random
# word_list = ["apple", "mango ", "banana"]
# comp = random.choice(word_list)
# print(f"The soloution is {comp}")
# display = []
# word_len = len(comp)
# for _ in range(word_len):
#     display += "_"
#     end_of_game = False
# print(display)


''''''
# import random
# fruits = ["ardvark", "boboon", "camel"]
# com_chose = random.choice(fruits)
# user = input("Enter a letter \n:").lower()
# for i in com_chose:
#     if i == user:
#         print("Right")
#     else:
#         print("Wrong")
# print(com_chose)
'''day 4 solution'''
# import random
# end_of_game = False

# word_list = ["apple", "mango ", "banana"]
# comp = random.choice(word_list)
# print(f"The soloution is {comp}")
# display = []
# word_len = len(comp)
# for _ in range(word_len):
#     display += "_"

# print(display)
# while not end_of_game:
#     guess = input("Enter a Letter:").lower()
#     for position in range(word_len):
#         letter = comp[position]
#         if letter == guess:
#             display[position] = letter
#     print(display)
#     if "_" not in display:
#         end_of_game = True
#         print("you win")

# import random
# end_of_game = False
# lives = 6

# word_list = ["apple", "mango", "banana"]
# comp = random.choice(word_list)
# print(f"The solution is {comp}")
# display = []
# word_len = len(comp)
# for _ in range(word_len):
#     display += "_"

# print(display)
# while not end_of_game:
#     guess = input("Enter a letter: ").lower()
#     for position in range(word_len):
#         letter = comp[position]
#         if letter == guess:
#             display[position] = letter
#     if guess not in comp:
#         lives -= 1
#         print(f"you lost a live you have {lives} lives")
#         while lives == 0:
#             end_of_game = True
#             print("You lose")
#             break
#     print(display)
#     if "_" not in display:
#         end_of_game = True
#         print("You win!")

# import random
# comp = random.randint(1, 5)
# print(comp)
# user = int(input("Guess a number :"))
# user1 = int(input("Guess a number :"))
# user2 = int(input("Guess a number :"))
# user3 = int(input("Guess a number :"))
# user4 = int(input("Guess a number :"))
# if user == comp or user1 == comp or user2 == comp or user3 == comp or user4 == comp:
#     print("you win")
# elif


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''
# word_list = [
#     'abruptly',
#     'absurd',
#     'abyss',
#     'affix',
#     'askew',
#     'avenue',
#     'awkward',
#     'axiom',
#     'azure',
#     'bagpipes',
#     'bandwagon',
#     'banjo',
#     'bayou',
#     'beekeeper',
#     'bikini',
#     'blitz',
#     'blizzard',
#     'boggle',
#     'bookworm',
#     'boxcar',
#     'boxful',
#     'buckaroo',
#     'buffalo',
#     'buffoon',
#     'buxom',
#     'buzzard',
#     'buzzing',
#     'buzzwords',
#     'caliph',
#     'cobweb',
#     'cockiness',
#     'croquet',
#     'crypt',
#     'curacao',
#     'cycle',
#     'daiquiri',
#     'dirndl',
#     'disavow',
#     'dizzying',
#     'duplex',
#     'dwarves',
#     'embezzle',
#     'equip',
#     'espionage',
#     'euouae',
#     'exodus',
#     'faking',
#     'fishhook',
#     'fixable',
#     'fjord',
#     'flapjack',
#     'flopping',
#     'fluffiness',
#     'flyby',
#     'foxglove',
#     'frazzled',
#     'frizzled',
#     'fuchsia',
#     'funny',
#     'gabby',
#     'galaxy',
#     'galvanize',
#     'gazebo',
#     'giaour',
#     'gizmo',
#     'glowworm',
#     'glyph',
#     'gnarly',
#     'gnostic',
#     'gossip',
#     'grogginess',
#     'haiku',
#     'haphazard',
#     'hyphen',
#     'iatrogenic',
#     'icebox',
#     'injury',
#     'ivory',
#     'ivy',
#     'jackpot',
#     'jaundice',
#     'jawbreaker',
#     'jaywalk',
#     'jazziest',
#     'jazzy',
#     'jelly',
#     'jigsaw',
#     'jinx',
#     'jiujitsu',
#     'jockey',
#     'jogging',
#     'joking',
#     'jovial',
#     'joyful',
#     'juicy',
#     'jukebox',
#     'jumbo',
#     'kayak',
#     'kazoo',
#     'keyhole',
#     'khaki',
#     'kilobyte',
#     'kiosk',
#     'kitsch',
#     'kiwifruit',
#     'klutz',
#     'knapsack',
#     'larynx',
#     'lengths',
#     'lucky',
#     'luxury',
#     'lymph',
#     'marquis',
#     'matrix',
#     'megahertz',
#     'microwave',
#     'mnemonic',
#     'mystify',
#     'naphtha',
#     'nightclub',
#     'nowadays',
#     'numbskull',
#     'nymph',
#     'onyx',
#     'ovary',
#     'oxidize',
#     'oxygen',
#     'pajama',
#     'peekaboo',
#     'phlegm',
#     'pixel',
#     'pizazz',
#     'pneumonia',
#     'polka',
#     'pshaw',
#     'psyche',
#     'puppy',
#     'puzzling',
#     'quartz',
#     'queue',
#     'quips',
#     'quixotic',
#     'quiz',
#     'quizzes',
#     'quorum',
#     'razzmatazz',
#     'rhubarb',
#     'rhythm',
#     'rickshaw',
#     'schnapps',
#     'scratch',
#     'shiv',
#     'snazzy',
#     'sphinx',
#     'spritz',
#     'squawk',
#     'staff',
#     'strength',
#     'strengths',
#     'stretch',
#     'stronghold',
#     'stymied',
#     'subway',
#     'swivel',
#     'syndrome',
#     'thriftless',
#     'thumbscrew',
#     'topaz',
#     'transcript',
#     'transgress',
#     'transplant',
#     'triphthong',
#     'twelfth',
#     'twelfths',
#     'unknown',
#     'unworthy',
#     'unzip',
#     'uptown',
#     'vaporize',
#     'vixen',
#     'vodka',
#     'voodoo',
#     'vortex',
#     'voyeurism',
#     'walkway',
#     'waltz',
#     'wave',
#     'wavy',
#     'waxy',
#     'wellspring',
#     'wheezy',
#     'whiskey',
#     'whizzing',
#     'whomever',
#     'wimpy',
#     'witchcraft',
#     'wizard',
#     'woozy',
#     'wristwatch',
#     'wyvern',
#     'xylophone',
#     'yachtsman',
#     'yippee',
#     'yoked',
#     'youthful',
#     'yummy',
#     'zephyr',
#     'zigzag',
#     'zigzagging',
#     'zilch',
#     'zipper',
#     'zodiac',
#     'zombie',
# ]
