# cv2.line(image, pt1, pt2, thickness)
# pt1(x,y)  = right and down 
# pt2(x,y)  = left and down 
import cv2
image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\2nd Phase\picture.jpg")


if image is not None:
    pt1  = (50,100)
    pt2  = (300,100)
    color  = (255,0,0)  # blue color 
    thickness = 2

    cv2.line(image, pt1, pt2, color, thickness)


   
    cv2.waitkey(0)
    cv2.destroyallwindows()
else:
    print("Image could not be loaded.")