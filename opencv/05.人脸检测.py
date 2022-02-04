#导入cv模块
import cv2 as cv
def face_detect_demo():
    gray =cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    face_detect = cv.CascadeClassifier("C:/Users/mac/AppData/Local/Temp/pip-build-endbkgjx/opencv-python/opencv/data/haarcascades/haarcascade_frontalface_alt.xml")
    face =face_detect.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=1)
    cv.imshow("result",img)
#读取图像
img =cv.imread("face1.jpg")
# 检测函数
face_detect_demo()
# 等待
while True:
    if ord(" ") == cv.waitKey():
        break
#释放内存
cv.destroyAllWindows()