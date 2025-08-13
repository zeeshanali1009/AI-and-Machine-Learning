# contours, heirarchy = cv2.findcontours (image, mode , method)
# image which will be in binary mode 
# mode represents the retreival mode treee, external , 
# how many counters and what kind of contours external gives 
# the outer most tree will give all shapes present in the heirarchy 
# method of approximation how much details of the contour to be detialed 
# cotours saves the list of continuous points 
# heirarchy have the parent to child info
# drawcounters(image, contours, contour_index, color, thickness)
# it is used to show the contours
# counter_index tells which shape to draw:  0 first ,1 second , -1 all 
import cv2

# Correct file path usage
image = cv2.imread(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\6th Phase\image.png")

# Convert to grayscale (correct conversion code)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold to get binary image
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Draw contours (-1 means draw all)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Display result
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


