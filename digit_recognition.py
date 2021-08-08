import random

import numpy
from keras.datasets import mnist  # subroutines for fetching the MNIST dataset
from keras.models import Model  # basic class for specifying and training a neural network
from keras.layers import Input, Dense  # the two types of neural network layer we will be using
from keras.utils import np_utils
from typing import List, Tuple

DOTS = ((1, 0), (0, 2), (-3, 0), (0, -4))  # По условию задачи
data_number = 10000  # Количество рандомных связок "точка - мин расстояние"
random.seed(567)  # Чтобы результаты повторялись


def min_distance(x: int, y: int) -> List[int]:
    """
    Функция считает расстояния от x, y до каждой из 4 точек и выдаёт список из 4 чисел.
    1 - это расстоянеие минимально, 0 - нет
    :param x: int
    :param y: int
    :return: List[int]
    """
    answer = [0, 0, 0, 0]
    distances = []
    for i in range(4):
        x2, y2 = DOTS[i]
        distances.append(numpy.sqrt(
            (x - x2)**2 + (y - y2)**2
        ))
    answer[distances.index(min(distances))] = 1
    return answer


def gen_random_data():
    """
    Генерирует 2 списка.
    Первый - Списки с рандомными точками x,y.
    Второй - Списки с соответствующими списками ответов к выходним нейронам
    :return: Tuple[numpy.ndarray[List[int, int]], numpy.ndarray[List[int, int, int, int]]]
    """
    xy = []
    mds = []
    for i in range(data_number):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        md = min_distance(x, y)
        xy.append([x, y])
        mds.append(md)
    return numpy.array(xy), numpy.array(mds)


batch_size = 128  # in each iteration, we consider 128 training examples at once
num_epochs = 200  # we iterate twenty times over the entire training set
hidden_size = 100  # there will be 512 neurons in both hidden layers

num_train = 600000  # Количество тренировок
num_test = 10000  # Количество тестов

input_data = 2  # Количество входных данных (x, y)
num_classes = 4  # Количество выходных данных [0, 0, 0, 1]

X_train, y_train = gen_random_data()
X_test, y_test = gen_random_data()

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')


inp = Input(shape=2)
hidden_1 = Dense(hidden_size, activation='relu')(inp)
hidden_2 = Dense(hidden_size, activation='relu')(hidden_1)  # First hidden ReLU layer
out = Dense(num_classes, activation='softmax')(hidden_2)  # Output softmax layer

model = Model(inp, out)  # To define a model, just specify its input and output layers

model.compile(loss='categorical_crossentropy',  # using the cross-entropy loss function
              optimizer='adam',  # using the Adam optimiser
              metrics=['accuracy'])  # reporting the accuracy

model.fit(X_train, y_train,  # Train the model using the training set...
          batch_size=batch_size,
          verbose=1, validation_split=0.1)  # ...holding out 10% of the data for validation
model.evaluate(X_test, y_test, verbose=1)  # Evaluate the trained model on the test set!

x, y = (int(i) for i in input('Введите точку: ').split(' '))

answer = model.predict(numpy.array([[x, y]]))[0]
max_ = 0
max_i = 0
for i in range(4):
    if answer[i] > max_:
        max_ = answer[i]
        max_i = i
    print(f'С вероятностью {answer[i]:.2} это {DOTS[i]}')

print(f'Близжайшая точка: {DOTS[max_i]}')