import cv2 as cv
import numpy as np
import os
path='E:/OpencvVideo'
def face_detect_demo(image,i,face_detector):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #根据自己电脑进行调整，在opencv安装目录下搜索文件haarcascade_frontalface_alt.xml，把这个文件的路径放上去
    faces = face_detector.detectMultiScale(gray, 1.1, 2)
    for x, y, w, h in faces:
        if w>70 and h>70:#过滤太小的人脸，如果检测不到，可以调整这个参数
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            face_img = gray[y:y+h, x:x+w]
            im = cv.resize(face_img, (128, 128), interpolation=cv.INTER_CUBIC)
            cv.imwrite('E:/OpencvVideo/qyf2_' + str(i) + '.jpg', im)
            cv.imshow("capture", frame)


if __name__=='__main__':
    capture = cv.VideoCapture(0)
    folder = os.path.exists('E:/OpencvVideo')
    face_detector = cv.CascadeClassifier("F:/Anaconda/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml")
    if not folder:
        os.makedirs(path)
    i=1
    while (True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        face_detect_demo(frame,i,face_detector)
        c = cv.waitKey(50)#拍照间隔
        if c == 27:  # 按ESC退出程序
            break
        i += 1
    capture.release()
    cv.destroyAllWindows()


