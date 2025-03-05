import requests
import os
import smtplib
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
SENDING_TO = os.environ["SENDING_TO"]

response = requests.get(url = URL)

soup = BeautifulSoup(response.text, features="html.parser")
price_complete =soup.find(name="span", class_="aok-offscreen").getText()
price = price_complete.split("$")
product_price = price[1]

with smtplib.SMTP("smtp.gmail.com") as connection:
     connection.starttls()
     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
     connection.sendmail(from_addr=MY_EMAIL,
                         to_addrs=SENDING_TO,
                         msg=f"Subject:Amazon Price Alert!\n\nThe 'Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Saute, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart' is now ${product_price}!\n{URL}")

