import numpy as np
import cv2

dest="/home/hbm22/Experiments/25_01_16/"
img = cv2.imread("/home/hbm22/Pictures/hmmetria/BO097Osteoide2.PNG")
cv2.imwrite(f'{dest}org.jpg', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite(f'{dest}hsv.jpg', hsv)

mask = cv2.inRange(hsv, (5,75,25), (25,255,255))

imask = mask>0
orange = np.zeros_like(img, np.uint8)
orange[imask] = img[imask]

yellow = img.copy()
hsv[...,0] = hsv[...,0]+20
yellow[imask] = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)[imask]
yellow = np.clip(yellow, 0, 255)
cv2.imwrite(f'{dest}yellow.jpg', yellow)

nofish = img.copy()
nofish = cv2.bitwise_and(nofish, nofish, mask=(np.bitwise_not(imask)).astype(np.uint8))
cv2.imwrite(f'{dest}nocolor.jpg', nofish)
