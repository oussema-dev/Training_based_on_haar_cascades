import numpy as np
import cv2
import time

test_cascade = cv2.CascadeClassifier('test.xml')

cap = cv2.VideoCapture(0)
time.sleep(1)

while 1:
    ret, img = cap.read()
    resize = cv2.resize(img,(320,240))
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    test = test_cascade.detectMultiScale(gray,1.01,10)   
   
    for (x,y,w,h) in test:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        print"Found test"

    cv2.imshow('img',gray)    
    if cv2.waitKey(30) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
