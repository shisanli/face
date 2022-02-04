#导入cv模块
import cv2 as cv
#读取图片
img = cv.imread("face1.jpg")
# 坐标
x,y,w,h = 100,100,100,100
# 绘制矩形 图片，起始点坐标，颜色 默认 bgr，矩形宽度
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=1)
# 绘制圆形
cv.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=2)
cv.imshow("pic",img)
while True:
    if ord(" ") == cv.waitKey():
        break
#释放内存
cv.destroyAllWindows()