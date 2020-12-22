import cv2
#
import time
#

face_cascade=cv2.CascadeClassifier('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_eye.xml')
#微笑检测
smile_cascade=cv2.CascadeClassifier('E:/opencv/opencv-4.4.0/data/haarcascades/haarcascade_smile.xml')

def seek_init():
    image=cv2.imread('background.jpg')
    #cv2.imshow('skin',image)

def seek_face():
    start = time.time()
    #获取实时画面
    #ret, frame = cap.read()
    faces=face_cascade.detectMultiScale(frame,1.3,5)
    img=frame

    for(x,y,w,h) in faces:
        #脸框检测，蓝色,颜色后可调节线框粗细
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        img=cv2.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 255), thickness=2)
        #框选出人脸区域，在人脸区域进行眼部检测，节省计算资源

        #眼睛检测
        face_area=img[y:y+h,x:x+w]
        #可以通过调节face_area的值改变精度
        eyes=eye_cascade.detectMultiScale(face_area,1.5,19)
        #用人眼级联分类器引擎在人脸部分进行人眼识别，返回的eyes为眼睛坐标列表
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(255,255,0),3)

        #微笑检测
        smiles=smile_cascade.detectMultiScale(face_area,scaleFactor=1.16,minNeighbors=65,minSize=(25,25),flags=cv2.CASCADE_SCALE_IMAGE)
        for(ex,ey,ew,eh)in smiles:
            cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)
            cv2.putText(img,'smile',(x,y-7),3,1.2,(0,0,255),2,cv2.LINE_AA)


#主函数
if __name__ == '__main__':
   # use camera
   cap = cv2.VideoCapture(0)
   while True:
       ret, frame = cap.read()
       seek_init()
       seek_face()
       # 实时展示画面效果
       cv2.imshow('frame2', frame)
       # 每五秒监听一次动作
       if cv2.waitKey(5) & 0xFF == ord('q'):
         break
   #关闭所有窗口
   cap.release()
   cv2.destroyAllWindows()
