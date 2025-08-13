# M= cv2.getrotationmatrix(center, angle , scale)
# tells how will be rotation carried out clockwise anticlock wise 
# angle represents that how many degrees the image will be rotated
# scale means how much teh image will be zoomed in or zoom out in the rotation

# rotated_image  = cv2.warpaffine|(image, M,(width, height))
import cv2
image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\2nd Phase\picture.jpg")


if image is not None:
    (h,w) = image.shape[:2]
    center  = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated  = cv2.warpAffine(image, M , (w,h))


    cv2.imshow("Original", image)
    cv2.imshow("Rotated", rotated)
    cv2.waitkey(0)
    cv2.destroyallwindows()
else:
    print("Image could not be loaded.")




