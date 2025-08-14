import cv2

# Load cascades
face_cascade = cv2.CascadeClassifier(
    r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\7th Phase\Resources\haarcascade_frontalface_alt.xml"
)
eye_cascade = cv2.CascadeClassifier(
    r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\7th Phase\Resources\haarcascade_eye.xml"
)
smile_cascade = cv2.CascadeClassifier(
    r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\7th Phase\Resources\haarcascade_smile.xml"
)

# Start webcam
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Draw face rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Region of interest for eyes and smile
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes):
            cv2.putText(frame, "Eyes Detected", (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

        # Detect smile
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles):
            cv2.putText(frame, "Smiling", (x, y - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("Smart Face Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
