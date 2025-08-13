# cv2.circle(image,center, radius , color , thickness)
# center represetnts the location
# radius represents the size

import cv2
image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\2nd Phase\picture.jpg")


if image is not None:
    cv2.circle(image, center  = (150,150), radius = (50), color= (255,0,0), thickness= (2))
    # thickness  = -1 will fill the circle
    cv2.waitkey(0)
    cv2.destroyallwindows()
else:
    print("Image could not be loaded.")