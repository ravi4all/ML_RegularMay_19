import cv2
dataset = cv2.CascadeClassifier('data.xml')

capture = cv2.VideoCapture(0)
while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        cv2.imshow('result',img)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()
capture.release()