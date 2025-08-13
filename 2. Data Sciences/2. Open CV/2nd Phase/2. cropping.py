# cropped_,image = image[starty:endy, startx: endx]
#  y represents the number of rows 
#  x represents the number of columns 

import cv2
image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\2nd Phase\picture.jpg")


if image is not None:
    cropped  = image[100:200,50:150]


    cv2.imshow("Original", image)
    cv2.imshow("Cropped", cropped)
    cv2.waitkey(0)
    cv2.destroyallwindows()



