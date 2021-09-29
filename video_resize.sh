
path=/home/liying_lab/taoxianming/DATA/rat/data/video3camera/chenxf
mp4Path=$path/photometry_rat_social_batch2
smallPath=$path/photometry_rat_social_batch2_640x360
IFS=$(echo -en "\n\r")
for i in `ls $mp4Path`
do
   echo "$i"
   ffmpeg -i $mp4Path/"$i" -s 640x360 $smallPath/${i/.mp4/.640x360.mp4}
done





##ffmpeg  -ss 00:00:50 -i 2021-01-15\ 11-00-26.mp4 -t 1260 -vf crop=iw/3:ih/2:0:0 2021-01-15_11-00-26_tl1260.mp4
