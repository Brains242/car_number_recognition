import cv2
import numpy as np

from NumberFinder.ColorFinder import find_blue, find_yellow

car_number_path = 'Input/american_2015.jpg'


if __name__ == '__main__':
    img = cv2.imread(car_number_path)
    x, y, width, height = find_blue(img)
    print(x, y, width/height)
    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 190, 0), 2)
    x, y, width, height = find_yellow(img)
    print(x, y, width/height)
    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 190, 0), 2)
    cv2.imshow('Image', img)
    while True:
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
