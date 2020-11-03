# print the coordinates and BGR value on the image window wherever the mouse click is detected
# here it will detect left & right click

import numpy as np
import cv2

# many mouse events are available in cv2 library
# events = { i for i in dir(cv2) if 'EVENT' in i}
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) +', ' +str(y)
            # fifth argument is font scale
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN :
        blue =  img[y, x, 0]
        green = img[y, x, 1]
        red =   img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) +', ' +str(green)+', ' +str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

img= np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()