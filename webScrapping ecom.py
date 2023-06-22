import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/s?k=iphone&crid=17V4LXM4TBXSS&sprefix=iphon%2Caps%2C509&ref=nb_sb_noss_2"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}

r = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

data = {'Title': [], 'Price': []}

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select('span.a-price')

for span in spans:
    print(span.string)
    data["Title"].append(span.string)

for price in prices : 
    if not("a-text-price" in price.get("class")): 
        print(price.find("span").get_text())
        data["Price"].append(price.find("span").get_text())
        if len(data["Price"])==len(data["Title"]) :
            break

df = pd.DataFrame.from_dict(data)
df.to_excel("data.xlsx", index=False)