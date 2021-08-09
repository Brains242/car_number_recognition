from cv2 import cv2
from NumberFinder.ColorFinder import find_blue

import cv2


# def map_image_parameter(x, in_min, in_max, out_min, out_max):
#     return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


# def apply_brightness_contrast(input_img, brightness=255, contrast=127):
#     brightness = map_image_parameter(brightness, 0, 510, -255, 255)
#     contrast = map_image_parameter(contrast, 0, 254, -127, 127)
#     if brightness != 0:
#         if brightness > 0:
#             shadow = brightness
#             highlight = 255
#         else:
#             shadow = 0
#             highlight = 255 + brightness
#         alpha_b = (highlight - shadow)/255
#         gamma_b = shadow
#         buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
#     else:
#         buf = input_img.copy()
#     if contrast != 0:
#         f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
#         alpha_c = f
#         gamma_c = 127*(1-f)
#         buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
#     cv2.putText(buf,'B:{},C:{}'.format(brightness,contrast),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     return buf

def scope_to_int(_scope):
    # return [[int(number) for number in point] for point in _scope]
    return _scope


def find_coordinates_of_number_letters_american_1995(x, y, width, height):
    first_x = x - (width / 5)
    first_y = y + (4 * height)
    first_width = width * 195 / 130
    first_height = height * 151 / 40

    second_x = first_x + first_width + (width / 2)
    second_y = y - height * 1.5
    second_width = width * 387 / 130
    second_height = height * 180 / 40

    third_x = first_x + first_width
    third_y = second_y + second_height
    third_width = width * 590 / 130
    third_height = height * 204 / 40
    return (
        [first_x, first_y, first_width, first_height],
        [third_x, third_y, third_width, third_height],
        [second_x, second_y, second_width, second_height]
    )


def find_coordinates_of_number_letters_american_2004(x, y, width, height):
    first_width = width * 70 / 28
    first_height = height
    first_x = x + width
    first_y = y

    second_width = first_width * 1.1
    second_height = height
    second_x = first_x + first_width + (width / 1.2) * 0.7
    second_y = first_y

    third_width = width * 119 / 28
    third_height = height
    third_x = x + width + (width * 0.5)
    third_y = y + height

    return (
        [first_x, first_y, first_width, first_height],
        [third_x, third_y, third_width, third_height],
        [second_x, second_y, second_width, second_height]
    )


def find_coordinates_of_number_letters_american_2015(x, y, width, height):
    first_width = width * 122 / 64
    first_height = height
    first_x = x + width + (width * 0.4)
    first_y = y

    second_width = first_width * 1.15
    second_height = height
    second_x = first_x + first_width + (width * 1.15) * 0.8
    second_y = y * 0.9

    third_width = width * 285 / 64
    third_height = height * 1.2
    third_x = first_x + (width / 5)
    third_y = y + height * 0.8

    return (
        [first_x, first_y, first_width, first_height],
        [third_x, third_y, third_width, third_height],
        [second_x, second_y, second_width, second_height]
    )


def find_coordinates_of_number_letters_standard_1995(x, y, width, height):
    first_x = x + width * 0.1
    first_y = y + height + (height * 1.5)
    first_width = width * 95 / 82
    first_height = height * 72 / 26

    second_x = x + first_width
    second_y = y - (height / 3)
    second_width = width * 263 / 82
    second_height = height * 146 / 26

    third_x = second_x + second_width + (width / 1.5) * 0.7
    third_y = second_y * 0.8
    third_width = width * 176 / 82 * 1.1
    third_height = second_height * 1.1

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


def find_coordinates_of_number_letters_standard_2004(x, y, width, height):
    first_x = x + width
    first_y = y + (height / 6)
    first_width = width * 211 / 72
    first_height = height * 152 / 88

    second_x = x + width + first_width
    second_y = first_y
    second_width = width * 341 / 72 * 0.95
    second_height = first_height

    third_x = x + width + first_width + second_width * 0.9
    third_y = first_y
    third_width = width * 240 / 72
    third_height = first_height * 1.05

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


def find_coordinates_of_number_letters_standard_2015(x, y, width, height):
    first_x = x + width
    first_y = y
    first_width = width * 264 / 87 * 0.87
    first_height = height

    second_x = first_x + first_width
    second_y = y
    second_width = width * 356 / 87
    second_height = height

    third_x = second_x + second_width
    third_y = y
    third_width = width * 254 / 87
    third_height = height

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

    second_width = width * 406 / 75 * 0.95
    second_height = height * 157 / 24 * 1.1
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


def find_coordinates_of_number_letters_tractor_2004(x, y, width, height):
    first_width = width * 165 / 68
    first_height = height * 88 / 128
    first_x = x + width + (width * 0.6)
    first_y = y

    second_width = width * 248 / 68
    second_height = height * 82 / 128 * 1.2
    second_x = x + width + (width * 0.1)
    second_y = first_y + first_height * 0.9

    third_width = first_width
    third_height = first_height
    third_x = first_x
    third_y = second_y + second_height * 0.9

    return (
        [first_x, first_y, first_width, first_height],
        [second_x, second_y, second_width, second_height],
        [third_x, third_y, third_width, third_height]
    )


def search_scope(image, function):
    blue_x, blue_y, blue_width, blue_height = find_blue(image)
    return scope_to_int(function(blue_x, blue_y, blue_width, blue_height))


if __name__ == '__main__':
    img = cv2.imread('../Input/american_1995.jpg')
    scopes = [*search_scope(img, find_coordinates_of_number_letters_american_1995),
              *search_scope(img, find_coordinates_of_number_letters_standard_1995),
              *search_scope(img, find_coordinates_of_number_letters_tractor_1995)
    ]
    for scope in scopes:
        x, y, width, height = [int(number) for number in scope]
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 0), 1, 1)
    cv2.imwrite('../Output/test.jpg', img)
