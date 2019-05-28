import cv2
import numpy as np
import glob
faceData = cv2.CascadeClassifier('data.xml')

files = glob.glob('*.npy')

face_1 = np.load(files[0]).reshape(200,-1)
face_2 = np.load(files[1]).reshape(200,-1)

usernames = dict()
# print(files[0][:-4])
for i in range(len(files)):
    usernames[i] = files[i][:-4]

faces = np.concatenate([face_1,face_2])

labels = np.zeros((faces.shape[0],1))
# print(labels.shape)
labels[:200,:] = 0.0
labels[200:,:] = 1.0

def predict(row, coef):
    pred = coef[0]
    for i in range(len(row)):
        pred += coef[i+1] * row[i]
    return 1 / (1 + np.exp(-pred))

def sgd(train,epochs,learningRate):
    coef = [0] * (train.shape[1] + 1)
    for epoch in range(epochs):
        print(epoch)
        for i,row in enumerate(train):
            y_pred = predict(row,coef)
            loss = y_pred - labels[i]
            coef[0] = coef[0] - learningRate * loss
            for i in range(len(row)):
                coef[i+1] = coef[i+1] - learningRate * loss * row[i]
    return coef

def accuracy(pred, actual):
    count = 0
    for i in range(len(pred)):
        if pred[i] == actual[i]:
            count += 1

    return count / len(pred) * 100

def logisticRegression(dataset,epochs,learningRate):
    predictions = []
    print(dataset.shape)
    coef = sgd(dataset,epochs,learningRate)
    print(coef.shape)
    np.save('coef.npy',coef)
    for i in range(len(dataset)):
        y_pred = predict(dataset[i], coef)
        y_pred = round(y_pred)
        predictions.append(y_pred)
    score = accuracy(predictions,labels)
    print(score)

pred = logisticRegression(faces,500,0.01)
print(pred)