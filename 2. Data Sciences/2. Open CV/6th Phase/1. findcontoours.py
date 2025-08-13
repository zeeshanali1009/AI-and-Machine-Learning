# contours, heirarchy = cv2.findcontours (image, mode , method)
# image which will be in binary mode 
# mode represents the retreival mode treee, external , 
# how many counters and what kind of contours external gives 
# the outer most tree will give all shapes present in the heirarchy 
# method of approximation how much details of the contour to be detialed 
# cotours saves the list of continuous points 
# heirarchy have the parent to child info
# 
import cv2
image = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\6th Phase\image.png")
gray = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, heirarchy = cv2.findcontours (image, cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)


