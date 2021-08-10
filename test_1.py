import os

import numpy as np
from cv2 import cv2
import time
from CarNumberRecognition import say_what_is_it, update_number, update_image
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

funcs_of_type = {
    1995: [
        find_coordinates_of_number_letters_american_1995,
        find_coordinates_of_number_letters_standard_1995,
        find_coordinates_of_number_letters_tractor_1995
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


def is_number(number):
    answer = True
    for n in number[2:-2]:
        answer = answer and n in '0123456789'
    for n in number[:2]:
        answer = answer and n in 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for n in number[-2:]:
        answer = answer and n in 'QWERTYUIOPASDFGHJKLZXCVBNM'
    return answer


def check_number(type_number, number):
    year = int(type_number.split('_')[-1])
    if year >= 2004 and len(number) == 8 and is_number(number):
        return True
    elif len(number) == 9:
        answer = True
        for n in number[:-2]:
            answer = answer and n in '0123456789'
        for n in number[-2:]:
            answer = answer and n in 'QWERTYUIOPASDFGHJKLZXCVBNM'
        return answer
    return False


v_say_what_is_it = np.vectorize(say_what_is_it)


def get_number(img):
    x, y, width, height = blue_coordinates = find_blue(img)
    # cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 255), 1)
    yellow_coordinates = find_yellow(img)
    year = get_type_of_car_number(*blue_coordinates[2:], *yellow_coordinates[2:])
    needed_funcs = funcs_of_type[year]
    answers = []
    for func in needed_funcs:
        type_number = "_".join(func.__name__.split('_')[-2:])
        scopes = search_scope(img, func)
        answer = []
        for i in range(len(scopes)):
            scope = scopes[i]
            x, y, width, height = (int(num) for num in scope)
            # cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 0), 1)
            cropped = img[y:y + height, x:x + width]
            # gry = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
            # ret, thresh_gry = cv2.threshold(gry, 120, 255, cv2.THRESH_BINARY)
            # its = say_what_is_it(cropped)
            answer.append(cropped)
            # cv2.imwrite(f'Output/{answer[-1]}.jpg', its[0])
        answer = update_number(year, "".join(v_say_what_is_it(answer)))
        if check_number(type_number, answer):
            return type_number, answer
    return answers


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
