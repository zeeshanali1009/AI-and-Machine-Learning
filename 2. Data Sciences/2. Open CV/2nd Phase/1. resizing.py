# resized  = cv2.resize(src,dsize, fx,fy, interpolation)
# src is the input image 
# dsize means desizing the image by width and height wise
# fx,fy are the scales 
# interpolation covers the quality.


import cv2
image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\2nd Phase\picture.jpg")

if image is None:
    print("Image not found!")
else:
    print("Image Loaded!")


    resized  = cv2.resize(image, (300,300))

    cv2.imshow("Original Image: ", image)
    cv2.imshow("Resized Image: ", resized)

    cv2.imwrite("Rezized_output", resized)

    cv2.waitkey(0)
    cv2.destroyallwindows()


