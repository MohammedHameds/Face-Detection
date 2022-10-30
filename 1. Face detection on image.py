import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread('Lenna.png',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray,1.1,5)
(x,y,w,h) = faces[0]

cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
cv2.imshow('Cascade classifier',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

