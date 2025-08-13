# cv2.puttext(image,text, org , font, fontscale, color , thickness)
# org represents the bottom left corner (x,y)

import cv2
image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\2nd Phase\picture.jpg")


if image is not None:
    cv2.puttext (image, "Hello, this is text", (50,100),cv2.FONT_POPPINS, 1.2,   color= (255,0,0), thickness= (2))
    
    cv2.waitkey(0)
    cv2.destroyallwindows()
else:
    print("Image could not be loaded.")