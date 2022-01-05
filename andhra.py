import pytesseract
import cv2


def andhra_data(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    x, y, w, h = 400, 210, 300, 58
    ROI = thresh[y:y + h, x:x + w]
    reg = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')


    x, y, w, h = 400, 260, 300, 58
    ROI = thresh[y:y + h, x:x + w]
    name = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')


    x, y, w, h = 1950, 600, 165, 58
    ROI = thresh[y:y + h, x:x + w]
    gpa1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')


    x, y, w, h = 1950, 750, 163, 58
    ROI = thresh[y:y + h, x:x + w]
    gpa2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')


    x, y, w, h = 1050,1060, 163, 58
    ROI = thresh[y:y + h, x:x + w]
    tot = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')



    x, y, w, h = 590, 1060, 123, 58
    ROI = thresh[y:y + h, x:x + w]
    cgpa = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')


    x, y, w, h = 570, 530, 143, 58
    ROI = thresh[y:y + h, x:x + w]
    sub1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("SUB 1:", sub1)
    x, y, w, h = 740, 530, 203, 58
    ROI = thresh[y:y + h, x:x + w]
    sub2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("SUB 2:", sub2)
    x, y, w, h = 950, 530, 203, 58
    ROI = thresh[y:y + h, x:x + w]
    sub3 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("SUB 3:", sub3)

    x, y, w, h = 1250, 530, 203, 58
    ROI = thresh[y:y + h, x:x + w]
    sub4 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("SUB 3:", sub3)

    x, y, w, h = 1500, 530, 203, 58
    ROI = thresh[y:y + h, x:x + w]
    sub5 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("SUB 4:", sub4)

    x, y, w, h = 1750, 530, 200, 58
    ROI = thresh[y:y + h, x:x + w]
    sub6 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("SUB 5:", sub5)

    x, y, w, h = 580, 605, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m1_1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 1_1:", m1_1)

    x, y, w, h = 580, 770, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m1_2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 1_2:", m1_2)

    x, y, w, h = 750, 605, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m2_1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 2_1:", m2_1)

    x, y, w, h = 960, 605, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m3_1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 3_1:", m3_1)

    x, y, w, h = 1260, 605, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m4_1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 4_1:", m4_1)

    x, y, w, h = 1550, 605, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m5_1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 5_1:", m3_1)

    x, y, w, h = 1800, 605, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m6_1 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 6_1:", m6_1)


    x, y, w, h = 588, 785, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m1_2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 1_2:", m1_2)

    x, y, w, h = 750, 785, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m2_2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 2_2:", m2_2)

    x, y, w, h = 960, 785, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m3_2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 3_2:", m3_2)

    x, y, w, h = 1260, 785, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m4_2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 4_2:", m4_2)

    x, y, w, h = 1550, 785, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m5_2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    #print("MARK 5_2:", m5_2)

    x, y, w, h = 1800, 785, 103, 48
    ROI = thresh[y:y + h, x:x + w]
    m6_2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')

    print("Name:", name)
    print("REG NO:", reg)
    print(sub1,m1_1,m1_2)
    print(sub2,m2_1,m2_2)
    print(sub3,m3_1,m3_2)
    print(sub4,m4_1,m4_2)
    print(sub5,m5_1,m5_2)
    print(sub6,m6_1,m6_2)
    print("GPA 1:", gpa1)
    print("GPA 2:", gpa2)
    print("CGPA:", cgpa)
    print("TOTAL:", tot)



