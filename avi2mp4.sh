
aviPath=/DATA/taoxm/video_web/hmdb/avi
mp4Path=/DATA/taoxm/video_web/hmdb/mp4
for i in `ls $aviPath`
do
   echo ${i/.avi/.mp4}
   ffmpeg -i $aviPath/$i  -c copy -map 0  $mp4Path/${i/.avi/.mp4} 
done

