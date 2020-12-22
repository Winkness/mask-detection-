import cv2
import time
import numpy as np
import pygame
import threading

#脸部的识别非必须
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade.load('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_frontalface_default.xml')
'''opencv的haar人脸特征分类器'''

#主要还是通过眼睛位置进行区域判断(眼镜判断)
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
eyes_cascade.load('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
'''opencv的haar眼镜特征分类器'''

smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
smile_cascade.load('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_smile.xml')


def seekface_init():
    image=cv2.imread('background.jpg')

def seekface_seek():

    image=frame

    #image=cv2.GaussianBlur(image,(5,5),0)#高斯滤波
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#将图片转化成灰度
    cv2.imshow("gray",gray)
    image2=image.copy()

    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)#将图片转化成HSV格式
    #cv2.imshow("hsv",hsv)#显示HSV图

    H,S,V=cv2.split(hsv)
    #cv2.imshow("hsv-H",H)#显示HSV图明度

    minH=cv2.getTrackbarPos("minH", 'skin')
    maxH=cv2.getTrackbarPos("maxH", 'skin')
    if minH>maxH:
        maxH=minH

    thresh_h=cv2.inRange(H,minH,maxH)#0-180du 提取人体肤色区域
    #cv2.imshow("skin",thresh_h)#显示肤色图


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 人脸检测

    for (x, y, w, h) in faces:
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 画框标识脸部
        image = cv2.circle(image, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 255), thickness=2)#圆圈标识

        face_area = image[y:y + h, x:x + w]
        eyes = eyes_cascade.detectMultiScale(face_area, 1.3, 19)  # 眼睛检测
        for (x, y, w, h) in eyes:
            cv2.rectangle(face_area, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 画框标识眼部

        smiles=smile_cascade.detectMultiScale(face_area,scaleFactor=1.16,minNeighbors=65,minSize=(25,25),flags=cv2.CASCADE_SCALE_IMAGE)# 笑脸检测
        for(x,y,w,h)in smiles:
            cv2.rectangle(face_area,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.putText(image,'smile',(x,y-7),3,1.2,(0,0,255),2,cv2.LINE_AA)

if __name__ == '__main__':
    seekface_init()
    capture=cv2.VideoCapture(0)
    while True:
        ref,frame=capture.read()
        if ref==False:
            print("打开摄像头错误")
            break
        #等待30ms显示图像，若过程中按“Esc”退出
        c= cv2.waitKey(30) & 0xff
        if c==27:
            capture.release()
            break

        seekface_seek()  # 对视频检测
        cv2.imshow("framelive",frame)#摄像头实时视频



    capture.release()
    cv2.destroyAllWindows()