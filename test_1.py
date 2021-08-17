import os
from typing import Set, Tuple, Dict, List

import numpy as np
import cv2

import time
from CarNumberRecognition import say_what_is_it, update_number, update_image, predict_number
from NumberFinder.ColorFinder import find_yellow
from NumberFinder.car_number_consts import get_type_of_car_number
from NumberFinder import find_coordinates_of_number_letters_american_1995, \
    find_coordinates_of_number_letters_american_2004, \
    find_coordinates_of_number_letters_american_2015, \
    find_coordinates_of_number_letters_standard_1995, \
    find_coordinates_of_number_letters_standard_2004, \
    find_coordinates_of_number_letters_standard_2015, \
    find_coordinates_of_number_letters_tractor_1995, \
    find_coordinates_of_number_letters_tractor_2004, \
    search_scope, find_blue
from test_my_threading import NumberRecognition, check_number

cv2.setLogLevel(0)

funcs_of_type = {
    1995: [
        find_coordinates_of_number_letters_standard_1995,
        find_coordinates_of_number_letters_tractor_1995,
        find_coordinates_of_number_letters_american_1995,
    ],
    2004: [
        find_coordinates_of_number_letters_american_2004,
        find_coordinates_of_number_letters_standard_2004,
        find_coordinates_of_number_letters_tractor_2004
    ],
    2015: [
        find_coordinates_of_number_letters_american_2015,
        find_coordinates_of_number_letters_standard_2015
    ]
}


def get_scopes(image):
    blue_coordinates = find_blue(image)
    yellow_coordinates = find_yellow(image)
    year = get_type_of_car_number(*blue_coordinates[2:], *yellow_coordinates[2:])
    needed_funcs = funcs_of_type[year]
    answer = {}
    for func in needed_funcs:
        type_number = "_".join(func.__name__.split('_')[-2:])
        scopes = search_scope(img, func)
        answer[type_number] = scopes
    return answer


def draw_scopes(image, scopes):
    img = image.copy()
    for i in range(len(scopes)):
        scope = scopes[i]
        x, y, width, height = (int(num) for num in scope)
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 0), 1)
    return img


def get_number(img):
    blue_coordinates: Tuple[int, int, int, int] = find_blue(img)
    x, y, width, height = blue_coordinates
    # cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 255), 1)
    yellow_coordinates: Tuple[int, int, int, int] = find_yellow(img)
    year: int = get_type_of_car_number(*blue_coordinates[2:], *yellow_coordinates[2:])
    print(year)
    needed_funcs: list = funcs_of_type[year]
    cropped_images: Dict[str, List[np.ndarray]] = {}
    for function in needed_funcs:
        cropped_images[function.__name__] = []
        scopes: List[List[int]] = search_scope(img, function)
        for scope in scopes:
            x, y, width, height = (int(num) for num in scope)
            cropped: np.ndarray = img[y:y + height, x:x + width]
            cropped_images[function.__name__].append(cropped)
    for cropped_name in cropped_images.keys():
        predict_answer = predict_number(cropped_images[cropped_name])
        answer = "".join(predict_answer)
        if check_number(year, answer):
            return year, answer
    # p = NumberRecognition(img, needed_funcs)
    # answer = p.loop()
    # return answer


if __name__ == '__main__':

    img_names = os.listdir('Input')

    for name in img_names:
        try:

            img = cv2.imread(f'Input/{name}')
            start_time = time.time()
            print(name, get_number(img))
            print("--- %s seconds ---" % (time.time() - start_time))
        except:
            print(name, 'error')
    # img_names = os.listdir('Input')
    # for name in img_names:
    #     if not 'american_1995' in name:
    #         continue
    #     img = cv2.imread(f'Input/{name}')
    #     # print(get_number(img))
    #     scopes = get_scopes(img)
    #     for _name in scopes.keys():
    #         cv2.imshow(name + _name, draw_scopes(img, scopes[_name]))
    # cv2.waitKey(0)
