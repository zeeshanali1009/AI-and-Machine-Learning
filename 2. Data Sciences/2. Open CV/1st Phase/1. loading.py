# image  = cv2.imread("filename", flag)
# flag tells the compiler in which color mode the image will be loaded.
import cv2

image   = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Machine Learning\2. Open CV\1st Phase\picture.jpg")

# this function reads the image or we can say that this function loads the image first step to move forward in computer vision programming.
if image is None:
    print("There is no available image at the given path.")
else:
    print("Image has been loaded successfuly.")