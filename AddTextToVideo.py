import  cv2
    # Here '0' representing camera number, can be 2,3 for 2nd and 3rd camera respectively
    # cap stores all the video captured
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # we are setting the frame size .
    # 3 is for frame height
    # 4 is for frame width
    # we can give any resolution to it but it will give only the available resolution for the camera
cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))

    # we are running loop definitely
while (cap.isOpened()):
        # read() method will read frame and return true if frame is available
        # value returned by read stored in frame
        # ret will be true if frame is true
    ret, frame =cap.read()
    if ret == True:
            # font choosen here is FONT_HERSHEY_SIMPLEX an stored in font
        font = cv2.FONT_HERSHEY_SIMPLEX


            # To print frame of the window on video streaming window un comment this
            # text stores texts to be printed on the video window
        text = 'Width :'+ str(cap.get(3)) + ' Height : '+ str(cap.get(4))

            # -----for printing date and time on the video window----------------------
            # datet = str(datetime.datetime.now())

            # frame variable which streams video over-written with text
        frame= cv2.putText(frame, text, (10,50), font, 2, (0, 255, 255), 4, cv2.LINE_AA)

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