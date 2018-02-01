import numpy as np
import cv2
import os
import keyboard

itterate = 0
path = os.getcwd()
index_array = []
show_img = True # pazet, kaip padaryti global, kad eitu per visus laukus.
char_array = []
global index
index = 1
previous_index = 0

print "This function will take u through the process of assigning your templates to chars"
def learn_Chars_draw_boxes_and_itterate (index):
    # Naudojamos funkcijos

    # Naudojami kintamiejia
    global index_arraya
    global char_resized

    # Pradinis vaizdas
    char_img = cv2.imread(path + '\Learn_chars.png', cv2.IMREAD_REDUCED_COLOR_2) #naudoju reduced color, nes cv nepriima kitokiu
    # Konvertuoja i grayscale ir  suranda konturus
    char_resized = cv2.resize(char_img, (800, 340))
    char_gray = cv2.cvtColor(char_resized, cv2.COLOR_BGR2GRAY)
    ret, char_threshed = cv2.threshold(char_gray, 120, 500, cv2.THRESH_BINARY_INV)
    cv2.imshow("Learn_chars", char_threshed)
    image, contours, hier = cv2.findContours(char_threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # for c in contours:
    rect = cv2.minAreaRect(contours[index])
    width = rect[1][0]
    height = rect[1][1]
    height_width_ratio = height / width
    if (height_width_ratio > 0.4) and (height_width_ratio < 7) and (height * width > 300) or (height_width_ratio < 0.3):
        box = cv2.boxPoints(rect)
        box = np.int0(box)  # lyg ir box vertes i integer paverciamos
        x, y, w, h = cv2.boundingRect(contours[index]) # papraso, kad bounding rect grazintu x, y, w, h
        char = char_threshed[y:y + h, x:x + w] # Keikvieno img paima koordinates ir saugoja roi, kuri prideda i char array
        char_array.append(char)
        # cv2.imwrite(str(index) + '.jpg', roi)
        cv2.drawContours(char_resized, [box], 0, (0, 0, 255), 1)
        index_array.extend([index])
    print "I have finnished my job"

pressed = False
while True:
    if keyboard.is_pressed('a') and pressed == False:
        index += 1
        learn_Chars_draw_boxes_and_itterate(index)
        cv2.imshow("Dezutes", char_resized)
        print index
        pressed = True
    else:
        index = 1
        pressed = False

            # i = 2
            # while i < n:
            #     if something:
            #         do
            #         something
            #         i += 1
            #     else:
            #         do
            #         something else
            #         i = 2  # restart the loop


a


    # print contours[1]

# Pikseliu vidurkinimo funkcija


# Kviecia funkcijas


# Neleidzia uzsidaryti
ESC = 27
while True:
    keycode = cv2.waitKey()
    if keycode != -1:
        # keycode & amp = "0xFF"
        if keycode == ESC:
            break
cv2.destroyAllWindows()

# BACKLOG
#   Dezutes ima ne mazesnes nei nustatytas plotas.
#   Dezutes pasvirimo kampas
#   Raidziu atpazinimo metu padaryti, kad vartotojas blogai atpazintas raides galetu pazymeti, kaip blogas ir jas ismestu is masyvo
#   Iteratinimas nuo kairio sono virsaus.
#   Iteratina masyva tik, kai gauna klaviaturos spustelejima.
#   Saugo viska i faila, realiai tik masyva, kuri susieja su masyvu, kuris kuriamas is mygtuku spaudimo, structure array
#   Palyginimo funckija: paima raide, ismesdami(minusuodami) neatitikusius konturus, paskaiciuoja kuris is ju turi maziausiai
#    likusio ploto ir tada deda tris galimus variantus i masyva, kuri rusiuoja(plota, atminusuotas plotas turi tureti labai mazai baltu pikseliu)
#    realiai appendina i simpla masyva, kurio kas trecia reiksme yra svarbiausia.


#   GUI, meniu, kuriame yra pasirinkimas ka daryti:
#       Apmokymas - Virsuje parasyta ka reikia daryti atsiradus paryskintai raidei
#       Atpazinimas - Ikeli img, jis parodomas, tada parodomas isskirtas numeris, tada kiekviena raide, ir ta raide, kuria atitinka, tik pora mygtuku, galima pasirinkti kuria tiketina raide rinktis
#       Info - pateikiama informacija, per kiek laiko uzima skriptu vykdymas ir t.t.
#       Saltiniai - aprasomos visos naudotos funkcijos su pvz ir argumentuojama kodel butent jos buvo pasirinktos.
#

