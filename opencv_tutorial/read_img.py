import cv2
# # front_video capturing
# cap=cv2.VideoCapture(0)
# frame_height=640
# frame_width=480
# cap.set(3,frame_width)
# cap.set(4,frame_height)
# cap.set(10,150)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # frame by frame display of the video
# # front_video capturing
cap=cv2.VideoCapture('Lane Detection Test Video 01.mp4')
frame_height=480
frame_width=640
i=0
while True:
    success, img = cap.read()
    print(success)
    try:
        img = cv2.resize(img, (frame_width, frame_height))
    except:
        break
        print("An exception occurred")


    i=i+1
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break