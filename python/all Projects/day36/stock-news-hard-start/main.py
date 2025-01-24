import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "9W7H29KULHHSG7RO"
NEWS_API_KEY = "3b8c0b1ac3ec4ca39d60b3d3d0b207e8"

# Email credentials
EMAIL = "koiryrishan1@gmail.com"  # Replace with your email
PASSWORD = "pplp lrem kdjg fumg"  # Replace with your email password
TO_EMAIL = "koiryrishan1@gmail.com"  # Replace with the recipient's email

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Fetch stock data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)

if response.status_code == 200:
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_closing = float(data_list[0]["4. close"])
    day_before_closing = float(data_list[1]["4. close"])

    price_difference = abs(yesterday_closing - day_before_closing)
    percentage_diff = (price_difference / yesterday_closing) * 100

    up_down_symbol = "🔺" if yesterday_closing > day_before_closing else "🔻"
else:
    print("Failed to fetch stock data.")
    exit()

# Fetch news articles
news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)

message_body = f"TSLA: {up_down_symbol}{round(percentage_diff, 2)}%"

if news_response.status_code == 200 and "articles" in news_response.json():
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    for article in three_articles:
        headline = article["title"]
        description = article["description"]
        message_body += f"\nHeadline: {headline}\nBrief: {description}"

else:
    message_body += "\nNo recent news articles found."

# Send an email with the stock information
email_subject = f"Stock Update for {STOCK_NAME}"
email_body = message_body

msg = MIMEMultipart()
msg['From'] = EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body, 'plain'))

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")

# Optionally, you can also check the price difference threshold
if percentage_diff < 5:
    print("Stock price change is less than 5%. No news sent.")
