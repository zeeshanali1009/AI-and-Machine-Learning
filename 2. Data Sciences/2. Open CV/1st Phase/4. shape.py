# shape attribute returns the follwing things as 
# Height → number of pixel rows
# Width → number of pixel columns
# Channels → number of color components per pixel
import cv2

image   = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Machine Learning\2. Open CV\1st Phase\picture.jpg")

# shape is not the function it is an attribute which gives the details about the image 
# it gives the height , width , channel (rgb, graychannel)
if image is not None:
    h,w,c =  image.shape
    print("Image loaded!\n Height {h}\n Width {w}\nChannel {c}")
else:
    print("Image has not been loaded.")