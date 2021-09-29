# -*- coding: utf-8 -*-
import numpy as np
import os

##
def mkdir(mkPath):
    if not os.path.exists(mkPath):
        os.makedirs(mkPath)

def cut_video(video,group,sec,savePath):
    ##pin: pin time point; group, A or B.
    ##video fragment: 60 frames
    ##2 min 120.01
    duration=2.01
    if group=='A':
        os.system('ffmpeg -ss %f -i %s -t %f -vf crop=iw/2:ih:0:0 -s 320x360 %s'%(sec-1,
            video,duration,savePath))
    if group=='B':
        os.system('ffmpeg -ss %f -i %s -t %f -vf crop=iw/2:ih:iw/2:0 -s 320x360 %s'%(sec-1,
            video,duration,savePath))

##windows
#path='/Users/taoxianming/Documents/research/Rat/data'
path=r'E:\taoxianming\rat\data\cnn_classify\raw_img'
##use pin and nonpin checked by human
classes=['pin','nonpin']
##
video_path=r'E:\taoxianming\rat\video'
video_save=r'E:\taoxianming\rat\data\cnn_classify\video_data'
##
for pi in range(len(classes)):
    print(pi)
    for f in os.listdir(os.path.join(path,classes[pi])):
        print(f)
        if f.find('left')>0:
            daycomb,partime=f.split('_A-left')
            group='A'
        if f.find('right')>0:
            daycomb,partime=f.split('_B-right')
            group='B'
        folder=' '.join([daycomb.split('_')[0],'M-M,','F-F'])
        fileName=daycomb.replace('_',' ')+'.mp4'
        video='"'+os.path.join(video_path,folder,fileName)+'"'
        ##save
        _,_,sec=partime.split('-')
        sec=float(sec.replace('s.jpg',''))
        savePath=os.path.join(video_save,classes[pi],f.replace('.jpg','.mp4'))
        cut_video(video,group,sec,savePath)
        #break



##
import os
video_save=r'E:\taoxianming\rat\data\cnn_classify\video_data'
classes=['pin','nonpin']
fid=open(os.path.join(video_save,'class_list.txt'),'w')
##
for pi in range(len(classes)):
    for f in os.listdir(os.path.join(video_save,classes[pi])):
        fid.write(f+' '+classes[pi]+'\n')
        break
    
fid.close()

##
duration=120.01
if group=='A':
    os.system('ffmpeg -ss %f -i %s -t %f -vf crop=iw/2:ih:0:0 -s 320x360 %s'%(sec-1,
        video,duration,savePath))


