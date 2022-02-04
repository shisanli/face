#导入cv模块
import cv2 as cv
#读取图片
img = cv.imread("face1.jpg")
#灰度转换
gray_img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
#显示灰度图片
cv.imshow("face4.jpg",gray_img)
cv.imwrite("face4.jpg",gray_img)
# 显示图片
cv.imshow("read_img",img)
# 等待
cv.waitKey(0)
#释放内存
cv.destroyAllWindows()