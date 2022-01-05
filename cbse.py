import pytesseract
import cv2


def cbse_data(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    x, y, w, h = 600, 1050, 500, 78
    ROI = thresh[y:y + h, x:x + w]
    name = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("NAME:",name)

    x, y, w, h = 400, 1150, 500, 78
    ROI = thresh[y:y + h, x:x + w]
    reg = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("REGISTER NUMBER:", reg)

    x, y, w, h = 350, 1950, 600, 78
    ROI = thresh[y:y + h, x:x + w]
    sub1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')

    x, y, w, h = 390, 2010, 500, 78
    ROI = thresh[y:y + h, x:x + w]
    sub2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')

    x, y, w, h = 390, 2080, 500, 78
    ROI = thresh[y:y + h, x:x + w]
    sub3 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')

    x, y, w, h = 390, 2140, 500, 76
    ROI = thresh[y:y + h, x:x + w]
    sub4 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')

    x, y, w, h = 390, 2220, 800, 78
    ROI = thresh[y:y + h, x:x + w]
    sub5 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')

    x, y, w, h = 1570, 1950, 160, 78
    ROI = thresh[y:y + h, x:x + w]
    mark1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print(sub1,":",mark1)

    x, y, w, h = 1570, 2020, 160, 78
    ROI = thresh[y:y + h, x:x + w]
    mark2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print(sub2,":",mark2)

    x, y, w, h = 1570, 2090, 150, 78
    ROI = thresh[y:y + h, x:x + w]
    mark3 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print(sub3,":",mark3)

    x, y, w, h = 1570, 2160, 150, 78
    ROI = thresh[y:y + h, x:x + w]
    mark4 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print(sub4,":",mark4)

    x, y, w, h = 1570, 2020, 150, 78
    ROI = thresh[y:y + h, x:x + w]
    mark5 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print(sub5,":",mark5)

