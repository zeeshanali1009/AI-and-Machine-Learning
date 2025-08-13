# approx = cv2.approxpolyDP(contour, epsilon, True)
# epsilon:    0.01(epsilon ) *cv2.arclength (contour, tree)
# smaller precise detection   
# large : rough 
# 
# shape                         arclength               epsilon
# small triangle                200px                   2px
# large rectangle               800px                   8px
# circle                        1200px                  12px
import cv2

# Load image
image = cv2.imread(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\6th Phase\image.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    # Approximate contour
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    corners = len(approx)

    # Detect shape based on corners
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    else:
        shape_name = "Circle"

    # Draw the contour
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

    # Get position for text
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    # Put shape name
    cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

# Display result
cv2.imshow("Shape Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
