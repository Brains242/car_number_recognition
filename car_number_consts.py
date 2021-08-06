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


AMERICAN_1995 = CarNumberCorrelation(3.1666666666666665, 3.3947368421052633)
STANDARD_1995 = CarNumberCorrelation(3.1923076923076925, 3.375)
STANDARD_2015 = CarNumberCorrelation(0.467005076142132, 3.1578947368421053)
TRACTOR_1995 = CarNumberCorrelation(3.25, 3.260869565217391)
STANDARD_2004 = CarNumberCorrelation(0.9058823529411765, 0.8488372093023255)
AMERICAN_2004 = CarNumberCorrelation(0.6170212765957447, 0.6444444444444445)
TRACTOR_2004 = CarNumberCorrelation(0.5384615384615384, 0.5267175572519084)
AMERICAN_2015 = CarNumberCorrelation(0.616822429906542, 2.933333333333333)


if __name__ == '__main__':
    american_1995 = CarNumberCorrelation(3.1666, 3.39)
    print(american_1995.correlation(3.1666, 3.39))