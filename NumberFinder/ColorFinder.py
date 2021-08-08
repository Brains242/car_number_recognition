import cv2
import module as module
import numpy as np

lower_blue = [90, 50, 120]
upper_blue = [138, 255, 255]
lower_yellow = [22, 93, 0]
upper_yellow = [45, 255, 255]


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
        return x, y, width, height
    return False
