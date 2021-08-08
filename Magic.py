class MagicClass:
    _x = 5

    def __init__(self):
        self.lst = [self._x]

    def __repr__(self):
        return 'ПППП'

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self.lst.clear()
        self.lst.append(x)
        self._x = x

    def y(self):
        return 5

    def __eq__(self, other):
        # print(other.x)
        return self.x == other.x

    def __iter__(self):
        return self.lst.__iter__()




magic_1 = MagicClass()
magic_1.x = 1
magic_2 = MagicClass()
magic_2.x = 6
magic_2.lst.append(7)
for x in magic_2:
    print(x)

a = []
a.append(a)
a.append(a)
print(a[0][0][0][0])