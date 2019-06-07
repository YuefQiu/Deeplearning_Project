from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import torch
from torch.autograd import Variable
import numpy as np
from net import CNN3
import pyttsx3
import win32com.client
import time
from AGUI_child import Ui_childWindow
from AGUI_alarm import Ui_Alarm

#以下为训练后神经网络模型的引进
face_detector=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
cnn=CNN3()
cnn.load_state_dict(torch.load('cnn.pkl'))
speaker=win32com.client.Dispatch("SAPI.SpVoice")



class Ui_childWindow1(Ui_childWindow):
    def __init__(self):
        super(Ui_childWindow1, self).__init__()
        self.setupUi(self)
        #参数定义
        self.Alarm = Ui_Alarm()
        self.open_time = self.close_time = self.total_time = self.time = self.loop_time = 0
        self.statistics = self.couting_instant = 0
        self.freq = 0
        self.state = 0
        self.alarm_mode = 0
        self.engine = pyttsx3.init()#语音包启动引擎
        #槽函数连接
        self.connect_fun()

    def connect_fun(self):
        self.pushButton_1.clicked.connect(self.fun_operate)  # 运行
        self.pushButton_2.clicked.connect(self.fun_pause)  # 暂停
        self.pushButton_3.clicked.connect(self.showMinimized)  # 最小化窗口
        self.pushButton_4.clicked.connect(self.close)# 关闭窗口
        self.radioButton_1.clicked.connect(self.alarm_mode_switch1)
        self.radioButton_2.clicked.connect(self.alarm_mode_switch2)
        self.radioButton_3.clicked.connect(self.alarm_mode_switch3)

        # 实时刷新，不然视频不动态
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(40)

    def alarm_mode_switch1(self):
        self.alarm_mode = 1

    def alarm_mode_switch2(self):
        self.alarm_mode = 2

    def alarm_mode_switch3(self):
        self.alarm_mode = 0

    # 运行的主函数
    def fun_operate(self):
        self.cap = cv2.VideoCapture(0)
        self.initialize()
        self.timer.timeout.connect(self.capPicture)

    #暂停的主函数
    def fun_pause(self):
        self.cap.release()

    #功能初始化函数
    def initialize(self):
        self.open_time = self.close_time = self.total_time = self.time = self.loop_time = time.time()
        self.statistics = 0
        self.freq = 0
        self.state = 0

    #功能拍照函数
    def capPicture(self):
        if (self.cap.isOpened()):
            # 从摄像头获取图像
            ret, img = self.cap.read()
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            # 检测摄像头图像中的人脸，并标记人脸的大小和位置，并在GUI界面中显示人脸
            img, face_list, max_size_index, length = self.face_detect(img, face_detector)
            self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.View.setPixmap(QPixmap.fromImage(self.image).scaled(self.View.width(), self.View.height()))
            # 当人脸数目不是0时
            if length is not 0:
                face_image = face_list[max_size_index]
                # 判断睁闭眼
                pred = self.eye_detector(face_image)
                self.total_time = time.time() - self.time
                #对于眨眼时间，频率等进行统计，并显示在GUI界面上
                if pred == self.state:
                    if self.state == 0:
                        self.open_time = time.time()
                    else:
                        self.listView_3.setText(str('%.3f' %(time.time() - self.open_time)))
                        self.close_time = time.time()
                else:
                    self.state = pred
                    if pred == 0:
                        self.statistics += 1
                        self.couting_instant += 1
                        self.close_time = time.time()
                    else:
                        self.open_time = time.time()
                self.listView_2.setText(str(self.statistics))
                self.freq = self.couting_instant/(time.time()-self.loop_time)
                if time.time()-self.loop_time > 10:
                    self.loop_time = time.time()
                    self.couting_instant = 0
                self.listView_1.setText(str('%.3f' %self.freq))
                #如果开启提醒模式，则会输入获得的数据分析，并给出提示
                if self.alarm_mode is not 0 :
                    alarm_msg=self.alarm()
                    if alarm_msg is not 0:
                        #语音提示
                        if self.alarm_mode==1:
                            self.engine.say(alarm_msg)
                            self.engine.runAndWait()
                        #文字提示
                        if self.alarm_mode==2:
                            self.Alarm.message_label.setText(alarm_msg)
                            self.Alarm.show()

            #当人脸数目大于2个时，进行提醒
            elif length>1:
                self.Alarm.message_label.setText("请保持视频框类仅有一张人脸")
                self.Alarm.show()

    #人脸检测函数
    def face_detect(self, img,face_detector):
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #获取视频中的所有人脸
        faces = face_detector.detectMultiScale(gray, 1.1, 2)
        face_img_list=[]
        sizes=[]
        max_size=max_size_index=0
        for x,y,w,h in faces:
            if w > 70 and h > 70:  # 过滤太小的人脸，如果检测不到，可以调整这个参数
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #框出人脸并统一大小
                face_img = gray[y:y + h, x:x + w]
                face_img = cv2.resize(face_img, (128, 128), interpolation=cv2.INTER_CUBIC)
                face_img_list.append(face_img)
                sizes.append(w*h)

        length=len(face_img_list)
        #找到所有测量的人脸中最大的那一个
        for i in range(length):
            if max_size<sizes[i]:
                max_size=sizes[i]
                max_size_index=i
        return img,face_img_list,max_size_index,length

    #cnn训练网络的引入，检验睁眼闭眼
    def eye_detector(self,img):
        images=np.array([])
        images=np.append(images,img)
        img = images.reshape(-1, 1,128, 128)
        img=torch.from_numpy(img).float()
        data=Variable(img)
        output=cnn(data)

        _ , predicted = torch.max(output[0], 1)
        return predicted.numpy()[0]
    #提醒判断函数，获取提示信息
    def alarm(self):
        message=""
        if self.freq < 0.05 and self.freq>0 :
            message+="眨眼频率过低  "
        elif self.freq > 2:
            message+="眨眼频率过高  "
        if time.time()-self.close_time>5:
            message+="闭眼时间过长  "
        elif time.time()-self.open_time>10:
            message+="睁眼时间过长  "
        if message is not "":
            return message
        else:
            return 0