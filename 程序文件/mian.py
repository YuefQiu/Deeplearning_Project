from torch.autograd import Variable
import torch
import torch.nn as nn
from tensorboardX import SummaryWriter
import torch.utils.data as Data
from datanew  import MyDataset  #导入自己的原始数据整合方法
import cv2 as cv
import numpy as np

#训练相关参数初始化
EPOCH = 20           # train the training data n times, to save time, we just train 1 epoch
BATCH_SIZE = 20
LR = 0.00006              # learning rate


def GYH(In):
    temp = In.cpu().detach().numpy()
    preOut = np.zeros(temp.shape, dtype=np.float32)

    cv.normalize(temp, preOut, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)

    Out = torch.from_numpy(preOut).unsqueeze(1)
    return Out

class CNN(nn.Module):
    def __init__(self):
        self.test=0

        super(CNN, self).__init__()

        self.conv1 = nn.Sequential(         # input shape (1, 28, 28)
            nn.Conv2d(
                in_channels=1,              # input height
                out_channels=16,            # n_filters
                kernel_size=5,              # filter size
                stride=1,                   # filter movement/step
                padding=2,                  # if want same width and length of this image after Conv2d, padding=(kernel_size-1)/2 if stride=1
            ),                              # output shape (16, 28, 28)
            nn.ReLU(),                      # activation
            #nn.MaxPool2d(kernel_size=2),    # choose max value in 2x2 area, output shape (16, 14, 14)
        )
        self.conv2 = nn.Sequential(         # input shape (16, 14, 14)
            nn.Conv2d(16, 32, 5, 1, 2),     # output shape (32, 14, 14)
            nn.ReLU(),                      # activation
            nn.MaxPool2d(2),                # output shape (32, 7, 7)
        )

        self.conv3=nn.Sequential(
            nn.Conv2d(32,64,5,1,2),
            nn.MaxPool2d(2),
            nn.ReLU(),
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(64, 128, 5, 1, 2),
            nn.ReLU(),
        )

        self.out = nn.Linear(128 * 32 * 32, 2)   # fully connected layer, output 10 classes
    def forward(self, x):
        self.x1 = x


        if self.test:
            TezhengTuWriter=SummaryWriter('./runs/Pict')
            TezhengTuWriter.add_image('countdown_1',self.x1[0],global_step=0,dataformats='CHW')

        x = self.conv1(x)
        self.x2=x


        if self.test:
            TezhengTuWriter.add_images('countdown_2',GYH(self.x2[0]),global_step=1,dataformats='NCHW')

        x = self.conv2(x)
        self.x3=x

        if self.test:
            TezhengTuWriter.add_images('countdown_3',GYH(self.x3[0]),global_step=2,dataformats='NCHW')

        x=self.conv3(x)
        self.x4=x

        if self.test:
            TezhengTuWriter.add_images('countdown_4', GYH(self.x4[0]), global_step=3,dataformats='NCHW')

        x = self.conv4(x)
        self.x5=x

        if self.test:
            TezhengTuWriter.add_images('countdown_5',GYH(self.x5[0]), global_step=4, dataformats='NCHW')
            TezhengTuWriter.close()
            self.test=0

        x = x.view(x.size(0), -1)           # flatten the output of conv2 to (batch_size, 32 * 7 * 7)

        output = self.out(x)
        return output, x    # return x for visualization

    def Go(self):#用于显示特征图
        self.test=1

#判断函数 可选是否输出特征图（command）
def Judge(cnn2,testloader,Select):
    #cnn2 = torch.load('2.pkl')

    cnn2.cpu()
    correct = 0
    total = 0
    for data in testloader:
        images, labels = data
        outputs = cnn2(Variable(images))
        _, predicted = torch.max(outputs[0], 1)  # outputs.data是一个4x10张量，将每一行的最大的那一列的值和序号各自组成一个一维张量返回，第一个是值的张量，第二个是序号的张量。

        total += labels.size(0)
        correct += (predicted == labels).sum()  # 两个一维张量逐行对比，相同的行记为1，不同的行记为0，再利用sum(),求总和，得到相同的个数。
    print('                          Judge                Accuracy of the network on the Some test images: %d %%' % (100 * correct / total))
    TepmCnn=cnn2
    Select.append( [100 * correct / total,TepmCnn])
    return 100 * correct / total


def Start():
    #定义自己的训练数据
    print('开始加载训练数据  ...')
    train_data = MyDataset(root='F:/训练场/3/' ,datatxt= '3.txt')
    print('             训练数据加载完成')
    print('开始加载测试数据  ...')
    test_data = MyDataset(root='C:/Users/admin/Desktop/data/trainset/' ,datatxt= 'train.txt')
    print('             测试数据加载完成，开始训练')
    #train_data=test_data


    #批量加载训练数据和测试数据

    train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
    testloader = Data.DataLoader(dataset=test_data, batch_size=BATCH_SIZE, shuffle=True)
    AimLine = SummaryWriter('./runs/Line')

    #备选网络
    Select=[]



    cnn = CNN()
    cnn.cuda()

    optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)   # optimize all cnn parameters
    loss_func = nn.CrossEntropyLoss()                      # the target label is not one-hotted

    # training and testing
    print('   ￥&$  本次训练相关参数：EPOCH ：',EPOCH,'BATCH_SIZE  :',BATCH_SIZE,'     LR  :',LR)

    lossWriter = SummaryWriter('./runs/lossEs')
    for epoch in range(EPOCH):

        for step, (b_x, b_y) in enumerate(train_loader):   # gives batch data, normalize x when iterate train_loader

            #可选是否使用CUDA训练模型
            #b_x=Variable(b_x)
            #b_y=Variable(b_y)
            b_y=b_y.cuda()
            b_x = b_x.cuda()

            output = cnn(b_x) # cnn output
            output=output[0]
            loss = loss_func(output, b_y)   # cross entropy loss
            LOSDATA=loss.data.cpu().numpy()

            optimizer.zero_grad()           # clear gradients for this training step
            loss.backward()                 # backpropagation, compute gradients
            optimizer.step()                # apply gradients

            lossWriter.add_scalar('LOSS_for_EPOCH {} '.format(epoch), LOSDATA, global_step=step)   #添加每个epoch的loss值
            #lossWriter.add_scalar('LOSS_for_EPOCH All ', LOSDATA, global_step=step)  # 添加每个epoch的loss值

            if step % 100 == 0:

                print('当前  EPOCH  ',epoch+1,' 已经完成第',step,'次批处理,(每次{}张图片)，loss 为'.format(BATCH_SIZE),loss.data.cpu().numpy())


        Acu=Judge(cnn,testloader,Select)
        AimLine.add_scalar('准确率',Acu,global_step=epoch)
        cnn.cuda()
    AimLine.close()
    lossWriter.close()

#模型保存模块 可选以CPU或者CUDA形式保存 ，可选保存全模型或者只保存参数

    cnn.cpu()
    #torch.save(cnn,'lin6.pkl')
    #torch.save(cnn.state_dict(), 'params_1.pkl')


    print('Pic is loading ..')
    Select.sort()
    Select.reverse()
    MaxCnn=Select[0][1]
    MaxCnn.Go()#激活网络存图模块

    print("确认最大准确率为：")
    Judge(MaxCnn,testloader,Select)


    #生成网络图
    dummy_input = torch.rand(1, 1, 128,128)
    with SummaryWriter('./runs/Graph',comment='Net1')as w:
        w.add_graph(cnn, (dummy_input,))
    w.close()


if __name__ == '__main__':
    Start()
