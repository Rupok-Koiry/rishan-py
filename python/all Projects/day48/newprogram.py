import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def fetch_news():
    country = entry.get()
    Chrome_driver_path = "C:/users/muaza gazet/Desktop/R I S H A N/devolopment/chromedriver-win64"
    
    # Setup the WebDriver
    driver = webdriver.Chrome(service=Service(Chrome_driver_path))
    driver.get(f"https://en.wikipedia.org/wiki/{country}")
    
    try:
        # Fetch the first 5 news-like articles from the Wikipedia page for the country
        articles = driver.find_elements(By.CSS_SELECTOR, "p a")
        news = "\n".join([article.text for article in articles[:5]])  # Get first 5 articles
        
        # Clear the previous results and display the new news under the country name
        result_label.config(text=news)
    except Exception as e:
        result_label.config(text="Error fetching news.")
    finally:
        driver.quit()

# Tkinter GUI Setup
root = tk.Tk()
root.title("Country Good Things")  # Set the title of the window
root.geometry("500x400")  # Set the size of the window

# Instruction label
instruction_label = tk.Label(root, text="Enter a country name to get the Country good Thing:", font=("Arial", 12))
instruction_label.pack(pady=10)

# Input field for country name
entry = tk.Entry(root, font=("Arial", 14), width=40)
entry.pack(pady=10)

# Button to fetch news
fetch_button = tk.Button(root, text="Click to see News", command=fetch_news, font=("Arial", 12))
fetch_button.pack(pady=10)

# Label to display the fetched news directly under the country name
result_label = tk.Label(root, text="", justify=tk.LEFT, font=("Arial", 12), width=60, height=10, anchor="w", relief="solid", padx=10, pady=10)
result_label.pack(pady=10)

root.mainloop()

