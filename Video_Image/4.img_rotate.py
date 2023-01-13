'''
target：进行旋转图像
对单个文件夹下的所有图片进行旋转
'''

import cv2
import os
import numpy as np
path = r'E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\图片11.4\图片22_15'

img_files = [os.path.join(rootdir, file) for rootdir, _, files in os.walk(path) for file in files if
                 (file.endswith('.jpg'))]
print("正在进行图片旋转。。")
for file in img_files:
    frame = cv2.imdecode(np.fromfile(file, dtype=np.uint8), flags=cv2.IMREAD_COLOR)
    img_rotate = cv2.rotate(frame, cv2.ROTATE_180)
    # 对同一名称文件进行写入图像操作，会自动覆盖原来的图片
    cv2.imencode('.jpg', img_rotate)[1].tofile(file)
print("图片旋转完成。。")


