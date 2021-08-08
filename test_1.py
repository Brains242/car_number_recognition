import os
from cv2 import cv2

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
    1995: {
        find_coordinates_of_number_letters_american_1995,
        find_coordinates_of_number_letters_standard_1995,
        find_coordinates_of_number_letters_tractor_1995
    },
    2004: {
        find_coordinates_of_number_letters_american_2004,
        find_coordinates_of_number_letters_standard_2004,
        find_coordinates_of_number_letters_tractor_2004
    },
    2015: {
        find_coordinates_of_number_letters_american_2015,
        find_coordinates_of_number_letters_standard_2015
    }
}

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
            its = say_what_is_it(cropped)
            answer.append(its[1])
            cv2.imwrite(f'Output/{answer[-1]}.jpg', its[0])
        answer = update_number(year, "".join(answer))
        print(answer)
        if check_number(type_number, answer):
            return type_number, answer
    return answers


if __name__ == '__main__':

    img_names = os.listdir('Input')

    for name in img_names:
        try:
            img = cv2.imread(f'Input/{name}')
            print(name, get_number(img))
        except:
            print(name, 'error')



