import cv2
import os

# -------- Step 1: Ask the user for the image path --------
image_path = input("Enter the full image path: ").strip()

# Check if file exists
if not os.path.exists(image_path):
    print("Error: File not found. Please enter a valid path.")
    exit()

# -------- Step 2: Ask the user for threshold value --------
try:
    threshold_value = int(input("Enter threshold value (0-255, default=200): ") or 200)
except ValueError:
    print("Invalid input. Using default threshold value 200.")
    threshold_value = 200

# -------- Step 3: Ask user for epsilon factor --------
try:
    epsilon_factor = float(input("Enter polygon approximation epsilon factor (0.001 to 0.05, default=0.01): ") or 0.01)
except ValueError:
    print("Invalid input. Using default epsilon factor 0.01.")
    epsilon_factor = 0.01

# -------- Step 4: Read and preprocess image --------
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# -------- Step 5: Find contours --------
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# -------- Step 6: Process each contour --------
for contour in contours:
    epsilon = epsilon_factor * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    corners = len(approx)

    # Shape classification
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    else:
        shape_name = "Circle"

    # Draw and label shapes
    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
    x, y = approx.ravel()[0], approx.ravel()[1] - 10
    cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 1)

# -------- Step 7: Display results --------
cv2.imshow("Threshold", thresh)
cv2.imshow("Detected Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
