#训练数据
import cv2
import os
import sys
from PIL import Image
import numpy as np
def getImageAndLabels(path):
    facesSamples=[]
    ids=[]
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]

    #检测人脸
    face_detector=cv2.CascadeClassifier('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_frontalface_default.xml')


    #遍历列表中的图片
    for imagePath in imagePaths:
        #打开图片
        PIL_img=Image.open(imagePath).convert('L')
        #将图像转化成数组
        img_numpy=np.array(PIL_img,'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        #获取每张图片ID
        id=int(os.path.split(imagePath)[1].split('.')[0])

        for x,y,w,h in faces:
            facesSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    print(imagePaths)
    return facesSamples,ids


if __name__ == '__main__':
    #图片路径path
    path='./route/practice/'
    #获取图像数组和ID标签数组
    faces,ids=getImageAndLabels(path)
    #获取循环对象
    recongnizer=cv2.face.LBPHFaceRecognizer_create()
    recongnizer.train(faces,np.array(ids))
    #保存到文件
    recongnizer.write('trainer/trainer.yml')


