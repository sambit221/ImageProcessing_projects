import cv2

    # Here '0' representing camera number, can be 2,3 for 2nd and 3rd camera respectively
    # cap stores all the video captured
cap=cv2.VideoCapture(0)

    # xvid is fourcc code, and fourcc is a class
fourcc= cv2.VideoWriter_fourcc(*'XVID')

    # 1st argument is name of output
    # 2nd one is output from fourcc variable(that includes fourcc class)
    # 3rd argument is resolutions per second i.e, 20.0 here i have given
    # 4th argument is a tuple that includes dimensions of the window
out=cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

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
        out.write(frame)
        cv2.imshow('Stream', frame)

            # ord reads the key pressed, if q is pressed window will quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    # Here it will print the dimensions of the window
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    # after capturing video we need to release cache files
cap.release()
out.release()
cv2.destroyAllWindows()