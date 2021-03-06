# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:23:00 2020

@author: Zhang Jingheng
"""
import numpy as np
import cv2

path1= "F:/face/3.jpg"

pathf1 = "D:\\anaconda3\\pkgs\\libopencv-4.4.0-py37_2\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml"
pathf2 = "D:\\anaconda3\\pkgs\\libopencv-4.4.0-py37_2\\Library\\etc\\haarcascades\\haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(pathf1)
eye_cascade = cv2.CascadeClassifier(pathf2)

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread(path1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

