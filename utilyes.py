from bs4 import BeautifulSoup
import requests
import lxml
import os
from time import sleep



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


def create_dir(src):
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    if not os.path.exists(f'dataset/{src}'):
        os.mkdir(f'dataset/{src}')


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
