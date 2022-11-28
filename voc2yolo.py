import numpy as np
import xml.etree.ElementTree as et
import os

xml_dir = '/home/fedyautkin/PycharmProjects/pythonProject4py379/neuro/VOC2028/1/' #path to .xml files
txt_dir = '/home/fedyautkin/PycharmProjects/pythonProject4py379/neuro/VOC2028/2/' #path to create .txt files
xml_files = os.listdir(xml_dir)
for file_name in (xml_files):
    xmin = xmax = ymin = ymax = files = names = labels_id = []
    a= str(xml_dir + file_name)
    tree = et.parse(a)
    root = tree.getroot()
    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)
    for tag1 in root.findall('object/name'):
        if str(tag1.text) == 'hat':
            labels_id = np.append(labels_id, '0')
        else:
            labels_id = np.append(labels_id, '1')
    for tag1 in root.findall('object/bndbox/xmin'):
        xmin = np.append(xmin, int(tag1.text))
    for tag1 in root.findall('object/bndbox/xmax'):
        xmax = np.append(xmax, int(tag1.text))
    for tag1 in root.findall('object/bndbox/ymin'):
        ymin = np.append(ymin, int(tag1.text))
    for tag1 in root.findall('object/bndbox/ymax'):
        ymax = np.append(ymax, int(tag1.text))
    width_norm = (xmax-xmin)/width
    height_norm = (ymax-ymin)/height
    xmin = xmin
    x_center_norm = (((xmax-xmin)//2)+xmin)/width
    y_center_norm = (((ymax-ymin)//2)+ymin)/height

    txt_file_name = (txt_dir + file_name[:-3] + 'txt')
    file_txt = open(txt_file_name, 'w+')
    for i in range(len(labels_id)):
        textt = (str(labels_id[i]) + ' ' + str(x_center_norm[i]) + ' ' + str(y_center_norm[i]) + ' ' + str(width_norm[i]) + ' ' + str(height_norm[i]))
        file_txt.write(f"{textt}\n")
    file_txt.close