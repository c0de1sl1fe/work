from utilyes import run
from time import sleep
import cv2
import numpy as np
import os

def cmp(image_1: cv2.Mat, image_2: cv2.Mat) -> bool:
  return image_1 == image_2
def fix_dataset(path_dir):
    image_11 = cv2.imread("dataset/zebra/0001.jpg")
    image_12 = cv2.imread("dataset/zebra/0002.jpg")

    i, j = 0, 0

    while():
        while():
            if(np.all(cmp(image_11, image_12) == True)):
                os.remove()
            j+=1
        
        i+=1 

if __name__ == '__main__':
    image_11 = cv2.imread("dataset/zebra/0001.jpg")
    image_12 = cv2.imread("dataset/zebra/0002.jpg")

    print()
    #print(cmp(image_11, image_12))
    