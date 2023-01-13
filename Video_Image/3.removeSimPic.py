'''
target:去除相似图片
寒寒给的代码
不需要图片一样的size
会把相似的图片保存起来

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

import shutil
# def yidong(filename1,filename2):
#     shutil.move(filename1,filename2)

'''
下面是用于判断两张图片的相似度情况
# dist可以理解为两张图片的相似度，一般情况下，
# 如果两张图片基本一样，dist<10，
# 如果两张图片很类似，比如光线不同、很小的局部区域有不同、图片中的目标的角度或者位置略有偏移等，dist<45
# 如果两张图片没相似性，看起来就是两张不同的图片，dist>65
'''
# 图像处理
def regene_image(input_frame, frame_name=None):
    gray_frame = cv2.cvtColor(input_frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (3, 3), 0)
    # out_frame = cv2.resize(blur_frame, (0, 0), fx=0.3, fy=0.3)
    #print("原图size：",blur_frame.shape) #先高后宽
    out_frame = cv2.resize(blur_frame, (250, 250))
    #print("修改size：",out_frame.shape)
    if frame_name:
        cv2.imwrite(frame_name, out_frame)
    return out_frame


# 构造detector和matcher
def build_sift_detector():
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    detector = cv2.ORB_create()
    return bf, detector


# 平均值
def get_average(dists):
    return sum(dists) / len(dists)


def compute_dist_score(bf, target_des, compare_des):
    try:
        # matches = flann.knnMatch(target_des, compare_des, k=2)
        matches = bf.match(target_des, compare_des)
        dist = [m.distance for m in matches]
        ret = get_average(dist)
        if ret == 0:
            ret = 0.1
    except cv2.error:
        ret = 100000
    return ret


def get_image_des(image_path):
    #frame = cv2.imread(image_path)
    # 用于读取中文路径
    frame = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), flags=cv2.IMREAD_COLOR)
    target_frame = regene_image(frame)
    (target_kp, target_des) = detector.detectAndCompute(target_frame, None)
    return target_des

bf, detector = build_sift_detector()



def delete(filename1):
    os.remove(filename1)

def movefile(srcfile,dstpath):
    # 移动函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        #fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.move(srcfile, dstpath)          # 移动文件
        #print ("move %s -> %s"%(srcfile, dstpath + fname))


if __name__ == '__main__':
    # 视频图片路径
    path = r'E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\图片11.4\图片17'
    yuzhi =57
    # path = r'C:\Users\xukechao\Desktop\图片11_10'
    # 相似图片移动的文件夹
    move_path = path + '_相似'
    if not os.path.exists(move_path):
        os.mkdir(move_path)
    # save_path_img = r'E:\0115_test\rec_pic'
    # os.makedirs(save_path_img, exist_ok=True)
    img_path = path
    imgs_n = []
    num_dist = []
    img_files = [os.path.join(rootdir, file) for rootdir, _, files in os.walk(path) for file in files if
                 (file.endswith('.jpg'))]
    print("阈值大小为：", yuzhi)

    for currIndex, filename in enumerate(img_files):
        if not os.path.exists(img_files[currIndex]):
            print('not exist', img_files[currIndex])
            break

        # 使用上述函数进行图片的相似度比较
        img =img_files[currIndex]
        img1 =img_files[currIndex+1]
        # 这里get_image_des输入的是图片路径
        image_des = get_image_des(img)
        image_des1 = get_image_des(img1)
        dist = compute_dist_score(bf, image_des, image_des1)
        num_dist.append(dist)
        name =os.path.split(img)[1]
        name1 = os.path.split(img1)[1]

        if dist < yuzhi:
            imgs_n.append(img_files[currIndex])
            print('相似图片:',dist,'图1:',name,'图2', name1)
        else:
            print(dist,'图1:',name,'图2', name1)
        currIndex += 1
        if currIndex >= len(img_files) - 1:
            break

    high_point = np.percentile(num_dist,(25,50,75),method='midpoint')
    print(f"相似度数值的下四分位数为：{high_point[0]},中位数为：{high_point[1]},上四分位数为：{high_point[2]}")
    print("开始移动相似图片")
    print("总的图片个数：",len(img_files))
    print("移动的图片个数：",len(imgs_n))
    print("剩下的图片个数：",len(img_files)-len(imgs_n))
    for image in imgs_n:
        # 移动图片
        movefile(image,move_path)
        # 删除相似图片
        # delete(image)
    print("移动相似图片完成")

