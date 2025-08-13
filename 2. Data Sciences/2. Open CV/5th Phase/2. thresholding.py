#  threshold_image  = cv2.threshold(image, thresh_value, max_value, method)
import cv2

image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\5th Phase\picture.jpg", cv2.IMREAD_GRAYSCALE)

ret, thresh_img  = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image" , image)
cv2.imshow("Threshold Image", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()