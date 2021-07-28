from cv2 import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\Roma\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('123.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
oem_psm_config = '--oem 3 --psm 6'
print(pytesseract.image_to_string(gray, config=oem_psm_config))

data = pytesseract.image_to_data(gray, config=oem_psm_config)
for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue
    el = el.split()
    print(el)
    try:
        x, y, w, h = (int(el[6]), int(el[7]), int(el[8]), int(el[9]))
        cv2.rectangle(gray, (x, y), (w + x, h + y), (0, 0, 255), 1)
        cv2.putText(gray, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
    except IndexError:
        print('Error!!!')
cv2.imshow('Result', gray)
cv2.waitKey(0)
