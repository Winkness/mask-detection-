#1.导入与显示
#导入模块
import cv2 as cv
#读取图片
img=cv.imread("test1.jpg")#路径非中文；
#显示图片
cv.imshow("read_img",img)
#等待键盘输入 单位毫秒 0为无限等待 1000ms=1s
cv.waitKey(0)
cv.waiKey(3000)
#释放内存 由于Opencv底层由C++编写
cv.destroyAllWindows()

