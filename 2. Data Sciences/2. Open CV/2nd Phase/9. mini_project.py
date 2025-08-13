# i have a project now take the file location form user input give him teh option what he want to do 
# drawline, circle, rectnagle, resizing,cropping,flipping ,rotating, and the seected option should do
#  the respective task then ask him wheter he want to save the image otr not if ues save it as well

import cv2

# Step 1: Take file location from user
image_path = input("Enter the path of the image: ")
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load image.")
    exit()

# Step 2: Show menu
print("\nSelect an operation:")
print("1. Draw Line")
print("2. Draw Circle")
print("3. Draw Rectangle")
print("4. Resize")
print("5. Crop")
print("6. Flip")
print("7. Rotate")

choice = int(input("Enter your choice (1-7): "))

# Step 3: Perform the selected operation
if choice == 1:
    # Draw line
    x1, y1 = map(int, input("Enter start point (x1 y1): ").split())
    x2, y2 = map(int, input("Enter end point (x2 y2): ").split())
    color = tuple(map(int, input("Enter color in B G R: ").split()))
    thickness = int(input("Enter thickness: "))
    cv2.line(img, (x1, y1), (x2, y2), color, thickness)

elif choice == 2:
    # Draw circle
    x, y = map(int, input("Enter center point (x y): ").split())
    radius = int(input("Enter radius: "))
    color = tuple(map(int, input("Enter color in B G R: ").split()))
    thickness = int(input("Enter thickness (-1 for filled): "))
    cv2.circle(img, (x, y), radius, color, thickness)

elif choice == 3:
    # Draw rectangle
    x1, y1 = map(int, input("Enter top-left corner (x1 y1): ").split())
    x2, y2 = map(int, input("Enter bottom-right corner (x2 y2): ").split())
    color = tuple(map(int, input("Enter color in B G R: ").split()))
    thickness = int(input("Enter thickness (-1 for filled): "))
    cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

elif choice == 4:
    # Resize
    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))
    img = cv2.resize(img, (width, height))

elif choice == 5:
    # Crop
    y1, y2 = map(int, input("Enter row range (y1 y2): ").split())
    x1, x2 = map(int, input("Enter column range (x1 x2): ").split())
    img = img[y1:y2, x1:x2]

elif choice == 6:
    # Flip
    print("Flip codes: 0 = vertical, 1 = horizontal, -1 = both")
    flip_code = int(input("Enter flip code: "))
    img = cv2.flip(img, flip_code)

elif choice == 7:
    # Rotate
    (h, w) = img.shape[:2]
    angle = float(input("Enter rotation angle in degrees: "))
    scale = float(input("Enter scale (1.0 = same size): "))
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, scale)
    img = cv2.warpAffine(img, matrix, (w, h))

else:
    print("Invalid choice!")
    exit()

# Step 4: Show the result
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 5: Ask to save
save_choice = input("Do you want to save the image? (yes/no): ").lower()
if save_choice == "yes":
    save_path = input("Enter the file name to save (with extension): ")
    cv2.imwrite(save_path, img)
    print(f"Image saved as {save_path}")
