import cv2
import numpy as np
img= cv2.imread('cards.jpg')
width,height = 600,400
pts1 = np.float32([[2533,557],[3557,649],[2401,1969],[3533,2105]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))



cv2.imshow('cards',cv2.resize(img,(600,400)))
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)