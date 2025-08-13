# imshow() — displays image
# waitKey() — waits for a key press
# destroyAllWindows() — closes all image windows
import cv2

image   = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Machine Learning\2. Open CV\1st Phase\picture.jpg")

# this function is used to dispaly the image after the loading been completed
if image is not None:
    cv2.imshow("Image showing!", image)     # shows the image
    cv2.waitkey(0)                          # wait for the user to input using just one key and close the image window
    cv2.destroyallwindows()                 # destroy all the windows related to the image
else:
    print("Image has not been loaded.")