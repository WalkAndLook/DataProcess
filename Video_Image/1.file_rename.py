'''
target:对文件夹下的视频文件.mp4按顺序进行重命名

'''

import os
def myrename(path):
    file_list=os.listdir(path)
    i=0
    for fi in file_list:
        old_name=os.path.join(path,fi)
        #new_name=os.path.join(path,str(i)+fi[-4:])
        new_name = os.path.join(path, str(0) + fi)
        os.rename(old_name,new_name)
        i+=1

if __name__=="__main__":
    #path=r"E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\视频\11.4"
    path = r'E:\南京工作\缺陷素材图片收集\sndmjs 室内地面积水\图片11.4\图片0'
    myrename(path)

