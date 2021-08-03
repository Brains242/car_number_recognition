# import buf as buf
from cv2 import cv2
import pytesseract
import numpy as np


def find_coordinates_of_number_letters_standard_2015(x, y, width, height):
    first_x = x + width
    first_y = y
    first_width = width * 264 / 87
    first_height = height

    second_x = x + width + first_width
    second_y = y
    second_width = width * 356 / 87
    second_height = height

    third_x = x + width + first_width + second_width
    third_y = y
    third_width = width * 254 / 87
    third_height = height

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


def find_coordinates_of_number_letters_american_1995(x, y, width, height):
    first_x = x - (width / 3.25)
    first_y = y + (4 * height)
    first_width = width * 195 / 130
    first_height = height * 151 / 40

    second_x = first_x + 1.6 * first_width
    second_y = y - height * 1.3
    second_width = width * 387 / 130 * .9
    second_height = height * 180 / 40

    third_x = second_x - (x / (x / 87))
    third_y = second_y + second_height * .9
    third_width = width * 590 / 130 * .9
    third_height = height * 204 / 40
    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


def find_coordinates_of_number_letters_tractor_1995(x, y, width, height):
    first_width = width + (width * 0.1)
    first_height = height * 3
    first_x = x
    first_y = y + height + (height * 1.5)

    second_width = width * 406 / 75
    second_height = height * 157 / 24
    second_x = x - (width / 1.6)
    second_y = y - second_height - (height / 2)

    third_width = width * 250 / 75
    third_height = height * 150 / 24
    third_x = x + width + (width * 0.1)
    third_y = y - (y * 0.03)

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


def find_coordinates_of_number_letters_standard_2004(x, y, width, height):
    first_x = x + width
    first_y = y + (height / 6)
    first_width = width * 211 / 72
    first_height = height * 152 / 88

    second_x = x + width + first_width
    second_y = first_y
    second_width = width * 341 / 72
    second_height = first_height

    third_x = x + width + first_width + second_width
    third_y = first_y
    third_width = width * 240 / 72
    third_height = first_height

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


def find_coordinates_of_number_letters_standard_1995(x, y, width, height):
    first_x = x
    first_y = y + height + (height * 1.5)
    first_width = width * 95 / 82
    first_height = height * 72 / 26

    second_x = x + first_width
    second_y = y - (height / 3)
    second_width = width * 263 / 82
    second_height = height * 146 / 26

    third_x = second_x + second_width + (width / 1.5)
    third_y = second_y
    third_width = width * 176 / 82
    third_height = second_height

    fourth_x = third_x + third_width
    fourth_y = second_y
    fourth_width = width * 241 / 82
    fourth_height = second_height

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height],
        [fourth_x, fourth_y, fourth_width, fourth_height]
    )


def find_coordinates_of_number_letters_american_2004(x, y, width, height):
    first_width = width * 70 / 28
    first_height = height
    first_x = x + width
    first_y = y

    second_width = first_width
    second_height = height
    second_x = first_x + first_width + (width / 1.2)
    second_y = y

    third_width = width * 119 / 28 * 1.2
    third_height = height
    third_x = x + width + (width * 0.5)
    third_y = y + height

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


def find_coordinates_of_number_letters_tractor_2004(x, y, width, height):
    first_width = width * 165 / 68
    first_height = height * 88 / 128
    first_x = x + width + (width * 0.6)
    first_y = y

    second_width = width * 248 / 68
    second_height = height * 82 / 128
    second_x = x + width + (width * 0.1)
    second_y = first_y + first_height

    third_width = first_width
    third_height = first_height
    third_x = first_x
    third_y = second_y + second_height

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


def find_coordinates_of_number_letters_american_2015(x, y, width, height):
    first_width = width * 122 / 64
    first_height = height
    first_x = x + width + (width * 0.4)
    first_y = y

    second_width = first_width
    second_height = height
    second_x = first_x + first_width + (width * 1.15)
    second_y = y

    third_width = width * 285 / 64
    third_height = height
    third_x = first_x + (width / 5)
    third_y = y + height

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


if __name__ == '__main__':
    img = cv2.imread('Input/american_2015.jpg')
    x, y = 13, 9
    width, height = 64, 103
    scopes = find_coordinates_of_number_letters_american_2015(x, y, width, height)
    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 0), 1, 1)
    for scope in scopes:
        x, y, width, height = [int(number) for number in scope]
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 0), 1, 1)
    cv2.imwrite('Output/test.jpg', img)
