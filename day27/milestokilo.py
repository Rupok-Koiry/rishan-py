# import turtle
# screen = turtle.Screen()
# screen.title("Miles to Kilometer")
# screen.setup(width=600, height=600)
# turtle.hideturtle()

# miles_input = screen.textinput("Miles to Kilometer", "Enter miles to convert:")
# miles = float(miles_input)
# km = miles * 1.60934


# turtle.write(f"{miles} miles = {km} kilometers",
#              align="center", font=("Arial", 16, "normal"))


# with open("day27\data.txt", "w") as file:
#     file.write(f"{miles} miles = {km} kilometers\n")
#     file.close()

# screen.exitonclick()
# import tkinter as tk
# from tkinter import simpledialog


# def get_user_input():
#     user_name = simpledialog.askstring("Input", "What is your name?")

#     if user_name:
#         label.config(text=f"Hello, {user_name}!")

#         with open("day27\\name.txt", "a") as file:
#             file.write(user_name + "\n")


# window = tk.Tk()
# window.minsize(width=500, height=400)
# window.title("My first GUI program")


# label = tk.Label(window, text="Welcome!", font=("Arial", 50, "bold"))
# label.pack(expand=True)
# get_user_input()

# window.mainloop()
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
# deposit=int("how much you want to deposit")
# withdrow=int(input("how much you want withdraw:"))
# show=int("")
# class bank:
#    def__init__(deposit,withdrow,show)
# def add(*args):
#     for i in args:
#         sum += i
#     return sum


# add(1, 2, 3, 4, 5, -6)
# class Bank:
#     def __init__(self, name, deposit):
#         self.name = name
#         self.balance = deposit

#     def deposit_money(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")

#     def withdraw_money(self, amount):
#         if amount > self.balance:
#             print(f"Insufficient funds. You have {
#                   self.balance} in your account.")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. New balance: {self.balance}")

#     def show_balance(self):
#         print(f"Current balance: {self.balance}")


# name = input("Enter your name: ")
# initial_deposit = int(input("How much do you want to deposit initially: "))

# account = Bank(name, initial_deposit)

# while True:
#     action = input(
#         "Choose an action: deposit (d), withdraw (w), show balance (s), or quit (q): ").lower()

#     if action == 'd':
#         amount = int(input("Enter deposit amount: "))
#         account.deposit_money(amount)

#     elif action == 'w':
#         amount = int(input("Enter withdrawal amount: "))
#         account.withdraw_money(amount)

#     elif action == 's':
#         account.show_balance()

#     elif action == 'q':
#         print("Thank you for banking with us!")
#         break

#     else:
#         print("Invalid action. Please choose again.")
# from tkinter import *
# window = Tk()
# window.title("gui program")
# window .minsize(width=600, height=600)
# my = Label(text="I am a label", font=("Arial", 24, "bold"))
# my.pack()


# def clicked():
#     my = Label(text="I am clicked ", font=("Arial", 24, "bold"))
#     my.pack()


# buttton = Button(text="click me", command=clicked)
# buttton.pack()
# window.mainloop()
# a = (input(""))
# b = bin(a)
# print(b)
# import tkinter as tk
# from tkinter import font


# def miles_to_km():
#     miles = float(miles_input.get())
#     km = miles * 1.60934
#     km_result_label.config(text=f"{km:.2f}")


# window = tk.Tk()
# window.title("Miles to Kilometers Converter")
# window.minsize(width=100, height=200)

# bold_font = font.Font(weight="bold", size=14)

# miles_label = tk.Label(text="Miles:", font=bold_font)
# miles_label.grid(column=0, row=0, padx=10, pady=10)

# miles_input = tk.Entry(width=10, font=bold_font)
# miles_input.grid(column=1, row=0, padx=10, pady=10)

# equal_label = tk.Label(text="is equal to", font=bold_font)
# equal_label.grid(column=0, row=1, padx=10, pady=10)

# km_result_label = tk.Label(text="0", font=bold_font)
# km_result_label.grid(column=1, row=1, padx=10, pady=10)

# km_label = tk.Label(text="Km", font=bold_font)
# km_label.grid(column=2, row=1, padx=10, pady=10)

# convert_button = tk.Button(text="Convert", command=miles_to_km, font=bold_font)
# convert_button.grid(column=1, row=2, padx=10, pady=20)

# window.mainloop()
