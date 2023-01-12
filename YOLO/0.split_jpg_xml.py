'''
Traget: 将labelimg标注的Annotations(xml)文件与images(jpg)文件分开
Using:
1 输入path路径，该路径下包含jpg文件和xml文件
2 输入输出保存的路径，jpg_path 和 xml_path
Remarks：
1 windows可以直接在文件夹里操作选取xml文件和jpg文件
2 Linux可以使用命令移动文件，cp /home/data/831/*.xml /project/train/src_repo/dataset/Annotations
'''

import os
import shutil
path = r'yibiao'  #包含原图和标签xml的文件夹
jpg_path = r'images'  #只存放images的文件夹
xml_path = r'Annatotions'  #只存放xml文件

if not os.path.exists(jpg_path):
    os.mkdir(jpg_path)

if not os.path.exists(xml_path):
    os.mkdir(xml_path)


#将文件中的图片和标签数据分开保存在images和Annatotions中
#ctrl+/快速多行加注释和取消注释
for root,dirs,files in os.walk(path):
    for i in range(len(files)):
        if(files[i][-3:] == 'jpg'):
            file_path = root + '/' + files[i]
            new_file_path = jpg_path + '/' + files[i]
            shutil.move(file_path,new_file_path)
        if(files[i][-3:] == 'xml'):
            file_path = root + '/' + files[i]
            new_file_path = xml_path + '/' + files[i]
            shutil.move(file_path, new_file_path)

