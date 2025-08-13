import cv2

# Note: Use raw string (r"...") or double backslashes for Windows file paths
image = cv2.imread(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\4th Phase\picture.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# GaussianBlur syntax:
# cv2.GaussianBlur(src, (kernel_width, kernel_height), sigmaX)
# softens the image , reduces the sharpness, removes the noise
# kernel size is the windows size always the odd 
# sigma means how strongly you want the blur

blurred = cv2.GaussianBlur(image, (7, 7), 0)
# 3,3  light blur   will blend central pixel with other 8 pixel
# 9,9 strongblur    will blend central pixel with other 80 pixel
# 21,21 super strong blur   will blend central pixel with other remaining pixel
# that is how the acne, noise is removed 
# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)

cv2.waitKey(0)              # Wait until any key is pressed
cv2.destroyAllWindows()     # Close all OpenCV windows
