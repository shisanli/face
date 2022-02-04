#导入cv模块
import cv2 as cv
#读取图片
img = cv.imread("face1.jpg")
# 修改尺寸
resize_img =cv.resize(img,dsize=(400,600))
# 显示图片
cv.imshow("before",img)
# 显示修改后的图片
cv.imshow("aftrer",resize_img)
# 打印原图
print("before",img.shape)
# 打印修改后的大小
print("after",resize_img.shape)
# 键盘按下空格 退出
while True:
    if ord(" ") == cv.waitKey():
        break
#释放内存
cv.destroyAllWindows()