import cv2

dataset = cv2.CascadeClassifier('data.xml')
img = cv2.imread('modi.jfif')
face = dataset.detectMultiScale(img)
# print(face)
for x,y,w,h in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
cv2.imwrite('result.jpg',img)