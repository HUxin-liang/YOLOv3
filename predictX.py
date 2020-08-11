#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo import YOLO
from PIL import Image
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '2'
yolo = YOLO()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = yolo.detect_image(image)
        r_image.save('imgX/3_result.jpg')
        # r_image.show()
