
# coding: UTF-8
import os,glob
import numpy as np
from itertools import islice
import datetime

##id_to_class
##5 classes
classes=['other','nonsocial','motion','sniff','play']

##18 classes
#classes=['touch','not move','one move','two move','leave',
#'approach','follow','crawl around','stride across','sniff tail','sniff body',
#'sniff nose','sniff genital','stand interaction','press on','allorooming','pinning','fighting']

##generate subtitle file
##video path
vPath='/home/liying_lab/taoxianming/DATA/rat/data/video3camera/chenxf'
videoPath=os.path.join(vPath,'photometry_rat_social_batch2_640x360')
subTitlePath=os.path.join(vPath,'photometry_rat_social_batch2_640x360_subtitle/5classes')
#subTitlePath=os.path.join(vPath,'photometry_rat_social_batch2_640x360_subtitle/18classes')
if not os.path.exists(subTitlePath):
    os.mkdir(subTitlePath)
    #os.makedirs(subTitlePath)


##predicted labeling path
lPath='/home/liying_lab/taoxianming/DATA/rat/result/video3camera/chenxf/multiClass/frame15_lc_zscore'
#03-30-1605-160-fof-5-classes-epoch100_5-classes  03-31-1512-160-fof-18-classes-epoch100_18-classes
labelPath=os.path.join(lPath,'03-30-1605-160-fof-5-classes-epoch100_5-classes')
#labelPath=os.path.join(lPath,'03-31-1512-160-fof-18-classes-epoch100_18-classes')

###
def strtime(start_time):
    seconds=int(start_time)
    millisec=int(round((start_time-seconds)*1000))
    minutes = 0
    hours = 0
    if seconds >= 60:
        minutes = seconds//60
        seconds = seconds % 60
    if minutes >= 60:
        hours = minutes//60
        minutes = minutes % 60
    return("%s:%s:%s,%s"%(hours,minutes,seconds,millisec))


##write srt file
labelFiles=glob.glob(os.path.join(labelPath,'*.csv'))
for lf in labelFiles:
    labelName=os.path.split(lf)[1]
    videoFile=os.path.join(videoPath,labelName.split('.mp4')[0]+'.mp4')
    subVideo=os.path.join(subTitlePath,labelName.split('.mp4')[0]+'.sub.mp4')
    subFile=subVideo.replace('mp4','srt')
    #print(lf)
    #print(videoFile)
    #print(subFile)
    ###
    lid=open(lf)
    sid=open(subFile,'w')
    sub_index=1
    for line in islice(lid, 1, None):
        time_behav=line.strip().split(',')[1:4]##
        start_time=float(time_behav[0])
        behav=classes[int(time_behav[1])]
        prob=float(time_behav[2])
        #print(line)
        #＃produce time range
        end_time=start_time+0.5-0.001 ##0.5s gap
        start_t=strtime(start_time)
        end_t=strtime(end_time)
        #print(start_t)
        #print(end_t)
        #sub_lines=("%s\n%s --> %s\n\\n{\\an1}%s, probability:%s\n\n"%(sub_index,start_t,end_t,behav,prob))
        sub_lines=("%s\n%s --> %s\n{\\an7}%s,  probability:%s\n\n"%(sub_index,start_t,end_t,behav,prob))
        #subscript.write('\\n'+'{\\an1}'+behav+'\n\n')
        sub_index=sub_index+1
        sid.write(sub_lines)
    sid.close()
    ##chaneg subtitle format
    ###os.system('ffmpeg -i "%s" "%s"'%(subFile,subFile.replace('srt','ass')))
    ###os.system('ffmpeg -i "%s" "%s"'%(subFile.replace('srt','ass'),subFile))
    os.system('ffmpeg -i "%s" -i "%s" -c:s mov_text -c:v copy -c:a copy "%s"'%(videoFile,subFile,subVideo))

