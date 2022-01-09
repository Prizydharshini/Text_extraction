import pytesseract
import cv2

def CISCE_data(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    x, y, w, h = 200, 200, 400, 58
    ROI = thresh[y:y + h, x:x + w]
    data = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("NAME :",data)

    x, y, w, h = 180, 250, 300, 58
    ROI = thresh[y:y + h, x:x + w]
    reg_no = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("REGISTER NO :",reg_no)

    x, y, w, h = 900, 400, 150, 58
    ROI = thresh[y:y + h, x:x + w]
    eng = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("ENGLISH :",eng)

    x, y, w, h = 900, 450, 150, 52
    ROI = thresh[y:y + h, x:x + w]
    maths = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("MATHS :",maths)

    x, y, w, h = 900, 480, 150, 52
    ROI = thresh[y:y + h, x:x + w]
    phy = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("PHYSICS :",phy)

    x, y, w, h = 900, 530, 150, 52
    ROI = thresh[y:y + h, x:x + w]
    chem = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("CHEMISTRY :",chem)

    x, y, w, h = 900, 570, 150, 52
    ROI = thresh[y:y + h, x:x + w]
    cs = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("COMP SCIENCE :",cs)

    x, y, w, h = 900, 620, 150, 52
    ROI = thresh[y:y + h, x:x + w]
    sp = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("SUPW & COMMUNITY SERVICE :",sp)

    cv2.imshow('thresh', thresh)
    cv2.imshow('ROI', ROI)
    cv2.waitKey()