# Drawing different shapes on image

import numpy as np
import cv2

    # reading the image, flag number '0' is for gray image and 1 is for coloured image
    # else we can use a black image created by numpy
#img = cv2.imread('lena.jpg',1)

    # we are creating an image using numpy zeros
    # 1st argument is the height of image
    # 2nd argument is width of image
    # 3rd argument is ending point (co-ordinate) for the line in tuple form
    # 4th argument is data type
img = np.zeros([512, 512, 3], np.uint8)

    # will create a ----Straight line-------
    # 1st argument is the image over which we will over-write
    # 2nd argument is starting point (co-ordinate) for the line in tuple form
    # 3rd argument is ending point (co-ordinate) for the line in tuple form
    # 4th argument is rgb colour code in tuple form
    # 5th argument is width of the line
img = cv2.line(img, (12,12), (221,12), (147,9644), 12)

    # will create a ----arrowed line------- with same argument pattern
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10)

    # will create a ------rectangle---------- with same argument pattern
    # Here the 2 points represent 2 vertices of a rectangle
    # (x1,y1)________
    # |             |
    # |             |
    # |             |
    # -----------(x2,y2)
img = cv2.rectangle(img, (300,428), (467,111), (0,0,255), 8)

    # will create a ----Circle-------
    # 1st argument is the image over which we will over-write
    # 2nd argument is centre of the circle in tuple form
    # 3rd argument is radius for the circle
    # 4th argument is rgb colour code in tuple form
    # 5th argument is width of the line
    # instead of 10 we can write -1 for a filled circle
img = cv2.circle(img, (180,380), 82, (0,255,0), -1)

    # here font selected as 'HERSHEY_SIMPLEX'
font=cv2.FONT_HERSHEY_SIMPLEX
    # 1st argument is the image variable
    # 2nd argument is the text to be written
    # 3rd argument is co-ordinate in tuple form
    # 4th argument is font variable
    # 5th argument is rgb colour code in tuple form
    # 6th argument is thickness of font
    # 5th argument is line type
img = cv2.putText(img, 'OpenCV Project', (10,440), font, 4, (255,255,255), 10,cv2.LINE_AA)





    # name of displayed window is 'image'
cv2.imshow('image', img)
    # it takes user input of keys
cv2.waitKey(0)
    # closing the window
cv2.destroyAllWindows()
