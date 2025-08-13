# mini video-handling project from a user’s perspective where:
# The program asks the user if they want to capture from webcam or load a video file
# Displays the video in real time
# Asks if they want to save the output
# Saves the video if requested

import cv2

# Step 1: Ask user for video source
source_choice = input("Enter 'w' for webcam or 'f' for video file: ").lower()

if source_choice == 'w':
    cap = cv2.VideoCapture(0)  # Webcam
elif source_choice == 'f':
    file_path = input("Enter the path of the video file: ")
    cap = cv2.VideoCapture(file_path)
else:
    print("Invalid choice!")
    exit()

# Step 2: Ask if user wants to save the videwo
save_choice = input("Do you want to save the video? (yes/no): ").lower()

if save_choice == "yes":
    save_path = input("Enter output file name (e.g., output.avi): ")

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 20  # default 20 if can't read

    # Video writer setup
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(save_path, fourcc, fps, (frame_width, frame_height))
else:
    out = None

# Step 3: Read and display video frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow("Video Feed", frame)

    # Save if requested
    if out is not None:
        out.write(frame)

    # Quit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 4: Release resources
cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()
