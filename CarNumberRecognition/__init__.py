import numpy as np
import tensorflow as tf
from cv2 import cv2
import keras_ocr

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
keras_ocr_pipeline = keras_ocr.pipeline.Pipeline()


def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf


def update_number(year, number):
    new_number = ''
    if year == 1995:
        for n in number[:-2]:
            if n == 'O':
                new_number += '0'
            else:
                new_number += n

        for n in number[-2:]:
            if n == '0':
                new_number += 'O'
            else:
                new_number += n
    else:
        for n in number[:2]:
            if n == '0':
                new_number += 'O'
            elif n == 'L':
                new_number += 'I'
            else:
                new_number += n
        for n in number[2:-2]:
            if n == 'O':
                new_number += '0'
            else:
                new_number += n
        for n in number[-2:]:
            if n == '0':
                new_number += 'O'
            else:
                new_number += n
    return new_number


def update_image(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 0, 0), (70, 255, 255))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    idx = 0
    mask1 = np.zeros_like(img)

    cv2.drawContours(mask1, contours, idx, (255, 255, 255), -1)
    out = np.zeros_like(img)
    out[mask1 == (255, 255, 255)] = img[mask1 == 255]
    return out


def say_what_is_it(image):
    try:
        image = (255-image)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except:
        return ''
    # gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    # ret, thresh_gry = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    # rgb = update_image(rgb)

    prediction_groups = keras_ocr_pipeline.recognize([rgb])
    answer = ''
    if len(prediction_groups[0]):
        max_area = 0
        for prediction in prediction_groups[0]:
            p, pts = prediction
            pt_top_left, pt_top_right, pt_bottom_right, pt_bottom_left = pts
            width, height = pt_top_right[0] - pt_top_left[0], pt_bottom_right[1] - pt_top_right[1]
            area = width * height
            if area > max_area:
                max_area = area
                answer = p
    return answer.upper()

# if __name__ == '__main__':
#     from NumberFinder import find_coordinates_of_number_letters_american_1995
#     img = cv2.imread('../car_number_recognition/Input/american_1995.jpg')
#     cv2.imshow('Original', img)
#     print(find_coordinates_of_number_letters_american_1995)
#     first_x, first_y, first_width, first_height = find_coordinates_of_number_letters_american_1995
#     cropped = img[first_x:first_width, first_y:first_height]
#     cv2.imshow('Cropped', cropped)
#     cv2.waitKey(0)
#     # print(say_what_is_it(img))
