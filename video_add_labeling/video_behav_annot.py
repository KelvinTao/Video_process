import os
import pandas as pd
import numpy as np
import tempfile as tmpf
import datetime

# %% 读取excel原始时间、生成字幕文件
sheet = pd.read_excel(r'Z:\Code\auROC\wpx_code\traces_plot_with_events\Esr29m\Esr290222(trace奇怪，优先check_video)\esr2-90222_mate_analysis.xls') # pd默认只读取第一张表
video_path = r'J:\Esr2_9\20210222\2021-02-22-15-30-55output.mp4'
(video_folder,video_name) = os.path.split(video_path)
os.chdir(video_folder)
fmpg_path = r'D:\L_ffmpeg\ffmpeg\bin'
# # %% 减去标注用视频和行为学视频的时间差
# ref_path1 = r'G:\\St18-1\\20210108\\2021-01-08-16-06-56.mp4'  # 标注用录频
# ref_path2 = r'G:\St18-1\20210108\SIBK20210108\cam01\20210108\Event20210108160631001.avi'  # ! cam1中的第一段行为学视频
# ref_time1 = os.path.getctime(ref_path1)
# ref_time2 = os.path.getctime(ref_path2)
# time_diff = round(ref_time2-ref_time1, 3)

sheet_col1 = sheet[list(sheet.keys())[0]]
time_idx = int(sheet_col1[sheet_col1.values=='Time'].index.values)
sheet.columns = sheet.iloc[time_idx]
sheet = sheet.drop(sheet.index[:time_idx+1])
sheet.index = range(sheet.shape[0])
# sheet['Time'] = sheet['Time'].astype(float) - time_diff
# %% create the dict containing time
behavs = sheet['Behavior'].unique()
light_idx = np.argwhere(behavs=='light')
np.delete(behavs,light_idx)
bhv_dict = {}
for i in range(behavs.shape[0]):
    bhv_dict[behavs[i]]={'Start':[],'End':[]}
scrip_idx = 1
with tmpf.NamedTemporaryFile(mode='w+t',suffix='.srt',dir=video_folder,delete=False) as subscript:
    tmp_name = subscript.name
    for i in range(sheet.shape[0]):
        col = sheet.iloc[i]
        if col['Status']=='STOP':
            continue
        elif col['Behavior']=='light':
            continue
        else:
            behav = col['Behavior']
            start_time = float(col['Time'])
            start_t = str(datetime.timedelta(seconds=start_time))[:-7]+','+str(datetime.timedelta(seconds=start_time))[-6:-3]
            bhv_dict[behav]['start'] = float(col['Time'])
            for j in range(i+1, sheet.shape[0]):
                if sheet.iloc[j]['Behavior']==col['Behavior']:
                    end_time = float(sheet.iloc[j]['Time'])
                    end_t = str(datetime.timedelta(seconds=end_time))[:-7]+','+str(datetime.timedelta(seconds=end_time))[-6:-3]
                    bhv_dict[behav]['end'] = end_time
                    subscript.write(str(scrip_idx)+'\n')
                    subscript.write('{} --> {}\n'.format(start_t,end_t))
                    subscript.write('\\n'+'{\\an1}'+behav+'\n\n')  # an1：字幕放在左下角
                    scrip_idx +=1
                    break
    # 如果不需要转码则用这一条:
    (_,str_name) = os.path.split(tmp_name)
    # %%在命令行中运行ffmpeg，转字幕并转编码
    os.system('{} -i {} -an -vcodec mpeg4 -g 10 -bf 0 -q:v 5 -pix_fmt yuv420p -vf crop=1120:676:0:48 {}output.mp4'.format(fmpg_path,video_name, video_name[:-4])) # 720:416:0:30
    os.system(r'{} -i {} -lavfi subtitles="{}" -vcodec mpeg4 "mate_sub{}"'.format(fmpg_path,video_name,str_name,video_name))
    # os.system('{} -i {}output.mp4 -lavfi scale=-2:240 subtitles="{}" {}mate_subt{}'.format(fmpg_path,video_name,str_name,video_folder,video_name))