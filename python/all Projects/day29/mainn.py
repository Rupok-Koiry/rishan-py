# from tkinter import *
# from tkinter import messagebox
# import random
# import pyperclip


# def generate_password():
#     letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     numbers = '0123456789'
#     symbols = '!#$%&()*+'

#     password_letters = [random.choice(letters)
#                         for _ in range(random.randint(8, 10))]
#     password_symbols = [random.choice(symbols)
#                         for _ in range(random.randint(2, 4))]
#     password_numbers = [random.choice(numbers)
#                         for _ in range(random.randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers
#     random.shuffle(password_list)
#     password = "".join(password_list)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)


# def save_password():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()

#     if len(website) == 0 or len(password) == 0:
#         messagebox.showwarning(
#             title="Oops", message="Please make sure all fields are filled out.")
#     else:
#         try:
#             with open("all_pass.txt", "a") as file:
#                 file.write(f"{website} | {email} | {password}\n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
#                 messagebox.showinfo(
#                     title="Success", message="Password saved successfully")
#         except Exception as e:
#             messagebox.showerror(
#                 title="Error", message=f"An error occurred: {e}")


# def find_password():
#     website = website_entry.get()
#     if len(website) == 0:
#         messagebox.showwarning(
#             title="Oops", message="Please enter the website name.")
#     else:
#         try:
#             with open("all_pass.txt", "r") as file:
#                 lines = file.readlines()
#                 for line in lines:
#                     data = line.strip().split(" | ")
#                     if data[0] == website:
#                         messagebox.showinfo(title="Password Found", message=f"Email: {
#                                             data[1]}\nPassword: {data[2]}")
#                         return
#                 messagebox.showinfo(
#                     title="Not Found", message="This data is not in your program.")
#         except FileNotFoundError:
#             messagebox.showerror(
#                 title="Error", message="No data file found. Please save a password first.")
#         except Exception as e:
#             messagebox.showerror(
#                 title="Error", message=f"An unexpected error occurred: {e}")


# window = Tk()
# window.title("PASSWORD GENERATOR AND STORE")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=200, height=224)
# logo_image = PhotoImage(file="C:/Users/USER/Desktop/python/day29/logo.png")
# canvas.create_image(100, 112, image=logo_image)
# canvas.grid(row=0, column=1)

# website_label = Label(text="NAME OF THE WEBSITE:")
# website_label.grid(row=1, column=0)
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()

# email_label = Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)

# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)

# generate_button = Button(text="Generate Password", command=generate_password)
# generate_button.grid(row=3, column=2)

# add_button = Button(text="ADD", width=36, command=save_password)
# add_button.grid(row=4, column=1, columnspan=2)

# find_button = Button(text="FIND PASSWORD", width=36, command=find_password)
# find_button.grid(row=5, column=1, columnspan=2)

# window.mainloop()
