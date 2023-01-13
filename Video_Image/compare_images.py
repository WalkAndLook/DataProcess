import numpy as np
import math
import cv2
import os
import hashlib
import glob
import time
import numpy as np
import subprocess

DIST_SCORE = 40


# 图像处理
def regene_image(input_frame, frame_name=None):
    gray_frame = cv2.cvtColor(input_frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (3, 3), 0)
    # out_frame = cv2.resize(blur_frame, (0, 0), fx=0.3, fy=0.3)
    out_frame = cv2.resize(blur_frame, (250, 250))
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
    frame = cv2.imread(image_path)
    target_frame = regene_image(frame)
    (target_kp, target_des) = detector.detectAndCompute(target_frame, None)
    return target_des

'''
des_is_none_path = "des_is_none"
if not os.path.exists(des_is_none_path):
    os.makedirs(des_is_none_path)
'''


bf, detector = build_sift_detector()


# Demo
img1 = "11/00000.jpg"
img2 = "11/00010.jpg"

image_des1 = get_image_des(img1)
image_des2 = get_image_des(img2)
dist = compute_dist_score(bf, image_des1, image_des2)
print(dist)

# dist可以理解为两张图片的相似度，一般情况下，
# 如果两张图片基本一样，dist<10，
# 如果两张图片很类似，比如光线不同、很小的局部区域有不同、图片中的目标的角度或者位置略有偏移等，dist<45
# 如果两张图片没相似性，看起来就是两张不同的图片，dist>65




