from bs4 import BeautifulSoup
import requests
import lxml
import os
import test
#n = 1000

#soup = BeautifulSoup(r.text, "lxml")
#zebra = soup.findAll('img', class_='serp-item__thumb justifier__thumb')

def CreateUrl(srt):
    return str.replace(' ', '%20')
    

#def getAllBlock(url):
   # r = requests.get(url)
  #  soup = BeautifulSoup(r.text, "lxml")
 #   zebra = soup.findAll('img', class_='serp-item__thumb justifier__thumb')
#    return zebra

