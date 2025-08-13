# cv2.videowriter(filename, codec, fps, frame_size)
# codec means the compression format like mp4
# fps frame per second decides the smoothness 
# framesize represents the width and height of the frames


import cv2 

camera   = cv2.videocapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec  = cv2.videowriter_fourcc("XVID")
recorder = cv2.videowriter("my_video", codec, 20, (frame_width, frame_height))

while True:
    success, image  = camera.read()


    if not success():
        break


    recorder.write(image)

    cv2.imshow("Recording live", image)


