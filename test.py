import imp
from bs4 import BeautifulSoup
import requests
import lxml
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep


url = "https://yandex.ru/images/search?text=zebra"
r = requests.get(url);
r.text
soup = BeautifulSoup(r.text, "lxml")
zebra = soup.findAll('img', class_='serp-item__thumb justifier__thumb')
zebra = zebra + zebra
print(len(zebra))
while(array <= 1000)
