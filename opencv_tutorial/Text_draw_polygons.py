import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(300,300),(0,255,0),4)
cv2.rectangle(img,(0,0),(150,150),(233,0,0),1)
cv2.putText(img,"Tutorial",(0,75),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,155),2)
cv2.imshow('black_imsge',img)
cv2.waitKey(0)