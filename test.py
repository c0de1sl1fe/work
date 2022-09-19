
import os
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


def CreateUrl(request, link = 'https://yandex.ru/images/search?text='):
    return link + request.replace(' ', '%20')

    
print("test")
str = "t t"
print(CreateUrl(str))