#3.修改尺寸
import cv2 as cv
img=cv.imread('test1.jpg')
cv.imshow('img',img)
print('原来的形状',img.shape)


#resize_img=cv.resize(img,dsize=(200,240))
resize_img=cv.resize(img,dsize=(400,460))
print('修改后的形状',resize_img.shape)


cv.imshow('resize_img',resize_img)

#cv.waitKey(0)
#只有输入q时候，退出
#code=cv.waitKey(0)
#print(code)

#按其他键无反应，按q有反应
while True:
    if ord('q')==cv.waitKey(0):
        break


cv.destroyAllWindows()