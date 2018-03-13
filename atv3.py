import cv2
import numpy as np

template = cv2.imread('madfox.jpg',0)
face_w, face_h = template.shape[::-1]



cv2.namedWindow('Image')

cap = cv2.VideoCapture(0)

threshold = 1
ret = True

while ret :
    ret, img = cap.read()

    #flip the image  ! optional 
    img = cv2.flip(img,1)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    if len(res):
        location = np.where( res >= threshold)
        for i in zip(*location[::-1]):
            #puting  rectangle on recognized erea 
            cv2.rectangle(img, pt, (pt[0] + face_w, pt[1] + face_h), (0,0,255), 2)

    cv2.imshow('image',img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()