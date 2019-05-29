import cv2
import numpy as np
import glob
faceData = cv2.CascadeClassifier('data.xml')

files = glob.glob('*.npy')
# files = ['Ravi1.npy','Ravi1.npy']

face_1 = np.load(files[0]).reshape(200,-1)
face_2 = np.load(files[1]).reshape(200,-1)

data = np.concatenate([face_1,face_2])
# print(faces.shape)
labels = np.zeros((data.shape[0],1))
# print(labels.shape)
labels[:200,:] = 0.0
labels[200:,:] = 1.0

def dist(x2,x1):
    return np.sqrt(sum((x2 - x1) ** 2))

def knn(x,train,k=5):
    n = train.shape[0]
    # print(train.shape, x.shape)
    distance = []
    for i in range(n):
        distance.append(dist(train[i],x))
    distance = np.asarray(distance)
    sortedLabels = np.argsort(distance)
    lab = labels[sortedLabels][:k]
    count = np.unique(lab,return_counts=True)
    return count[0][np.argmax(count[1])]

dataset = cv2.CascadeClassifier('data.xml')
font = cv2.FONT_HERSHEY_COMPLEX

capture = cv2.VideoCapture(0)

username = {0:'Ravi', 1:'Sukhvinder'}

while True:
    ret,img = capture.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

            face = img[y:y+h, x:x+w,:]
            face = cv2.resize(face ,(50,50))
            label = knn(face.flatten(), data)
            # print(label[0])
            text = username[int(label)]
            cv2.putText(img,text,(x,y),font,1,(255,0,0),2)
        cv2.imshow('result',img)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()
capture.release()
