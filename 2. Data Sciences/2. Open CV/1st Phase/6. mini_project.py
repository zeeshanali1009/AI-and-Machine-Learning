# now i have amini project t do about i haveto load an image then grayscale it then show it and then save it as well now it must ask the
#  user about the location of the file as input and the name of teh file to be stored after all the operations 
import cv2

# Step 1: Ask the user for the image path
image_path = input("Enter the path of the image file: ")

# Step 2: Load the image
image = cv2.imread(image_path)

# Check if image is loaded successfully
if image is None:
    print("Error: Could not load image. Please check the path.")
    exit()

# Step 3: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 4: Display the grayscale image
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 5: Ask the user for output file name
output_name = input("Enter the name of the file to save (e.g., output.jpg): ")

# Step 6: Save the grayscale image
cv2.imwrite(output_name, gray_image)
print(f"Grayscale image saved as {output_name}")
