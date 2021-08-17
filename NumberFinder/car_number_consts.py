from cv2 import cv2

from NumberFinder.ColorFinder import find_blue, find_yellow


class CarNumberCorrelation:
    def __init__(self, blue: float, yellow: float):
        self.blue = blue
        self.yellow = yellow

    def correlation(self, blue: float, yellow: float) -> bool:
        return (
                self.blue * 0.9 < blue < self.blue * 1.1
                and
                self.yellow * 0.9 < yellow < self.yellow * 1.1
        )


AMERICAN_1995 = CarNumberCorrelation(3.1666666666666665, 3.3076923076923075)
AMERICAN_2004 = CarNumberCorrelation(0.6170212765957447, 0.6170212765957447)
AMERICAN_2015 = CarNumberCorrelation(0.616822429906542, 2.933333333333333)
STANDARD_1995 = CarNumberCorrelation(3.1923076923076925, 3.24)
STANDARD_2004 = CarNumberCorrelation(0.9058823529411765, 0.8390804597701149)
STANDARD_2015 = CarNumberCorrelation(0.467005076142132, 3.1578947368421053)
TRACTOR_1995 = CarNumberCorrelation(3.25, 3.125)
TRACTOR_2004 = CarNumberCorrelation(0.5384615384615384, 0.5227272727272727)

car_numbers_list = [AMERICAN_1995, AMERICAN_2004, AMERICAN_2015, STANDARD_1995,
                    STANDARD_2004, STANDARD_2015, TRACTOR_1995, TRACTOR_2004]


def get_type_of_car_number(b_width, b_height, y_width, y_height):
    if b_width > b_height and y_width > y_height:
        return 1995
    elif b_width < b_height and y_width < y_height:
        return 2004
    elif b_width < b_height and y_width > y_height:
        return 2015


if __name__ == '__main__':
    img = cv2.imread('../Input/standard_2004.jpg')
    blue_x, blue_y, blue_width, blue_height = find_blue(img)
    yellow_x, yellow_y, yellow_width, yellow_height = find_yellow(img)
    number_from_camera = CarNumberCorrelation(blue_width / blue_height, yellow_width / yellow_height)
    for n in range(len(car_numbers_list)):
        number = car_numbers_list[n]
        nfc_blue, nfc_yellow = blue_width / blue_height, yellow_width / yellow_height
        print(number.correlation(nfc_blue, nfc_yellow))
