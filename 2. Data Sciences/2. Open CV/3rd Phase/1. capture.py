# for opening the video or loading it so that we can work with the frames
# cv2.videocapture(source)
# 0  if using the laptop webcam 
# 1 if external webcam is used

import cv2

capture  =  cv2.videocapture(0)

while (True):
    ret, frame = capture.read()

    if not ret:
        print("Could not read.")
        break

    cv2.imshow("Webcam feed", frame)

    if cv2.waitkey(1) & 0xFF == ord('q'):       # odd function waits for 1 ms and if q press the loops will be broken
        print("Quitting")
        break

capture.release()
cv2.destroyallwindows()






