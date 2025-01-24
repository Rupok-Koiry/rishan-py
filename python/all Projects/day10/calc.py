# logo = """
#  _____________________
# |  _________________  |
# | |Python calculator | |  .----------------.  .----------------.  .----------------.  .----------------.
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
# |_____________________|
# """
# print(logo)


# def add(number1, number2):
#     return number1 + number2


# def subtract(number1, number2):
#     return number1 - number2


# def multiply(number1, number2):
#     return number1 * number2


# def divide(number1, number2):
#     if number2 != 0:
#         return number1 / number2
#     else:
#         return "Error: Division by zero is not allowed."


# def modulus(number1, number2):
#     return number1 % number2


# def calc(number1, operation, number2):
#     if operation == "+":
#         result = add(number1, number2)
#     elif operation == "-":
#         result = subtract(number1, number2)
#     elif operation == "*":
#         result = multiply(number1, number2)
#     elif operation == "/":
#         result = divide(number1, number2)
#     elif operation == "%":
#         result = modulus(number1, number2)
#     else:
#         result = "Invalid operation"
#     print(f"Result: {result}")


# number1 = int(input("Enter your First Number: "))
# symbols = ["+", "%", "*", "-", "/"]
# print("Available operations:")
# for symbol in symbols:
#     print(symbol)

# operation = input("Enter the operation you want to perform (+, -, *, /, %): ")
# number2 = int(input("Enter your Second Number: "))

# calc(number1, operation, number2)

# while True:
#     continue_game = input(
#         "Do you want to perform another calculation? (y for yes, n for no): ")
#     if continue_game.lower() == "y":
#         number1 = int(input("Enter your First Number: "))
#         operation = input(
#             "Enter the operation you want to perform (+, -, *, /, %): ")
#         number2 = int(input("Enter your Second Number: "))
#         calc(number1, operation, number2)
#     elif continue_game.lower() == "n":
#         break
#     else:
#         print("Invalid input. Please enter 'y' or 'n'.")

# years = int(input())


# def is_leap(yearss):
#     if yearss/4 and not yearss/100:
#         print("True")
#     elif yearss/400:
#         print("True")
#     else:
#         print("False")


# is_leap(years)

# Write your logic here
# a = "this program do anything you type that will be organised  by upper case letter this program is who hates capital letter type with shifts so i made that."
# b = a.title()
# print(b)
# aa = input("Enter Your Word :")
# bb = aa.title()
# print(bb)
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))


# def is_leap(year):

#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is Not a leap year")


# def days_in_month(year, month):

#     if month == 2:
#         return 29 if is_leap(year) else 28
#     elif month in [4, 6, 9, 11]:
#         return 30
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     else:
#         return "Invalid month"


# days = days_in_month(year, month)
# print(f"Number of days in month {month} of year {year}: {days}")
