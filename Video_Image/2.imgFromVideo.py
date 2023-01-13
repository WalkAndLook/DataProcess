'''
读取文件夹中多个视频的图片
每个视频对应一个单独图片文件夹
'''

import os
import cv2
import random


cut_frame = 10  # 多少帧截一次，自己设置就行，1帧表示1/12秒
video_path = r'E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\视频\11.4'
save_path = r'E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\图片11.4'

if not os.path.exists(save_path):
    os.mkdir(save_path)

for root, dirs, files in os.walk(video_path):  # 这里就填文件夹目录就可以了
    for file in files:
        # 获取文件路径
        if ('.mp4' in file):
            path = os.path.join(root, file)

            video = cv2.VideoCapture(path)
            video_fps = int(video.get(cv2.CAP_PROP_FPS))
            print(video_fps)
            current_frame = 0

            #每个视频保存图片的文件夹
            mp4_path = os.path.join(save_path,'图片' + file[:-4])  #每个视频单独保存一个文件夹
            #mp4_path =save_path  #所有视频单独保存一个文件夹
            if not os.path.isdir(mp4_path):
                os.mkdir(mp4_path)
            while (True):
                ret, image = video.read()
                # 视频读取出来的手机图片是倒着的，这里对读取的图片进行重新旋转180度
                img_rotate = cv2.rotate(image, cv2.ROTATE_180)
                #cut_frame = random.randint(5, 35)
                if ret is False:
                    video.release()
                    break
                if current_frame % cut_frame == 0:
                    # cv2.imwrite(save_path + '/' + file[:-4] + str(current_frame) + '.jpg',
                    #             image)  # file[:-4]是去掉了".mp4"后缀名，这里我的命名格式是，视频文件名+当前帧数+.jpg，使用imwrite就不能有中文路径和中文文件名
                    cv2.imencode('.jpg', img_rotate)[1].tofile(
                        mp4_path + '/' +str("{:0>2d}".format(file[:-4])) + str(
                            "{:0>5d}".format(current_frame)) + '.jpg')  # 使用imencode就可以整个路径中可以包括中文，文件名也可以是中文
                    print('正在保存' +str(file[:-4]) + str("{:0>5d}".format(current_frame)) + '.jpg')

                current_frame = current_frame + 1


