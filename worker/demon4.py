#4.画图
import cv2 as cv
img=cv.imread('test1.jpg')
#画矩形
#左上角（x，y），矩形宽高（w，h）
x,y,w,h=100,100,100,100

#绘制正方形
#cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,255),thickness=3)
#显示图片
#绘制圆center元组指原点的坐标  radius：半径   （0,0,255）红色
cv.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,255),thickness=2)
#显示图片
cv.imshow('rectangle_img',img)
cv.waitKey(0)
cv.destroyAllWindows()