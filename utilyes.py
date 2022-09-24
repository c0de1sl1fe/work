from bs4 import BeautifulSoup
import requests
import lxml
import os
import test
#n = 1000

#soup = BeautifulSoup(r.text, "lxml")
#zebra = soup.findAll('img', class_='serp-item__thumb justifier__thumb')

def CreateUrl(srt):
    str.replace(' ', '%20')
    url = 'https://yandex.ru/images/search?text=' +str+ 'zebra&p=1'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    soup.find('img', class_='serp-item__thumb justifier__thumb').get('src')

#def getAllBlock(url):
   # r = requests.get(url)
  #  soup = BeautifulSoup(r.text, "lxml")
 #   zebra = soup.findAll('img', class_='serp-item__thumb justifier__thumb')
#    return zebra

