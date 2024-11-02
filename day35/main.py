import smtplib
import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "ce476299ce914a40b32132837240310"
PASSWORD = "pplp lrem kdjg fumg"


def send_email(receiver_email, subject, message):
    sender_email = "koiryrishan1@gmail.com"
    text = f"Subject: {subject}\n\n{message}".encode("utf-8")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, PASSWORD)
        server.sendmail(sender_email, receiver_email, text)
        messagebox.showinfo("Success", "Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Failed to login. Check credentials.")
    except smtplib.SMTPConnectError:
        messagebox.showerror("Error", "Failed to connect to the server.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")
    finally:
        server.quit()


def check_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    weather_data = response.json()

    temperature = weather_data["current"]["temp_c"]
    wind_speed = weather_data["current"]["wind_kph"]
    condition = weather_data["current"]["condition"]["text"]
    rain = "rain" in condition.lower()

    emoji = ""
    if rain:
        emoji = "🌧️" if "heavy" in condition.lower() else "🌦️"

    weather_report = f"Weather in {city}:\nTemperature: {
        temperature}°C\nWind: {wind_speed} kph\nCondition: {condition} {emoji}"

    return weather_report, rain


def main():
    city = city_entry.get()
    receiver_email = receiver_email_entry.get()

    weather_report, rain = check_weather(city)

    if rain:
        subject = "Weather Alert: Rain Expected!"
        message = f"{weather_report}\n\nIt's going to rain today in {
            city}. Remember to bring an umbrella ☔️."
        send_email(receiver_email, subject, message)
    else:
        subject = "Weather Update"
        message = f"{weather_report}\n\nNo rain is expected today."
        send_email(receiver_email, subject, message)


root = tk.Tk()
root.title("Weather Email Alert")
root.geometry("400x300")

tk.Label(root, text="City", font=("Arial", 12)).grid(row=0, padx=10, pady=10)
tk.Label(root, text="Receiver Email", font=(
    "Arial", 12)).grid(row=1, padx=10, pady=10)

city_entry = tk.Entry(root, font=("Arial", 12))
receiver_email_entry = tk.Entry(root, font=("Arial", 12))

city_entry.grid(row=0, column=1, padx=10, pady=10)
receiver_email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Send Weather Alert", command=main, font=(
    "Arial", 12)).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
