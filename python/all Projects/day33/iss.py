# import smtplib
# import tkinter as tk
# from tkinter import messagebox


# def send_email():
#     sender_email = sender_entry.get()
#     receiver_email = receiver_entry.get()
#     subject = subject_entry.get()
#     message_body = message_text.get("1.0", "end-1c")
#     text = f"Subject: {subject}\n\n{message_body}".encode("utf-8")

#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.ehlo()
#         server.starttls()
#         server.ehlo()

#         password = "pplp lrem kdjg fumg"
#         server.login(sender_email, password)

#         server.sendmail(sender_email, receiver_email, text)
#         messagebox.showinfo("Success", "Email sent successfully!")

#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to send email: {e}")
#     finally:
#         server.quit()


# window = tk.Tk()
# window.title(
#     "Send Email to another account for weather so the person dont forget the umbrella.☔")

# tk.Label(window, text="Sender Email:").grid(row=0, column=0)
# sender_entry = tk.Entry(window, width=50)
# sender_entry.insert(0, "koiryrishan1@gmail.com")
# sender_entry.grid(row=0, column=1)

# tk.Label(window, text="Receiver Email:").grid(row=1, column=0)
# receiver_entry = tk.Entry(window, width=50)
# receiver_entry.grid(row=1, column=1)

# tk.Label(window, text="Subject:").grid(row=2, column=0)
# subject_entry = tk.Entry(window, width=50)
# subject_entry.grid(row=2, column=1)

# tk.Label(window, text="Message:").grid(row=3, column=0)
# message_text = tk.Text(window, height=10, width=50)
# message_text.grid(row=3, column=1)

# send_button = tk.Button(window, text="Send Email", command=send_email)
# send_button.grid(row=4, column=1)

# window.mainloop()
