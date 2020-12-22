#2.灰度处理
import cv2 as cv

img=cv.imread('test1.jpg')
cv.imshow('BGR_img',img)

#将图片灰度转换
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_img',gray_img)

#保存图片
cv.imwrite('gray_test1.jpg',gray_img)

cv.waitKey(0)
cv.destroyAllWindows()
