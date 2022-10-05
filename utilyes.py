import os
from time import sleep

from bs4 import BeautifulSoup
import requests
import cv2
import numpy as np
import os.path


def cmp(image_1: cv2.Mat, image_2: cv2.Mat) -> bool:
    dsize = (400, 400)
    test_1 = cv2.resize(image_1, dsize)
    test_2 = cv2.resize(image_2, dsize)
    return test_1 == test_2


def remove_duplicate_slow(path_dir):
    path = f'dataset/{path_dir}'
    del_arr = []
    names = os.listdir(path)
    for filename1 in names:
        del_arr = []
        for filename2 in names:
            img_1 = cv2.imread(f'{path}/{filename1}')
            img_2 = cv2.imread(f'{path}/{filename2}')
            if np.all(cmp(img_1, img_2) == True) and filename1 != filename2:
                print("DUblicate: ", filename1, " and ", filename2)
                os.remove(f'{path}/{filename2}')
                del_arr.append(filename2)
        print(filename1)
        for i in del_arr:
            print('to delete  ', i)
            names.remove(i)


def remove_duplicate_fast(path_dir):
    if os.path.isdir(f'dataset/{path_dir}'):
        path = f'dataset/{path_dir}'
        names = os.listdir(path)
        i, j = 0, 0
        length_names = len(names)
        while i < length_names:
            j = i
            while j < length_names:
                img_1 = cv2.imread(f'{path}/{names[i]}')
                img_2 = cv2.imread(f'{path}/{names[j]}')
                if np.all(cmp(img_1, img_2) == True) and i != j:
                    print("DUblicate: ", names[i], " and ", names[j])
                    os.remove(f'{path}/{names[j]}')
                j += 1
            print(names[i])
            names = os.listdir(path)
            length_names = len(names)
            i += 1


def create_url(request):
    data = []

    for n in range(1, 6):
        print("Parsing ", n, " page")
        request.replace(' ', '%20')
        url = f'https://yandex.ru/images/search?text={request}&p={n + 35}'
        r = requests.get(url)
        sleep(1)
        soup = BeautifulSoup(r.text, 'lxml')
        tmp = soup.find_all('img', class_='serp-item__thumb justifier__thumb')
        for img in tmp:
            tmp_url = 'https:' + img.get('src')
            yield (tmp_url)

        # for img in tmp:
         #   test = 'https:' + img.get('src')
          #  data.append(test)
    # return data


def create_dir(src):
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    if not os.path.exists(f'dataset/{src}'):
        os.mkdir(f'dataset/{src}')


def download_img(img_url, img_name, img_path):
    response = requests.get(img_url)
    path = os.path.join(os.path.join("dataset", img_path), f'{img_name}.jpg')
    file = open(path, "wb")
    file.write(response.content)
    file.close()


def run(class_name):
    create_dir(class_name)
    number = 0 + 1050
    for item in create_url(class_name):
        download_img(item, str(number).zfill(4), class_name)
        number += 1
        if (number % 10 == 0):
            print('downloded: ', number)
        sleep(1)
