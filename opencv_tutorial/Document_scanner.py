import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    imgcontours=img1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            imgcontours= cv2.drawContours(img1, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            # cv2.imshow("result", image)
            # pts=np.float32([[x,y], [w, 0], [0, h], [w, h]])
    return imgcontours
#

# def wrapping_img(img,pts)
#     width, height = 600, 400
#
#     pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
#     matrix = cv2.getPerspectiveTransform(pts1, pts2)
#     imgOutput = cv2.warpPerspective(img, matrix, (width, height))





cap=cv2.VideoCapture(0)
frame_height=640
frame_width=480
cap.set(3,frame_width)
cap.set(4,frame_height)
cap.set(10,150)
while True:
    success, img1 = cap.read()
    img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_canny = cv2.Canny(img_blur, 400, 300)
    # imagethreshold = cv2.threshold(img_blur,180, 255, cv2.THRESH_BINARY_INV)
    imgcontours=getContours(img_blur)
    imgStack=stackImages(0.6,([img1,img_gray],[img_blur,imgcontours]))
    cv2.imshow("Result", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
