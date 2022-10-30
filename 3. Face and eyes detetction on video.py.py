import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')
                                    
                                    
                                    
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,4)
        
        for (x,y,w,h) in faces : 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(frame, 'Face', (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0) ,2)
            
            eyes = eye_cascade.detectMultiScale(gray,1.1,4) 
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,255),2) 
                cv2.putText(frame, 'Eye', (ex-10,ey-10), cv2.FONT_HERSHEY_SIMPLEX,0.5 , (50,255,50) ,2)
                
    cv2.imshow('Frame' ,frame)         
    if cv2.waitKey(27) == ord('q') :
        break

        
cv2.destroyAllWindows()
cap.release()        

