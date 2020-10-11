#!/usr/bin/env python

# imports
from PIL import Image
from sys import argv
import re
import os


# constants
UPSCALE_RES = 2160
SCALE_MODE = Image.NEAREST
RUN_PATH = './'
EP_PATH = None


def main():
    # check if dir exists
    if not os.path.isdir(EP_PATH):
        exit(f'path not found\n{EP_PATH}')

    for file in os.listdir(EP_PATH):
        if file.endswith('.png'):
            resize_img(f'{EP_PATH}{file}', file)
            # file_path = './ep_0/ep_0_title.png'
            # file_name - 'ep_0_title.png'


def scale_to_height(dimensions, height):
    width = int((height * dimensions[0]) / dimensions[1])

    return (width, height)


def resize_img(file_path, file_name):
    # file_path = './ep_0/ep_0_title.png'
    # file_name - 'ep_0_title.png'
    print(f'processing {file_name}')

    # check if resized dir exists
    if not os.path.exists(f'{EP_PATH}resized/'):
        os.makedirs(f'{EP_PATH}resized/')
    
    with Image.open(file_path) as img:
        print('   file opened')

        # replace 'ep_0_title.png' with 'ep_0_title'
        file_name = file_name.replace('.png', '')

        # resize image
        img = img.resize(scale_to_height(img.size, UPSCALE_RES), SCALE_MODE)
        print('   file resized')

        # saving resized image
        img.save(f'{EP_PATH}resized/{file_name}_2160.png')
        print('   file saved')

    print('   file closed')


if __name__ == "__main__":
    print('hello')
    print(os.path.dirname(RUN_PATH))

    print('-' * 10)
    for file in os.listdir(RUN_PATH):
        if re.search(r'^ep_', file):
            print(file)
    print('-' * 10)

    ep = 'ep_' + input('episode: ep_')
    EP_PATH = RUN_PATH + ep + '/'

    main()