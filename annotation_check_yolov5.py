import cv2 as cv
import os

txt_dir = '/home/fedyautkin/PycharmProjects/pythonProject4py379/neuro/VOC2028/txt/'
img_dir = '/home/fedyautkin/PycharmProjects/pythonProject4py379/neuro/VOC2028/JPEGImages/'
num_imgs = 15  # количество изображений для проверки разметки
img_files = os.listdir(img_dir)
for i in range(num_imgs):
    img = cv.imread(img_dir+img_files[i], 1)
    height, width = img.shape[:2]
    d = str(txt_dir+img_files[i][:-3]+'txt')
    txt = open(d, 'r')
    obj = txt.readlines()
    for k in range(len(obj)):
        label_id, x_center_norm, y_center_norm, width_norm, height_norm = obj[k].split()
        x_left = (float(x_center_norm) * float(width)) - ((float(width_norm) * float(width))/2)
        y_left = (float(y_center_norm) * float(height)) - ((float(height_norm) * float(height))/2)
        x_right = (float(x_center_norm) * float(width)) + ((float(width_norm) * float(width))/2)
        y_right = (float(y_center_norm) * float(height)) + ((float(height_norm) * float(height))/2)
        if label_id == '0':
            cv.rectangle(img,(int(x_left),int(y_left)),(int(x_right),int(y_right)),(0,255,0),2)
        elif label_id == '1':
            cv.rectangle(img,(int(x_left),int(y_left)),(int(x_right),int(y_right)),(0,0,255),2)
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()