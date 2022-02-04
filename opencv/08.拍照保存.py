import  cv2 as cv
cap =cv.VideoCapture(0)
num= 1
flag =1
while(cap.isOpened()):
    ret_flag,Vshow = cap.read()#每一帧的图像
    cv.imshow("cap",Vshow)
    k= cv.waitKey(1)
    if k == ord('s'):
        cv.imwrite("D:/pic/"+str(num)+".jpg",Vshow)
        print("success to save"+str(num)+".jpg")
        print("=======")
        num+=1
    elif  k==ord(' '):
        break
cap.release()
cv.destroyAllWindows()