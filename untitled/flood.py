import numpy as np
import cv2
import pytesseract
from PIL import Image

show_steps = True
decode_with_tessercat = True
decode_with_templates = True

img = cv2.imread('C:\Users\Pauliaus\PycharmProjects\untitled\img\car5.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (800, 600))
ret, thresh2 = cv2.threshold(img, 120, 500, cv2.THRESH_BINARY_INV)
roi_array = [] #iskirptu paveiksliuku masyvas
roi_array_m = [] #iskirptu raidziu masyvas
index = 0
show_img = True
index_array = []
image, contours, hier = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
modified = 0
print "Number plate finder"
print "Enable show_steps, to see images"

#funkcija kuri paveiksliuke isskiria numerius ir issaugo i roi_array
for c in contours:
    index = index + 1
    rect = cv2.minAreaRect(c)
    width = rect[1][0]
    height = rect[1][1]
    if width > 0 and height > 0:
        height_width_ratio = height / width
        if (height_width_ratio > 0.15) and (height_width_ratio < 0.3) and (height*width > 3000):
            box = cv2.boxPoints(rect)
            box = np.int0(box) #lyg ir box vertes i integer paverciamos
            x, y, w, h = cv2.boundingRect(c)
            roi = img[y:y+h, x:x+w]
            # cv2.imwrite(str(index) + '.jpg', roi)
            cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
            index_array.extend([index])
            roi_array.append(roi)

#funkcija kuri plates paima ir isima raides ir sudeda raides i masyva roi_array_m.
print "Number plates extracted, all fine"
print "---------------------------------"

if decode_with_tessercat == True:
    print "Pytessercat reikalai"
    image_one = Image.open('Plate.jpg')
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
    decoded_letters = pytesseract.image_to_string(image_one)
    print(decoded_letters)
    print "---------------------------------"

if decode_with_templates == True:
    print "Dekodavimas su templates"
    print "Number plate letter finder"
    for i in range(0, len(roi_array)):  # runs plates
        modified_plate_name = "modified_number_plate" + str(i)
        ret, modified_plate = cv2.threshold(roi_array[i], 120, 500, cv2.THRESH_BINARY_INV)
        # kernel = np.ones((5, 5), np.uint8)
        # modified_plate = cv2.morphologyEx(modified_plate, cv2.MORPH_OPEN, kernel)
        image1, modified, hier = cv2.findContours(modified_plate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for m in modified:
            rect = cv2.minAreaRect(m)
            width_m = rect[1][0]
            height_m = rect[1][1]
            if width_m > 0 and height_m > 0:
                height_width_ratio_m = height_m / width_m
                if (height_width_ratio_m > 0.4) and (height_width_ratio_m < 6) and (height_m * width_m > 150):
                    # print height_width_ratio_m
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    x, y, w, h = cv2.boundingRect(m)
                    roi_m = modified_plate[y:y + h, x:x + w]
                    cv2.drawContours(modified_plate, [box], 0, (255, 255, 255), 1)
                    # cv2.imwrite(str(index) + '.jpg', roi)
                    index_array.extend([index])
                    roi_array_m.append(roi_m)
        if show_steps == True:
            original_plate_name = "cropped_number_plate" + str(i)
            # cv2.imshow(str(original_plate_name), cv2.resize(roi_array[i], (400, 100)))
            cv2.imshow(str(modified_plate_name), cv2.resize(modified_plate, (400, 100)))
    print "--------------------------"

    print "Number plate letter extraction atvaizdvimas"
    # funkcija kuri atvaizduoja raides is turimo konturo
    for j in range(0, len(roi_array_m)):
        letter = "Detected letter" + str(j)
        # cv2.imwrite(letter + '.jpg', roi_array_m[j])
        if show_steps == True:
            cv2.imshow(letter, cv2.resize(roi_array_m[j], (53, 90)))
            # cv2.imshow(letter, roi_array_m[j])
    print "---------------------------------"




ESC = 27
while True:
    keycode = cv2.waitKey()
    if keycode != -1:
        # keycode & amp = "0xFF"
        if keycode == ESC:
            break
cv2.destroyAllWindows()
