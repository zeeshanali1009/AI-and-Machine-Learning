import cv2

# For opening the video or loading it so that we can work with the frames
# cv2.VideoCapture(source)
# 0  if using the laptop webcam 
# 1  if external webcam is used

capture = cv2.VideoCapture(0)  # Correct: 'VideoCapture', not 'videocapture'

while True:
    ret, frame = capture.read()  # Read a frame

    if not ret:
        print("Could not read.")
        break

    cv2.imshow("Webcam feed", frame)  # Show the live feed

    # waitKey waits for 1 ms; if 'q' is pressed, loop will break
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Correct: 'waitKey', not 'waitkey'
        print("Quitting")
        break

capture.release()            # Release the webcam
cv2.destroyAllWindows()      # Correct: 'destroyAllWindows', not 'destroyallwindows'
