import  os
import  cv2
from  PIL import Image
import  numpy as np
def getImageAndLabels(path):
    # 储存人脸数据
    facesSamples=[]
    # 储存姓名数据
    ids=[]
    # 储存图片信息
    imagePaths=[os.path.join(path,f)for f in os.listdir(path)]
    # 加载分类器
    face_detecteror =cv2.CascadeClassifier("C:/Users/mac/AppData/Local/Temp/pip-build-endbkgjx/opencv-python/opencv/data/haarcascades/haarcascade_frontalcatface.xml")
    # 遍历列表中的图片
    for imagePath in imagePaths:
        PIL_img=Image.open(imagePath).convert('L')
        # 将图片以黑白深浅转换为数组
        img_numpy= np.array(PIL_img,'uint8')
        # 获取图片中人脸特征
        faces =face_detecteror.detectMultiScale(img_numpy)
        # 获取图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])
        # 预防无面容图片
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])
        # 打印脸部特征和id
        print('id:',id)
        print('fs:',facesSamples)
        return facesSamples,ids

if __name__ == '__main__':
    #图片路径
    path = 'D:/pic/'
    faces,ids=getImageAndLabels(path)
    # 加载识别器
    recognizer =cv2.face.LBPHFaceRecognizer_create()
    # 训练
    recognizer.train(faces,np.array(ids))
    # 保存文件
    recognizer.write('D:/pic/trainer/trainer.yml')