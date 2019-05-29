import cv2

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread('modi.jfif')
while True:
    cv2.imshow('result', img)
    cv2.rectangle(img,(100,100),(300,300),(0,0,255),5)
    cv2.putText(img,"Modi Ji",(20,20),font,1,(255,0,0),2)
    if cv2.waitKey(1) == 27:
        break