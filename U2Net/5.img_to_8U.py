import os
import cv2
import numpy as np
path = r'./dataset/meter_crop/yibiao_mask'
label = []
for file in os.listdir(path):
    if ".png" in file:
        img_path = os.path.join(path,file)
        print(img_path)
        img = cv2.imread(img_path, 0)
        print(np.unique(img))
        arr = np.uint8(img)
        # img[img >1] =1
        # img[img == 38] = 1
        # img[img == 76] =1
        # img[img == 75] =2
        # cv2.imwrite(img_path, img)
