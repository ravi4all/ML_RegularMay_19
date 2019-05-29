import cv2
import numpy as np
dataset = cv2.CascadeClassifier('data.xml')

capture = cv2.VideoCapture(0)

faceData = []
username = input("Enter your name : ")
while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

            faceArray = gray[y:y+h,x:x+w]
            faceArray = cv2.resize(faceArray,(50,50))
            if len(faceData) < 50:
                faceData.append(faceArray)
                print(len(faceData))

        cv2.imshow('result',img)

        if cv2.waitKey(1) == 27 or len(faceData) >= 50:
            break

faceData = np.asarray(faceData)
np.save(username+'.npy', faceData)
cv2.destroyAllWindows()
capture.release()