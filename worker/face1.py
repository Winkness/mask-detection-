import cv2 as cv
def face_detect_demo():
    # 将图片灰度处理
    gray=cv.cvtColor(img,cv.COLOR_BGR2BGRA)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # 将图片转化成HSV格式
    cv.imshow("hsv",hsv)#显示HSV图

    # 加载特征数据
    face_detector=cv.CascadeClassifier('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_frontalface_default.xml')
    #检测人脸
    faces=face_detector.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
    cv.imshow('result',img)


#加载图片
img=cv.imread('test one-77.jpg')
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()
