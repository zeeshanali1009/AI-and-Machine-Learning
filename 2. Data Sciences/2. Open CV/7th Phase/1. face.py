import cv2

# Load face cascade
face_cascade = cv2.CascadeClassifier(
    r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\7th Phase\Resources\haarcascade_frontalface_alt.xml"
)

# Start webcam
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show result
    cv2.imshow("Webcam Face Detector", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and close
capture.release()
cv2.destroyAllWindows()
