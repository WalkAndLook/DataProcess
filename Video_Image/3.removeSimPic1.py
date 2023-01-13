'''
target:去除相似图片
图片的形状size需要一样
准确率高，但效率低
这里用的是OpenCV自带的方法ssim，同一个文件夹多个文件进行相似度比较
方法二：逐个去比较，若相似，则从原来列表删除，添加到新列表里，若不相似，则继续

例如：有文件1-10，首先1和2相比较，若相似，则把2在原列表删除同时加入到新列表里，再接着1和3相比较，若不相似，则继续进行1和4比较…
一直比,到最后一个，再继续，正常应该再从2开始比较，但2被删除了，所以从3开始，继续之前的操作，最后把新列表里的删除。
'''

'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：579817333 
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''

import os
import cv2
#from skimage.measure import compare_ssim
from skimage.metrics import _structural_similarity as ssim
import numpy as np
import shutil
import datetime
def yidong(filename1,filename2):
    shutil.move(filename1,filename2)
def delete(filename1):
    os.remove(filename1)
    print('real_time:',now_now -now)
if __name__ == '__main__':
    path = r'F:\temp\demo'
    # save_path_img = r'F:\temp\demo_save'
    # os.makedirs(save_path_img, exist_ok=True)
    for (root, dirs, files) in os.walk(path):
        for dirc in dirs:
            if dirc == 'rec_pic':
                pic_path = os.path.join(root, dirc)
                img_path = pic_path
                imgs_n = []
                num = []
                del_list = []
                img_files = [os.path.join(rootdir, file) for rootdir, _, files in os.walk(img_path) for file in files if
                             (file.endswith('.jpg'))]
                for currIndex, filename in enumerate(img_files):
                    if not os.path.exists(img_files[currIndex]):
                        print('not exist', img_files[currIndex])
                        break
                    new_cur = 0
                    for i in range(10000000):
                        currIndex1 =new_cur
                        if currIndex1 >= len(img_files) - currIndex - 1:
                            break
                        else:
                            size = os.path.getsize(img_files[currIndex1 + currIndex + 1])
                            if size < 512:
                                # delete(img_files[currIndex + 1])
                                del_list.append(img_files.pop(currIndex1 + currIndex + 1))
                            else:
                                img = cv2.imread(img_files[currIndex])
                                img = cv2.resize(img, (46, 46), interpolation=cv2.INTER_CUBIC)
                                img1 = cv2.imread(img_files[currIndex1 + currIndex + 1])
                                img1 = cv2.resize(img1, (46, 46), interpolation=cv2.INTER_CUBIC)
                                ssim_value = ssim.structural_similarity(img, img1, multichannel=True)
                                if ssim > 0.9:
                                    # imgs_n.append(img_files[currIndex + 1])
                                    print(img_files[currIndex], img_files[currIndex1 + currIndex + 1], ssim)
                                    del_list.append(img_files.pop(currIndex1 + currIndex + 1))
                                    new_cur = currIndex1
                                else:
                                    new_cur = currIndex1 + 1
                                    print('small_ssim',img_files[currIndex], img_files[currIndex1 + currIndex + 1], ssim)
                for image in del_list:
                    # yidong(image, save_path_img)
                    delete(image)
                    print('delete',image)
