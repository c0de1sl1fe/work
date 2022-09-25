from bs4 import BeautifulSoup
import requests
import lxml
import os
from time import sleep
import shutil


def create_url(request):
    data = []
    for n in range(1, 6):
        print ("Parsing ", n+1 , " page")
        request.replace(' ', '%20')
        url = f'https://yandex.ru/images/search?text={request}&p={n}'
        r = requests.get(url)
        sleep(3)
        soup = BeautifulSoup(r.text, 'lxml')
        tmp = soup.find_all('img', class_='serp-item__thumb justifier__thumb')
        for img in tmp:
            test = 'https:' + img.get('src')
            data.append(test)
    return data



""" 
def download(img_url, img_name, img_path):
    src = requests.get(img_url)
    with open(f'{img_path}/{img_name}.jpg', 'ab') as file:
        file.write(src)
    file.close()     """




""" def get_image_url(item):
    for page in range(1, 2):
        url = f'https://yandex.ru/images/search?p={page}&text={item}'
        src = requests.get(url)
        soup = BeautifulSoup(src.text, "lxml")
        all_images = soup.find_all("a", class_="serp-item__link")
        for image in all_images:
            url_img = "https:" + image.find("img", class_="serp-item__thumb").get("src")
            yield url_img """

""" def create_dir(src):
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    os.chdir('dataset')
    if not os.path.exists(src):
        os.mkdir(src)
    oldpwd = os.getcwd()
 """
def create_dir(src):
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    if not os.path.exists(f'dataset/{src}'):
        os.mkdir(f'dataset/{src}')




""" def download_image(url_image, name, item):
    src = requests.get(url_image, stream=True)
    with open(f'{item}/{name}.jpg', 'ab') as file:
        for iteration in src.iter_content(1024**2):
            file.write(iteration)
    file.close()
 """

def download_img(img_url, img_name, img_path):
    response = requests.get(img_url)
    file = open(f"dataset/{img_path}/{img_name}.jpg", "wb")
    file.write(response.content)
    file.close()


def run(class_name):
    create_dir(class_name)
    test = create_url(class_name)
    number = 0
    for item in test:
        download_img(item, str(number).zfill(4), class_name)
        number += 1

""" def run():
    create_dir('rose')
    create_dir('tulip')

    number = 0
    for url_of_item in get_image_url("rose"):
        number += 1
        download_image(url_of_item, str(number).zfill(4), "rose")
        print(1)
        sleep(1)

    number = 0
    for url_of_item in get_image_url("tulip"):
        number += 1
        download_image(url_of_item, str(number).zfill(4), "tulip")
        print(2)
        sleep(1)
    os.chdir(oldpwd)
 """

print(1)




#def getAllBlock(url):
   # r = requests.get(url)
  #  soup = BeautifulSoup(r.text, "lxml")
 #   zebra = soup.findAll('img', class_='serp-item__thumb justifier__thumb')
#    return zebra

