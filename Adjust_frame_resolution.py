# customising the frame resolutions

import  cv2
    # Here '0' representing camera number, can be 2,3 for 2nd and 3rd camera respectively
    # cap stores all the video captured
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    # we are setting the frame size .
    # 3 is for frame height
    # 4 is for frame width
    # we can give any resolution to it but it will give only the available resolution for the camera
cap.set(3, 100)
cap.set(4, 100)

print(cap.get(3))
print(cap.get(4))

    # we are running loop definitely
while (cap.isOpened()):
        # read() method will read frame and return true if frame is available
        # value returned by read stored in frame
        # ret will be true if frame is true
    ret, frame =cap.read()
    if ret == True:
            # to make image grey from coloured image execute following
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # and replace the following frame attribute with gray
            # as following
            # cv2.imshow ('Stream', gray)

            # Name of the window is frame and the window is reading the 'frame' variable i.e, coloured
            # for coloured video execute the following
            # cv2.imshow ('Stream', frame)
        cv2.imshow('Stream', frame)

            # ord reads the key pressed, if q is pressed window will quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    # after capturing video we need to release cache files
cap.release()
cv2.destroyAllWindows()