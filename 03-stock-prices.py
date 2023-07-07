#https://finance.naver.com/item/sise.naver?code=035250,006360,036570,207940

import requests
from bs4 import BeautifulSoup

codes = ["035250","006360","036570", "207940"]
url = "https://finance.naver.com/item/sise.naver?code=%s"
prices = []

for code in codes :
    response = requests.get(url % code)

    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("strong#_nowVal")
    prices.append(price.text)
print(prices)