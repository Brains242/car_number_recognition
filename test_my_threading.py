import logging
import threading
import time
import concurrent.futures
from typing import List, Dict

from CarNumberRecognition import say_what_is_it, update_number
from NumberFinder import search_scope


def is_number(number):
    answer = True
    for n in number[2:-2]:
        answer = answer and n in '0123456789'
    for n in number[:2]:
        answer = answer and n in 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for n in number[-2:]:
        answer = answer and n in 'QWERTYUIOPASDFGHJKLZXCVBNM'
    return answer


def check_number(year, number):
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


class NumberRecognition:
    on: bool
    prediction: dict
    is_predict: Dict[str, bool]
    year: int

    def __init__(self, img, needed_funcs):
        self.img = img
        self.needed_funcs = needed_funcs
        self.year = int("_".join(self.needed_funcs[0].__name__.split('_')[-2:]).split('_')[-1])
        self.prediction = {}
        self.is_predict = {}
        for name in self.needed_funcs:
            type_number = "_".join(name.__name__.split('_')[-2:])
            self.prediction[type_number] = {}
            self.is_predict[type_number] = False

    def predict(self, name, index, scope, length):
        x, y, width, height = (int(num) for num in scope)
        cropped = self.img[y:y + height, x:x + width]
        try:
            its = say_what_is_it(cropped)
            self.prediction[name][index] = its
            # print(name, self.prediction[name])
            if length == len(self.prediction[name]):
                answer = update_number(self.year, "".join([self.prediction[name][i] for i in sorted(self.prediction[name].keys())]))
                # print(answer)
                if check_number(self.year, answer):
                    self.is_predict[name] = True
                    self.prediction[name] = answer
                else:
                    self.is_predict[name] = False
        except:
            self.prediction[name] = None

    def say_what_is_it(self, function):
        scopes = search_scope(self.img, function)
        name = "_".join(function.__name__.split('_')[-2:])
        for i in range(len(scopes)):
            threading.Thread(target=self.predict, args=(name, i, scopes[i], len(scopes))).start()

    def loop(self):
        self.on = True
        for function in self.needed_funcs:
            self.say_what_is_it(function)
        while self.on:
            for type_number in self.is_predict.keys():
                if self.is_predict[type_number]:
                    return self.year, self.prediction[type_number]
            time.sleep(0.1)

    def stop(self):
        self.on = False

# if __name__ == "__main__":
