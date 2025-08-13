import cv2
import numpy as np

# Step 1: Take image path from user
image_path = input("Enter full path of the image: ").strip()
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not load image. Check path.")
    exit()

# Step 2: Ask user for the operation
print("\nChoose an operation:")
print("1. Simple Thresholding")
print("2. Canny Edge Detection")
print("3. Bitwise Operations")
choice = input("Enter choice (1-3): ").strip()

processed = None

# Step 3: Perform chosen operation
if choice == "1":
    # Simple Thresholding
    _, processed = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

elif choice == "2":
    # Canny Edge Detection
    processed = cv2.Canny(image, 100, 200)

elif choice == "3":
    # Create shapes for demonstration of bitwise ops
    img1 = np.zeros((300, 300), dtype="uint8")
    img2 = np.zeros((300, 300), dtype="uint8")
    cv2.circle(img1, (150, 150), 100, 255, -1)
    cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

    bitwise_and = cv2.bitwise_and(img1, img2)
    bitwise_or = cv2.bitwise_or(img1, img2)
    bitwise_not = cv2.bitwise_not(img1)

    cv2.imshow("Circle", img1)
    cv2.imshow("Rectangle", img2)
    cv2.imshow("Bitwise AND", bitwise_and)
    cv2.imshow("Bitwise OR", bitwise_or)
    cv2.imshow("Bitwise NOT", bitwise_not)

else:
    print("Invalid choice.")
    exit()

# Step 4: Show results
if processed is not None:
    cv2.imshow("Original Image", image)
    cv2.imshow("Processed Image", processed)

# Step 5: Option to save
if processed is not None:
    save = input("Do you want to save the processed image? (y/n): ").strip().lower()
    if save == "y":
        save_path = input("Enter file name (with extension): ").strip()
        cv2.imwrite(save_path, processed)
        print(f"Image saved as {save_path}")

cv2.waitKey(0)
cv2.destroyAllWindows()
