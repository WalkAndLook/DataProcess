'''
target: 只读取某一个视频中的图片
'''

import cv2
import os

num =26
video_path = r'E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\视频\11.4\{0}.mp4'.format(num)
save_path = r'E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\图片11.4\图片{0}_30'.format(num)
cut_frame =30


video = cv2.VideoCapture(video_path)
video_fps = int(video.get(cv2.CAP_PROP_FPS))
print(video_fps)
current_frame = 0

# 每个视频保存图片的文件夹
# mp4_path = os.path.join(save_path, file[:-4])
mp4_path = save_path
if not os.path.isdir(mp4_path):
    os.mkdir(mp4_path)
while (True):
    ret, image = video.read()
    # 视频读取出来的手机图片是倒着的，这里对读取的图片进行重新旋转180度
    img_rotate = cv2.rotate(image, cv2.ROTATE_180)
    # cut_frame = random.randint(5, 35)
    if ret is False:
        video.release()
        break
    if current_frame % cut_frame == 0:
        # cv2.imwrite(save_path + '/' + file[:-4] + str(current_frame) + '.jpg',
        #             image)  # file[:-4]是去掉了".mp4"后缀名，这里我的命名格式是，视频文件名+当前帧数+.jpg，使用imwrite就不能有中文路径和中文文件名
        # 这里把图片的命名为5位数字，方便后面的图片跟着下一张图片进行对比，按照视频读取图片的方式
        cv2.imencode('.jpg', img_rotate)[1].tofile(
            mp4_path + '/' +str(num)+ str("{:0>5d}".format(current_frame)) + '.jpg')  # 使用imencode就可以整个路径中可以包括中文，文件名也可以是中文
        print('正在保存'+str(num) + str("{:0>5d}".format(current_frame)) + '.jpg')

    current_frame = current_frame + 1
