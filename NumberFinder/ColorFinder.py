import math
import os
import cv2.cv2 as cv2
import imutils
import numpy as np

lower_blue = [90, 50, 120]
upper_blue = [138, 255, 255]
lower_yellow = [22, 93, 0]
upper_yellow = [45, 255, 255]
lower_black = [0, 5, 50]
upper_black = [179, 50, 255]


def contours_of_color(image, lower, upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')
    mask = cv2.inRange(hsv, lower, upper)
    thresh = cv2.threshold(mask, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    c = max(contours, key=cv2.contourArea)
    return c


def find_center_of_contour(contours):
    moments = cv2.moments(contours, 1)
    moment01 = moments['m01']
    moment10 = moments['m10']
    area = moments['m00']
    x = int(moment10 / area)
    y = int(moment01 / area)
    return x, y


def align_image_from_flag(image):
    blue_contour = contours_of_color(image, lower_blue, upper_blue)
    yellow_contour = contours_of_color(image, lower_yellow, upper_yellow)
    white_contour = contours_of_color(image, lower_black, upper_black)
    blue_center = find_center_of_contour(blue_contour)
    yellow_center = find_center_of_contour(yellow_contour)
    # cv2.line(image, blue_center, yellow_center, (0, 0, 0), 1)
    cv2.drawContours(image, [white_contour], -1, (255, 0, 0), 2)

    # angle = math.degrees(math.atan((blue_center[0] - yellow_center[0]) / (blue_center[1] - yellow_center[1])))
    # height, width, px = image.shape
    # center = int(width / 2), int(height / 2)
    # rotate_matrix = cv2.getRotationMatrix2D(center, -angle, 1)
    # image = cv2.warpAffine(image, rotate_matrix, (width, height))
    return image


# def rotate(image, angle, center = None, scale = 1.0):
#     (h, w) = image.shape[:2]
#
#     if center is None:
#         center = (w / 2, h / 2)
#
#     # Perform the rotation
#     M = cv2.getRotationMatrix2D(center, angle, scale)
#     rotated = cv2.warpAffine(image, M, (w, h))
#
#     return rotated


def find_blue(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(lower_blue, dtype='uint8')
    upper = np.array(upper_blue, dtype='uint8')

    mask = cv2.inRange(hsv, lower, upper)
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, width, height = cv2.boundingRect(c)
        # cv2.rectangle(img, (x, y), (x + width, y + height), (50, 255, 50), 2)
        center = x + width // 2, y + height // 2
        cv2.circle(img, center, 2, (255, 255, 255), -1)
        return x, y, width, height
    return False


def find_yellow(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array(lower_yellow, dtype='uint8')
    upper = np.array(upper_yellow, dtype='uint8')

    mask = cv2.inRange(hsv, lower, upper)
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, width, height = cv2.boundingRect(c)
        # cv2.rectangle(img, (x, y), (x + width, y + height), (0, 190, 0), 2)
        center = x + width // 2, y + height // 2
        cv2.circle(img, center, 2, (0, 0, 0), -1)
        return x, y, width, height
    return False


if __name__ == '__main__':
    # img_names = os.listdir('Input')
    #
    # for name in img_names:
    #     try:
    #         img = cv2.imread(f'Input/{name}')
    #         # cv2.imshow(img)
    #         find_points_of_blue(img)
    #         cv2.imshow(name, img)
    #         cv2.waitKey(0)
    #     except:
    #         print(name, 'error')
    img = cv2.imread('Input/car_2015.jpg')
    # cv2.imshow('Image', img)
    img = align_image_from_flag(img)
    cv2.imshow('Rotated', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
