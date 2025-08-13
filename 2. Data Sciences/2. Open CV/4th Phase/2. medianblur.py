import cv2

# Note: Use raw string (r"...") or double backslashes for Windows file paths
image = cv2.imread(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\4th Phase\picture.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# MedianBlur syntax:
# cv2.medianBlur(src, kernel size)
# clean the image by replacing each pixel with the central one
# deiiference
# guassain  = average of all the pixels
# median = middle value from all pixels
blurred = cv2.medianBlur(image, 7)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)

cv2.waitKey(0)              # Wait until any key is pressed
cv2.destroyAllWindows()     # Close all OpenCV windows
