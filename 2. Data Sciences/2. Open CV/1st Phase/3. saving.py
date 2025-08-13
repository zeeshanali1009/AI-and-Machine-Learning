# cv2.imwrite("filename", image)
import cv2

image   = cv2.imwrite("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Machine Learning\2. Open CV\1st Phase\picture.jpg")

# this function saves the image after the writing process has been completed
if image is not None:
    success = cv2.imwrite("Successfully_saved.png")
    if success:
        print("Image has been saved successfully.")
    else:
        print("Image has not been saved successfully.")
else:
    print("Image has not been loaded.")