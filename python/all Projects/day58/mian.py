import tkinter as tk
from tkinter import messagebox, ttk
import os
import json

class BankSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ultra Pro Max Banking System")
        self.root.geometry("600x650")
        self.root.config(bg="#f0f0f0")
        
        self.users_data = self.load_data()
        self.current_user = None
        self.create_menu()
        self.create_widgets()

    def load_data(self):
        if not os.path.exists("users_data.json"):
            return {}
        with open("users_data.json", "r") as f:
            return json.load(f)
    
    def save_data(self):
        with open("users_data.json", "w") as f:
            json.dump(self.users_data, f)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        
        # Create a menu for login/signup and other actions
        account_menu = tk.Menu(menu_bar, tearoff=0)
        account_menu.add_command(label="Login", command=self.show_login_screen)
        account_menu.add_command(label="Register", command=self.show_register_screen)
        account_menu.add_separator()
        account_menu.add_command(label="Logout", command=self.logout)
        
        menu_bar.add_cascade(label="Account", menu=account_menu)
        
        # Create a menu for other actions (like Transaction History, Deposit, Withdraw)
        action_menu = tk.Menu(menu_bar, tearoff=0)
        action_menu.add_command(label="Transaction History", command=self.show_transactions)
        action_menu.add_command(label="Deposit", command=self.deposit)
        action_menu.add_command(label="Withdraw", command=self.withdraw)
        action_menu.add_command(label="Change Password", command=self.change_password)
        
        menu_bar.add_cascade(label="Actions", menu=action_menu)
        
        # Adding the menu to the window
        self.root.config(menu=menu_bar)

    def create_widgets(self):
        self.clear_window()

        if not self.current_user:
            title_label = tk.Label(self.root, text="Welcome to Wultra Pro Max Bank", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
            title_label.pack(pady=20)
            
            self.name_label = tk.Label(self.root, text="Name:", font=("Helvetica", 12), bg="#f0f0f0")
            self.name_label.pack(pady=5)
            
            self.name_entry = tk.Entry(self.root, font=("Helvetica", 12), width=40)  # Full-width input field
            self.name_entry.pack(pady=5)
            
            self.pin_label = tk.Label(self.root, text="Pin Code:", font=("Helvetica", 12), bg="#f0f0f0")
            self.pin_label.pack(pady=5)
            
            self.pin_entry = tk.Entry(self.root, show="*", font=("Helvetica", 12), width=40)  # Full-width input field
            self.pin_entry.pack(pady=5)
            
            self.login_button = ttk.Button(self.root, text="Login", command=self.login, style="TButton")
            self.login_button.pack(pady=10)
            
            self.register_button = ttk.Button(self.root, text="Register", command=self.register, style="TButton")
            self.register_button.pack(pady=10)

    def show_login_screen(self):
        self.clear_window()
        self.create_widgets()

    def show_register_screen(self):
        self.clear_window()
        self.create_widgets()

    def login(self):
        name = self.name_entry.get()
        pin = self.pin_entry.get()

        if name in self.users_data and self.users_data[name]['pin'] == pin:
            self.current_user = name
            self.name_entry.config(state="disabled")
            self.pin_entry.config(state="disabled")
            self.login_button.config(state="disabled")
            self.register_button.config(state="disabled")
            self.show_account_screen()
        else:
            messagebox.showwarning("Login Failed", "Invalid username or PIN.")

    def register(self):
        name = self.name_entry.get()
        pin = self.pin_entry.get()

        if name in self.users_data:
            messagebox.showwarning("Already Registered", "User already exists. Please log in.")
            return

        if name and pin:
            self.users_data[name] = {
                "pin": pin,
                "balance": 0,
                "transactions": []
            }
            self.save_data()
            messagebox.showinfo("Registration Successful", f"Account for {name} created successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid name and PIN.")

    def show_account_screen(self):
        self.clear_window()
        
        self.balance_label = tk.Label(self.root, text=f"Balance: ${self.users_data[self.current_user]['balance']}", font=("Helvetica", 14), bg="#f0f0f0")
        self.balance_label.pack(pady=10)
        
        self.deposit_button = ttk.Button(self.root, text="Deposit", command=self.deposit, style="TButton")
        self.deposit_button.pack(pady=5)
        
        self.withdraw_button = ttk.Button(self.root, text="Withdraw", command=self.withdraw, style="TButton")
        self.withdraw_button.pack(pady=5)
        
        self.transaction_history_button = ttk.Button(self.root, text="Transaction History", command=self.show_transactions, style="TButton")
        self.transaction_history_button.pack(pady=5)
        
        self.change_password_button = ttk.Button(self.root, text="Change Password", command=self.change_password, style="TButton")
        self.change_password_button.pack(pady=5)
        
        self.logout_button = ttk.Button(self.root, text="Logout", command=self.logout, style="TButton")
        self.logout_button.pack(pady=5)

    def deposit(self):
        amount = self.prompt_for_amount("Deposit")
        if amount:
            self.users_data[self.current_user]["balance"] += amount
            self.users_data[self.current_user]["transactions"].append(f"Deposited: ${amount}")
            self.save_data()
            self.update_balance()

    def withdraw(self):
        amount = self.prompt_for_amount("Withdraw")
        if amount and amount <= self.users_data[self.current_user]["balance"]:
            self.users_data[self.current_user]["balance"] -= amount
            self.users_data[self.current_user]["transactions"].append(f"Withdrew: ${amount}")
            self.save_data()
            self.update_balance()
        elif amount > self.users_data[self.current_user]["balance"]:
            messagebox.showwarning("Insufficient Funds", "You don't have enough balance.")

    def prompt_for_amount(self, transaction_type):
        amount = tk.simpledialog.askinteger(f"{transaction_type} Money", f"Enter amount to {transaction_type.lower()}:")
        if amount is not None and amount > 0:
            return amount
        else:
            messagebox.showwarning("Invalid Amount", "Please enter a valid amount.")
            return None

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.users_data[self.current_user]['balance']}")

    def show_transactions(self):
        transactions = self.users_data[self.current_user]["transactions"]
        if not transactions:
            messagebox.showinfo("Transaction History", "No transactions found.")
        else:
            transaction_history = "\n".join(transactions)
            messagebox.showinfo("Transaction History", transaction_history)

    def change_password(self):
        new_pin = tk.simpledialog.askstring("Change PIN", "Enter a new PIN:")
        if new_pin and len(new_pin) == 4:
            self.users_data[self.current_user]["pin"] = new_pin
            self.save_data()
            messagebox.showinfo("Success", "PIN changed successfully!")
        else:
            messagebox.showwarning("Invalid PIN", "Please enter a valid 4-digit PIN.")

    def logout(self):
        self.current_user = None
        self.name_entry.config(state="normal")
        self.pin_entry.config(state="normal")
        self.login_button.config(state="normal")
        self.register_button.config(state="normal")
        self.clear_window()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    import tkinter.simpledialog as simpledialog
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10, width=15)
    root = tk.Tk()
    app = BankSystem(root)
    root.mainloop()
