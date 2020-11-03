# Reading an image and copying it to another variable

import cv2

    # reading an image and storing its matrix data to img
    # reading the image, flag number '0' is for gray image and 1 is for coloured image
img= cv2.imread('lena.jpg', -1)
print(img)

    # creating an image window
cv2.imshow('image', img)

    # it takes user input of keys
k=cv2.waitKey(0)

    # if ESC is pressed then will clear the window
if k== 27:
    cv2.destroyAllWindows()

    #if S is pressed then will save whatever is on the window to the following path
elif k == ord('s'):

    # creating an image file by copying from image window
    cv2.imwrite('lena_copy.png', img)

    # closing the window
    cv2.destroyAllWindows()