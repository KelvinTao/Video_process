# -*- coding: utf-8 -*-
import numpy as np
import cv2,os
###
#path='E:/taoxianming/Rat/data'
##windows
path=r'E:\taoxianming\Rat\data\pin_result'
###labels pin
pinTSV=os.path.join(path,'pin-2020-06-23 A-Me-Mf B-Mg-Mh.tsv')
#labels=open(pinTSV).read().split('Status')[1].strip().split('\t\n')
labels=np.loadtxt(pinTSV,dtype='str',skiprows=16,usecols=(0,8),delimiter='\t')



##get file

file=path+'/video/2020-06-23 M-M, F-F/2020-06-23 A-Me-Mf B-Mg-Mh.mp4'
#file=path+'/video/2020-06-21 M-M, F-F'
##计算机自带的摄像头为0，外部设备为1, file path
video = cv2.VideoCapture(file)#



##get frame at a moment
sec=38.120
msec=sec*1000
video.set(cv2.CAP_PROP_POS_MSEC,msec)
ret, frame = video.read()
img = cv2.resize(frame,(320,240))
#cv2.imwrite(path+'/photo/%d.jpg'%i,img)
cv2.imshow("capture",img)

cv2.destroyAllWindows()

##帧速率
fps = video.get(cv2.CAP_PROP_FPS)##or##video.get(5)
print('fps = ', fps)
##总帧数
total_s = video.get(cv2.CAP_PROP_FRAME_COUNT)

print("total_s = ", total_s)
##获取特定帧
video.set(cv2.CAP_PROP_POS_FRAMES,5000)##NO.

i=1
ret, frame = video.read()
img = cv2.resize(frame,(320,240))
cv2.imwrite(path+'/photo/%d.jpg'%i,img)
#cv2.imshow("capture",img)
frms = video.get(cv2.CAP_PROP_POS_FRAMES)
print(frms)



###read one by one
gap0=34
gap1=33
i=0
#ret, frame = video.read()
#img = cv2.resize(frame,(320,240))
#cv2.imwrite(path+'/photo/%d.jpg'%i,img)
while True:
    print(i)
    # 循环读取帧
    ret, frame = video.read()
    img = cv2.resize(frame,(320,240))
    #cv2.imwrite(path+'/photo/%d.jpg'%i,img)
    cv2.imshow("capture",img)
    if i % 2==0:
        cv2.waitKey(gap0)
    else:
        cv2.waitKey(gap1)
    #cv2.imshow("capture",frame)
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #RGB图像转为单通道的灰度图像
    #gray = cv2.resize(gray,(320,240)) #图像大小为320*240

38.120

##
while ret:
    milliseconds = video.get(cv2.CAP_PROP_POS_MSEC)
    seconds = milliseconds//1000
    milliseconds = milliseconds%1000
    minutes = 0
    hours = 0
    if seconds >= 60:
        minutes = seconds//60
        seconds = seconds % 60
    if minutes >= 60:
        hours = minutes//60
        minutes = minutes % 60
    print(int(hours), int(minutes), int(seconds), int(milliseconds))
    ret, frame = video.read()
    ###
    #i += 1
    
