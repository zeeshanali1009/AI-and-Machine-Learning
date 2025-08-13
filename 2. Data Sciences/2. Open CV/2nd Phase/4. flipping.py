# fipped_image = cv2.flip(image, flipcoat)
# 0 flip vertically , top to bottom 
# 1 flip vertically , left to right
# -1 flip both horizontally and vertically as well

import cv2
image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\2nd Phase\picture.jpg")


if image is not None:
    flipped_horizontally = cv2.flip(image, 1)
    flipped_vertically = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)


    cv2.imshow("Original", image)
    cv2.imshow("Flipped horizonatally", flipped_horizontally)
    cv2.imshow("Fliped Vertically", flipped_vertically)
    cv2.imshow("Flipped both ways", flipped_both)
   
    cv2.waitkey(0)
    cv2.destroyallwindows()
else:
    print("Image could not be loaded.")


