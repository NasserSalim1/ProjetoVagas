import cv2
import pickle
import numpy as np

vagas = []

with open('vagas.pkl', 'rb') as arquivo:
    vagas = pickle.load(arquivo)

video = cv2.VideoCapture('Video.mp4')

while True:
    check,img = video.read()
    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16) # Usa-se o THRESHHOLD INVERSO para que os itens com mais claridade sejam transformados em preto (por conta do vídeo ter sombras)
    imgMedian = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3,3), np.int8)
    imgDil = cv2.dilate(imgMedian, kernel)

    for x,y,w,h in vagas:
        vaga = imgDil[y:y+h, x:x+w]
        count = cv2.countNonZero(vaga)
        cv2.putText(img, str(count), (x, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
        cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('video', img)
    cv2.imshow('video Median', imgDil)
    cv2.waitKey(10)