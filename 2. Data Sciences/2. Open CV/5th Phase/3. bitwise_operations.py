import cv2
import numpy as np

# Create two black images
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# Draw a white circle on img1
cv2.circle(img1, (150, 150), 100, 255, -1)

# Draw a white rectangle on img2
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

# Bitwise operations
bitwise_and = cv2.bitwise_and(img1, img2)   # Intersection area
bitwise_or = cv2.bitwise_or(img1, img2)     # Union area
bitwise_not = cv2.bitwise_not(img1)         # Invert colors of img1

# Display images
cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
