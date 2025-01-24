# num=int(input("Enter your number: "))
# if num%2==0:
#   print("Even")
# else:
#   print('Odd')
# year = int(input("Enter the year: "))
# if (year % 400 == 0):
#     print("Leap Year")

# else:
#     if (year % 4 == 0 and year % 100 != 0):
#         print('Leap Year')
#     else:
#         print("Not a Leap Year")
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# bill = 0
# if size == 'S':
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
# else:
#     if size == 'M':
#         bill = 20
#     elif size == 'L':
#         bill = 25
#     if add_pepperoni == 'Y':
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1

# print(f"${bill}")
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# combine = name1.lower()+name2.lower()
# t = combine.count('t')
# r = combine.count('r')
# u = combine.count('u')
# e = combine.count('e')
# true = t+r+u+e
# l = combine.count('l')
# o = combine.count('o')
# v = combine.count('v')
# e = combine.count('e')
# love = l+o+v+e
# true_love = int(str(true)+str(love))
# if true_love < 10 or true_love > 90:
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif true_love > 40 and true_love < 50:
#     print(f"Your score is {true_love}, you are alright together.")

# else:
#     print(f"Your score is {true_love}.")
