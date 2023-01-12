'''
接着5.img_to_8U.py
对得到的所有jpg，png图片进行划分训练集合验证集
将其存储在对应的train,val文件夹下
Using:
    val_num = int(len(lt_png) * 0.1) 在这里修改比例
    path :这里输入保存jpg和png的mask路径
    out_path :这里输入之后用来训练的分好训练集验证集的文件路径

'''


import os
import random
import cv2


#用来删除没有对应mask的图片
#利用集合的差集来得出没有mask的jpg文件名，然后删除
# path = r'E:\Work\video\BJSJ_video\pictures\0002_normal'
# out_path = r'E:\Work\video\BJSJ_video\pictures\0002_mask'

path = r'./dataset/meter_crop/yibiao_mask'
out_path = r'./dataset/meter_crop/yibiao_train_val'

st_jpg =set()
st_png =set()
for dir in os.listdir(path):
    if '.jpg' in dir:
        st_jpg.add(dir[:-4])
    if '.png' in dir:
        st_png.add(dir[:-4])

#也有可能是mask多了，但没有图片
# name = st_png - st_jpg
name = st_jpg - st_png  #计算差集
while len(name) > 0:
    try:
        for i in name:
            os.remove(os.path.join(path, i+'.jpg'))
        break
    except:
        pass

#分配训练集和验证集
lt_png =list(st_png)
val_num = int(len(lt_png) * 0.9)

valid = random.sample(lt_png, val_num)
train = set(lt_png) - set(valid)

#写入train文件
if not os.path.isdir(out_path):
    os.mkdir(out_path)
train_path =os.path.join(out_path,'train')
if not os.path.isdir(train_path):
    os.mkdir(train_path)
val_path =os.path.join(out_path,'val')
if not os.path.isdir(val_path):
    os.mkdir(val_path)

for i in train:
    img_train1 = cv2.imread(os.path.join(path,i+'.jpg'))
    print(os.path.join(path,i+'.jpg'))
    img_train2 = cv2.imread(os.path.join(path,i+'.png'))
    cv2.imwrite(os.path.join(train_path,i+'.jpg'),img_train1)
    print(os.path.join(train_path,i+'.jpg'))
    cv2.imwrite(os.path.join(train_path,i+'.png'),img_train2)

for i in valid:
    img_val1 =cv2.imread(os.path.join(path,i+'.jpg'))
    img_val2 = cv2.imread(os.path.join(path, i + '.png'))
    cv2.imwrite(os.path.join(val_path,i+'.jpg'),img_val1)
    cv2.imwrite(os.path.join(val_path,i+'.png'),img_val2)


