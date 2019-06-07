
#从OpencvVideo文件夹获取原始数据，更方便地分类，睁开眼睛按  z 键，闭眼睛按 b 键 ，啥也不是 按空格，请注意结束的时候请不要以啥也不是作为最后一张图片
#分好类的图片并未同意大小处理！

import cv2
cascPath = "haarcascade_frontalface_default.xml"   #识别人脸的一个模型
faceCascade = cv2.CascadeClassifier(cascPath)
def FindMax2(path):
    i = 1
    while True:
        test = cv2.imread(path.format(i))
        if test is  None:
            break
        else:
            if not (i%100):
                print('已经寻找了 ',i,'张图片' )
            i += 1
    return i
def FindMax1(path):
    i = FindMax2('F:/OpencvVideo/{}.jpg')+5
    j=0
    while True:
        test = cv2.imread(path.format(i))
        if test is not None:
            break
        else:
            if not (j%100):
                print('已经反向寻找了 ',j,'张图片' )
            i -= 1
            j+=1
    return i

print('开始寻找总库最大......')
iMax=FindMax2('F:/OpencvVideo/{}.jpg')-1
print('最大找到为  ',iMax,'/n开始寻找本次起始点')
iStart=max(FindMax1('F:/ShouldReadyImg/RGB/Close/{}.jpg'),FindMax1('F:/ShouldReadyImg/RGB/Open/{}.jpg'))
print(iMax,'   ',iStart)
if iMax ==iStart:
    print('全部分类完毕！请获取更多原始数据！！')
    while True:
        continue
print("当前起始为",iStart+1)
i=iStart+1
while True:
    frame = cv2.imread('F:/OpencvVideo/{}.jpg'.format(i))
    if frame is None:
        print('分类工作暂时完成，请休息')
        while True:
            continue
    # 转为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 调用分类器进行检测
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80,111 ),
        # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # 画矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    try:
        cut = frame[y:(y + h), x:(x + w)]
        cutOfgray = gray[y:(y + h), x:(x + w)]
        cv2.imshow('Video', cut)
    except:
        i+=1
        print('Waring！    坏图片，转到第',i,'号')
        cv2.destroyAllWindows()
        continue

    while (1):
        if cv2.waitKey() & 0xFF == ord('z'):
            try:
                cv2.imwrite('F:/ShouldReadyImg/RGB/Open/' + str(i) + '.jpg', cut)
                cv2.imwrite('F:/ShouldReadyImg/Gray/open/' + str(i) + '.jpg', cutOfgray)
                print("第{}号照片已经入库".format(i))
            except:
                print('异常存储失败！')
            break
        elif cv2.waitKey() & 0xFF == ord('b'):
            try:
                cv2.imwrite('F:/ShouldReadyImg/RGB/Close/' + str(i) + '.jpg', cut)
                cv2.imwrite('F:/ShouldReadyImg/Gray/Close/' + str(i) + '.jpg', cutOfgray)
                print("第{}号照片已经入库".format(i))
            except:
                print('异常存储失败！')
            break
        elif cv2.waitKey() & 0xFF == ord(' '):
            print("第{}号照片啥也不是，  已经丢弃".format(i))
            break
    i += 1
    # 关闭所有窗口
    cv2.destroyAllWindows()
