import sys
from cv2 import cv2


class Video:
    on: bool = False
    src: str
    capture: cv2.VideoCapture

    def __init__(self, src: str):
        self.src = src
        self.settings = (self.src, cv2.CAP_FFMPEG)

    def restart(self):
        while self.on:
            self.capture = cv2.VideoCapture(self.src)
            if self.capture.isOpened():
                break

    def start(self):
        if not self.on:
            self.on = True
            self.restart()
            while self.on:
                if self.capture.isOpened():
                    image_is_ok, image = self.capture.read()
                    if image_is_ok:
                        cv2.imshow('Video Receiver', image)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            self.stop()
                            break
                else:
                    self.restart()

    def stop(self):
        if self.on:
            self.on = False


if __name__ == '__main__':
    if '--src' in sys.argv:
        src = sys.argv[sys.argv.index('--src')+1]
    else:
        src = 'rtsp://10.10.10.11:8554/local_rtsp_server'
    video = Video(src)
    try:
        video.start()
    except KeyboardInterrupt:
        video.stop()
