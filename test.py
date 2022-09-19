from bs4 import BeautifulSoup
import requests
import lxml

url = "https://yandex.ru/images/search?text=zebra"
r = requests.get(url);
r.text
soup = BeautifulSoup(r.text, "lxml")
zebra = soup.findAll('img', class_='serp-item__thumb justifier__thumb')
print(len(zebra))