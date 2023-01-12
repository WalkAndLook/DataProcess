'''
Target: 将数据划分为训练集和测试集， 比例是按照trainval_percent和train_percent来分配
Using:
1 将文件里的xml文件放到Annotations里面， 然后将jpg文件放到images文件夹里面
2 查看路径是否对，root是当前数据dataset的根路径，xmlfilepath存放标签xml的位置，txtsavepath存放分类好的文件名称
3 修改划分比例，比例关系train, val, test = trainval*train, trainval*(1-train), 1-trainval
Return:
返回ImageSets下的四个txt文件，存放划分后的文件名名称
'''

import os
import random

#划分数据集为训练集，测试集，验证集
root = r'E:\codeWork\yibiao\DataProcessYolov5\Method_kc\dataset/'
xmlfilepath = root+'Annotations'
txtsavepath = str(root)+'ImageSets'  # 存放划分的数据集的对应名称，文件名不含后缀名
trainval_percent = 1.0
train_percent = 0.9
if not os.path.exists(txtsavepath):
    os.mkdir(txtsavepath)

total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(str(root)+'ImageSets/trainval.txt', 'w')
ftest = open(str(root)+'ImageSets/test.txt', 'w')
ftrain = open(str(root)+'ImageSets/train.txt', 'w')
fval = open(str(root)+'ImageSets/val.txt', 'w')

for i in list:
    # name 去掉后缀名
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
print('done!')