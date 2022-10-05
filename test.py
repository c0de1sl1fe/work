from utilyes import run
from time import sleep
import cv2
import numpy as np
import os
import os.path

def cmp(image_1: cv2.Mat, image_2: cv2.Mat) -> bool:
    dsize = (400, 400)
    test_1 = cv2.resize(image_1, dsize)
    test_2 = cv2.resize(image_2, dsize)

    return test_1 == test_2
def fix_dataset(path_dir):

    if os.path.isdir(f'dataset/{path_dir}'):
        i, j = 0, 0

        path_1 = f'dataset/{path_dir}/{str(i).zfill(4)}.jpg'
        path_2 = f'dataset/{path_dir}/{str(j).zfill(4)}.jpg'
        
        while(os.path.exists(path_1)):
            path_1 = f'dataset/{path_dir}/{str(i).zfill(4)}.jpg'
            j = 0
            while(os.path.exists(path_2)):
                path_2 = f'dataset/{path_dir}/{str(j).zfill(4)}.jpg'
                img_1 = cv2.imread(path_1)
                img_2 = cv2.imread(path_2)
                    
                if np.all(cmp(img_1, img_2) == True) and i != j:
                    print("DUblicate: ", path_2)
                    os.remove(path_2)
                j+=1
                path_2 = f'dataset/{path_dir}/{str(j).zfill(4)}.jpg'
            
            i+=1
            path_1 = f'dataset/{path_dir}/{str(i).zfill(4)}.jpg'
    else:
        print("Error of exist dir")
    print(i, " ", j)


def remove_duplicate(path_dir):
    path = f'dataset/{path_dir}'
    flag = False
    exit = False
    while( not exit):
        flag = False
        names = os.listdir(path)
        inner_names = os.listdir(path)
        for filename1 in names:
            if(flag):
                break
            for filename2 in inner_names:
                if(flag):
                    break
                img_1 = cv2.imread(f'{path}/{filename1}')
                img_2 = cv2.imread(f'{path}/{filename2}')
                if np.all(cmp(img_1, img_2) == True) and filename1!=filename2:
                    print("DUblicate: ", filename1," and ", filename2)
                    os.remove(f'{path}/{filename2}')
                    flag = True
        if not flag:
            exit = True


def fix_dataset(path_dir):

    if os.path.isdir(f'dataset/{path_dir}'):
        i, j = 0, 0

        path_1 = f'dataset/{path_dir}/{str(i).zfill(4)}.jpg'
        path_2 = f'dataset/{path_dir}/{str(j).zfill(4)}.jpg'
        
        while(os.path.exists(path_1)):
            path_1 = f'dataset/{path_dir}/{str(i).zfill(4)}.jpg'
            j = 0
            while(os.path.exists(path_2)):
                path_2 = f'dataset/{path_dir}/{str(j).zfill(4)}.jpg'
                img_1 = cv2.imread(path_1)
                img_2 = cv2.imread(path_2)
                    
                if np.all(cmp(img_1, img_2) == True) and i != j:
                    print("DUblicate: ", path_2)
                    os.remove(path_2)
                j+=1
                path_2 = f'dataset/{path_dir}/{str(j).zfill(4)}.jpg'
            
            i+=1
            path_1 = f'dataset/{path_dir}/{str(i).zfill(4)}.jpg'
    else:
        print("Error of exist dir")
    print(i, " ", j)


def remove_duplicate1(path_dir):
    path = f'dataset/{path_dir}'
    flag = False
    exit = False
    while( not exit):
        flag = False
        names = os.listdir(path)
        inner_names = os.listdir(path)
        filename1 = os.listdir(path)
        while not flag:
            while not flag:
                img_1 = cv2.imread(f'{path}/{filename1}')
                img_2 = cv2.imread(f'{path}/{filename2}')
                if np.all(cmp(img_1, img_2) == True) and filename1!=filename2:
                    print("DUblicate: ", filename1," and ", filename2)
                    os.remove(f'{path}/{filename2}')
                    flag = True
        
        for filename1 in names:
            if(flag):
                break
            for filename2 in inner_names:
                if(flag):
                    break
                
        if not flag:
            exit = True



def remove_duplicate2(path_dir):
    path = f'dataset/{path_dir}'
    del_arr = []
    names = os.listdir(path)
    for filename1 in names:
        del_arr = []
        for filename2 in names:
            img_1 = cv2.imread(f'{path}/{filename1}')
            img_2 = cv2.imread(f'{path}/{filename2}')
            if np.all(cmp(img_1, img_2) == True) and filename1!=filename2:
                print("DUblicate: ", filename1," and ", filename2)
                os.remove(f'{path}/{filename2}')
                #names.remove(filename2)
                del_arr.append(filename2)
        print(filename1)
        for i in del_arr:
            print( 'to delete  ',i)
            names.remove(i)
        # names.remove(filename1)




if __name__ == '__main__':
    # remove_duplicate2('bay horse')

    remove_duplicate2('zebra')
    # path_dir = 'tiger'
    # path = f'dataset/{path_dir}'
    # filename1 = os.listdir(path)
    # print(filename1)
    #fix_dataset('bay horse')
    #print(cmp(image_11, image_12))
    