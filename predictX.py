#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo import YOLO
from PIL import Image
import os
import time

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
        start = time.time()
        r_image = yolo.detect_image(image)
        end = time.time()
        print('detection time: %.4f' %(end - start))
        r_image.save('imgX/3_result.jpg')
        # r_image.show()
