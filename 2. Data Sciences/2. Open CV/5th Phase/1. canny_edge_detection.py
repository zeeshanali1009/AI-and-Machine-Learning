# edges  = cv2.canny(image, threshold1, threshold2)
# t1  = minimum limit  
# t2  = maximum limit
# the decisions are been made like if the minimum limit exceeded do this 
# or if the maximum limit exceede do this 
# extracts the outlines , borders so that the filtering is done 
# seperating objects 
# feature extraction
# face recognition

import cv2

image  = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\2. Open CV\5th Phase\picture.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50,150)
cv2.imshow("Original Image" , image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()









