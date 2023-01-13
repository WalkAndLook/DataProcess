'''
target:去除相似图片
图片的形状size需要一样
这里用的是OpenCV自带的ssim方法
只对于连续图片（例一个视频里截下的图片）准确率也较高，其效率高

方法一：相邻两个文件比较相似度，相似就把第二个加到新列表里，然后进行新列表去重，统一删除。

例如：有文件1-10，首先1和2相比较，若相似，则把2加入到新列表里，再接着2和3相比较，若不相似，则继续进行3和4比较…一直比到最后，然后删除新列表里的图片
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cv2
#from skimage.measure import compare_ssim
from skimage.metrics import _structural_similarity as ssim
import numpy as np

# import shutil
# def yidong(filename1,filename2):
#     shutil.move(filename1,filename2)



def delete(filename1):
    os.remove(filename1)
if __name__ == '__main__':
    path = r'E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\视频\11.4\图片0'
    # save_path_img = r'E:\0115_test\rec_pic'
    # os.makedirs(save_path_img, exist_ok=True)
    img_path = path
    imgs_n = []
    num = []
    img_files = [os.path.join(rootdir, file) for rootdir, _, files in os.walk(path) for file in files if
                 (file.endswith('.jpg'))]
    for currIndex, filename in enumerate(img_files):
        if not os.path.exists(img_files[currIndex]):
            print('not exist', img_files[currIndex])
            break

        # print(img_files[currIndex])

        #img = cv2.imread(img_files[currIndex])
        # 用于读取中文路径
        img = cv2.imdecode(np.fromfile(img_files[currIndex], dtype=np.uint8), flags=cv2.IMREAD_COLOR)
        #img1 = cv2.imread(img_files[currIndex + 1])
        img1 = cv2.imdecode(np.fromfile(img_files[currIndex+1], dtype=np.uint8), flags=cv2.IMREAD_COLOR)


        # 使用OpenCV自带的函数进行图片的比较
        ssim_value = ssim.structural_similarity(img, img1, multichannel=True)
        if ssim_value > 0.8:
            imgs_n.append(img_files[currIndex + 1])
            print('相似图片:',ssim_value,'图1:',img_files[currIndex],'图2', img_files[currIndex + 1])
        else:
            print(ssim_value,'图1:',img_files[currIndex],'图2', img_files[currIndex + 1])
        currIndex += 1
        if currIndex >= len(img_files)-1:
            break

    '''    
    for image in imgs_n:
        # yidong(image, save_path_img)
        delete(image)
    '''

