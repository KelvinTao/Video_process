# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "/Users/taoxianming/Documents/research/Rat/data/video"

# set path for coco json to be saved
save_json_path = "/Users/taoxianming/Documents/research/Rat/data/video/coco/test_coco.json"

# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)