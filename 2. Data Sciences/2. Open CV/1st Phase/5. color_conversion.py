# Converts an image from one color space to another.
# cv2.cvtColor(src, code)


image   = cv2.imread("C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Machine Learning\2. Open CV\1st Phase\picture.jpg")

# this function is used to convert the color from one form to another form using the particular conditions
if image is not None:
    gray = cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale_image.png", gray)
    cv2.waitkey(0)
    cv2.destroyallwindows()
    
else:
    print("Image has not been loaded.")