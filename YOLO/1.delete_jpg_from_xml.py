'''
Target:
delete_jpg_from_xml: 删除多余的没有参与标注的图片jpg
Using:
1 输入jpg文件夹路径images_dir
2 输入xml文件夹路径xml_dir
Remarks:
delete_jpg_from_xml: 根据xml文件删除多余的jpg图片
其他函数：
delete_xml_from_jpg： 根据图片删除多余的xml文件
select_xml_from_size： 删除大小小于指定大小的xml，例如size<=1kb
delect_bbox_out_image： 删除框的标注边界值超出了图像的边界
'''

import os
import xml.etree.ElementTree as ET

def delete_jpg_from_xml(images_dir, xml_dir):
    '''
    Target: 根据xml文件删除多余的jpg图片
    params:
        images_dir: 放图片jpg的文件路径
        xml_dir: 放标签xml的文件路径
    '''
    # 创建列表
    xmls = []
    # 读取xml文件名(即：标注的图片名)
    for xml in os.listdir(xml_dir):
        # xmls.append(os.path.splitext(xml)[0])    #append()参数：在列表末尾添加新的对象，即将所有文件名读入列表
        xmls.append(xml.split('.')[0])  # splitext和split的区别：前者('0001','.jpg'), 后者('0001','jpg') 在此可选用
    print(xmls)

    # 读取所有图片
    for image_name in os.listdir(images_dir):
        image_name = image_name.split('.')[0]
        if image_name not in xmls:
            image_name = image_name + '.jpg'
            print(image_name)
            os.remove(os.path.join(images_dir, image_name))
    print("done!")

# =================================================
# 其他功能函数
# =================================================
def delete_xml_from_jpg(images_dir, xml_dir):
    '''
    Target: 根据图片删除多余的xml文件
    params:
        images_dir: 放图片jpg的文件路径
        xml_dir: 放标签xml的文件路径
    '''
    # 创建列表
    imgs = []
    # 读取图片名
    for img in os.listdir(images_dir):
        # xmls.append(os.path.splitext(xml)[0])    #append()参数：在列表末尾添加新的对象，即将所有文件名读入列表
        imgs.append(img.split('.')[0])  # splitext和split的区别：前者('0001','.jpg'), 后者('0001','jpg') 在此可选用
    print(imgs)

    # 读取所有xml文件
    for xml_name in os.listdir(xml_dir):
        xml_name = xml_name.split('.')[0]
        if xml_name not in imgs:
            xml_name = xml_name + '.xml'
            print(xml_name)
            os.remove(os.path.join(xml_dir, xml_name))
    print('done!')


def select_xml_from_size(xml_dir):
    '''
    Target: 删除大小小于指定大小的xml，例如size<=1kb
    params:
        xml_dir: 放标签xml的文件路径
    '''
    for root, dirs, files in os.walk(xml_dir):
        for file in files:
            filename = os.path.join(root, file)
            size = os.path.getsize(filename)
            # 1kb=1024
            if size < 1 * 1024:
                print("remove", filename)
                os.remove(filename)
    print('done!')

def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(root, file))
    return L


def delect_bbox_out_image(xml_dir):
    '''
    Target: 删除框的标注边界值超出了图像的边界
    '''
    count = 0
    xml_dirs = file_name(xml_dir)
    for i in range(0, len(xml_dirs)):
        # print(xml_dirs[i])
        annotation_file = open(xml_dirs[i]).read()
        root = ET.fromstring(annotation_file)
        label = root.find('filename').text
        # print(label)
        count_label = count

        # get the pictures' width and height
        for size in root.findall('size'):
            label_width = int(size.find('width').text)
            label_height = int(size.find('height').text)

        # get the boundbox's width and height
        for obj in root.findall('object'):
            for bbox in obj.findall('bndbox'):
                label_xmin = int(bbox.find('xmin').text)
                label_ymin = int(bbox.find('ymin').text)
                label_xmax = int(bbox.find('xmax').text)
                label_ymax = int(bbox.find('ymax').text)
                if label_xmin <= 0 or label_xmax > label_width or label_ymin <= 0 or label_ymax > label_height:
                    # judge the filename is not repeat
                    if label_temp == label:
                        continue
                    print('--' * 30)
                    print(xml_dirs[i])  # print the xml's filename
                    # print(label)
                    print("width:", label_width)
                    print("height:", label_height)
                    print(label_xmin, label_ymin, label_xmax, label_ymax)
                    print('--' * 30)
                    count = count + 1
                    os.remove(xml_dirs[i])
            label_temp = label
    print("================================")
    print(count)


if __name__ == '__main__':
    images_dir = r'E:\codeWork\yibiao\DataProcessYolov5\Method_kc\dataset\images'
    xml_dir = r'E:\codeWork\yibiao\DataProcessYolov5\Method_kc\dataset\Annotations'
    delete_jpg_from_xml(images_dir, xml_dir)
    # delete_xml_from_jpg(images_dir, xml_dir)
    # delect_bbox_out_image(xml_dir)