'''
Target: 将前面划分好的数据和标签转为yolo的txt文件格式
Using: 这里采用的是绝对路径，可以不受当前py文件位置的影响，只需要执行的时候修改root和class
File_before:
    dataset
        Annotations  # 存放标签xml的位置
        images       # 存放图片jpg的位置
        ImageSets    # 之前划分数据集的文件名
    3.voc_yolo_absolute.py
File_after:
    dataset
        Annotations  # 存放标签xml的位置
        images       # 存放图片jpg的位置
        ImageSets    # 之前划分数据集的文件名
        labels       # xml文件转为了txt文件
        test.txt     # 划分的文件名
        train.txt    # 划分的文件名
        val.txt      # 划分的文件名
    3.voc_yolo_absolute.py
'''
import xml.etree.ElementTree as ET
import os

sets = ['train', 'val', 'test']
classes = ["yibiao", "00050000", "00050001", "00060000", "00060001", "00100000", "00100001", "00110000", "00110001"]
root = r'E:\codeWork\yibiao\DataProcessYolov5\Method_cvmart\dataset/'
abs_path = os.getcwd()
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
def convert_annotation(image_id, root):
    in_file = open(str(root)+'Annotations/%s.xml'%( image_id))
    out_file = open(str(root)+'labels/%s.txt'%(image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        #difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes :
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

for image_set in sets:

    if not os.path.exists(str(root)+'labels/'):
        os.makedirs(str(root)+'labels/')
    image_ids = open(str(root)+'ImageSets/%s.txt'%(image_set)).read().strip().split()
    list_file = open(str(root)+'%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write(str(root)+'images/%s.jpg\n'%(image_id))
        convert_annotation(image_id, root)
    list_file.close()
    print('done!')
