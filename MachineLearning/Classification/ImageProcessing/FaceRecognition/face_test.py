import numpy as np
import cv2

dataset = cv2.CascadeClassifier('data.xml')
font = cv2.FONT_HERSHEY_COMPLEX
def predict(coef,face):
    y_pred = coef[0]
    for row in face:
        for i in range(len(row)):
            y_pred += coef[i+1] * row[i]
    return 1 / (1 + np.exp(-y_pred))

coef = np.load('coef.npy')
# print(coef.shape)
capture = cv2.VideoCapture(0)
usernames = dict()
# print(files[0][:-4])

username = {0:'Ravi_1', 1:'Ravi_2'}

while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face ,(50,50))
            label = predict(coef,face)
            print(label[0])
            text = username[int(label)]

            cv2.putText(img,text,(x,y),font,1,(255,0,0),2)
        cv2.imshow('result',img)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()
capture.release()