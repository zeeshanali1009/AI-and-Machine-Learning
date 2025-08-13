import cv2
import numpy as np

# Use raw string for Windows file paths
image = cv2.imread(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\4th Phase\picture.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Sharpening kernel (must be NumPy array)
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply filter
# ddepth = -1 means output image will have same depth as source
changed = cv2.filter2D(image, ddepth=-1, kernel=sharpen_kernel)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", changed)

cv2.waitKey(0)
cv2.destroyAllWindows()
