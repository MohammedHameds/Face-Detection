import cv2

img = cv2.imread('Lenna.png',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')

faces = face_cascade.detectMultiScale(gray,1.1,5)
(x,y,w,h) = faces[0]

cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

eyes = eye_cascade.detectMultiScale(gray,1.1,4)
for eye in eyes:
    (xx,yy,ww,hh) = eye
    cv2.rectangle(img,(xx,yy),(xx+ww,yy+hh),(0,255,255),2)
 

cv2.imshow('Cascade classifier',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

