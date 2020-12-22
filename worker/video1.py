#检测视频人脸（识别由图片构成，只需识别每一帧的人脸，便可达到目的）
import cv2 as cv
def face_detect_demo(img):

    gray=cv.cvtColor(img,cv.COLOR_BGR2BGRA)

    face_detector = cv.CascadeClassifier('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_frontalface_default.xml')


    faces = face_detector.detectMultiScale(gray)

    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 255), thickness=2)
    cv.imshow('result',img)

cap=cv.VideoCapture('test video-3.mp4')
while True:
    flag,frame=cap.read()
    print('flag',flag,'frame.shape:',frame.shape)
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q')==cv.waitKey(10):
        break
cv.destroyAllWindows()
cap.release()