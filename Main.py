#Yamel Hernandez
#80590552
#CS 2302
#Diego Aguirre
#Lab 1
#Purpose of this lab was to understand recursion & 
#how to implement it using machine learning in ver A

import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


##############################################################
def process_dir(path):
    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    #my code
    for fPath in file_list:
        if classify_pic(fPath) > .5: #seperates the pictures & adds to proper array
            dog_list.append(fPath)
        else:
            cat_list.append(fPath)
    
    if not dir_list: 
        #print("in the thing")
        return cat_list, dog_list
    
    for dL in dir_list:
        print(str(path+"/"+dL)) #prints path
        cl, dl = process_dir(str(path+"/"+dL))#processes the path again and etends the lists
        cat_list.extend(cl)
        dog_list.extend(dl)

    return cat_list, dog_list
###############################################################

def main():
    start_path = '/home/yamel/Desktop/CS3/1.1 CatsDogs' # current directory

    process_dir(start_path)


main()