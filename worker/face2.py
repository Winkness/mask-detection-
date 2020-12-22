#检测多张人脸
import cv2 as cv
def face_detect_demo():
    #将图片灰度
    gray=cv.cvtColor(img,cv.COLOR_BGR2BGRA)
    #加载特征数据
    face_detector=cv.CascadeClassifier('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_frontalface_default.xml')

    #检测人脸 可修改scaleFactor,minNeighbors调节识别不精准的问题 也可用maxSize,minSize调整识别范围大小
    faces=face_detector.detectMultiScale(gray,scaleFactor=1.02,minNeighbors=1)
    for x,y,w,h in faces:
        print(x,y,w,h)
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
        cv.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 255), thickness=2)
    cv.imshow('result',img)

img=cv.imread('test one-77.jpg')
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()
