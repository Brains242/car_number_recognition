import threading
import time


class Something:
    a: list
    on: bool

    def __init__(self):
        self.a = []

    def run(self):
        while self.on:
            print('append a')
            self.a.append('a')
            time.sleep(1)

    def start(self):
        self.on = True
        threading.Thread(target=self.run).start()

    def stop(self):
        self.on = False


if __name__ == '__main__':
    s = Something()
    s.start()
    try:
        while True:
            d = input()
            if d == 'stop':
                s.stop()
                break
            else:
                s.a.append(d)
                print(s.a)
    except KeyboardInterrupt:
        s.stop()

