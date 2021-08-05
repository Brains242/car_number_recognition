import cv2
import numpy as np

img = cv2.imread('Input/standard_2015.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([90, 150, 0])
upper_range = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower_range, upper_range)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cont = cv2.drawContours(img, contours, -1, (255, 255, 255), 2, cv2.LINE_AA, hierarchy, 1)
cv2.imshow('Contours', img)
while True:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()