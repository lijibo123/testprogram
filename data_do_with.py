import cv2
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
def img_rote(image, angle, center = None, scale = 1.0):

    # scale_ = 0.8
    (img_h, img_w) = image.shape[:2]
    #image = cv2.resize(image, (int(scale_*img_w), int(scale_*img_h)), interpolation=cv2.INTER_CUBIC)
    #(img_h, img_w) = image.shape[:2]
    if center is None:
        center = (img_w*0.5, img_h*0.5)
    rotated_M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(image, rotated_M, (img_w, img_h))
    return rotated_img

if __name__ == '__main__':
    with open('D:/img_mv.txt','r') as file:
        for line in file.readlines():
            img_name = line.replace('\n','')
            img = cv2.imread('D:/data1/'+ img_name)
            cv2.imwrite('D:/bugimg/dinge/'+img_name.split('.')[0]+'.jpg',img)
'''
'''
pd.set_option('display.max_columns', None)
path = os.path.join('D:/', 'image_info_child.csv')
df = pd.read_csv(path)
#print(df.head(100))
#colo = df.head(400)
#colo.to_csv('D:/img_info1.csv')

# colo = df[['文件名','角度']]cd ..
# colo.to_csv('D:/image_info_child.csv', index = 0)
# print('over!')
print(len(df))
for i in range(len(df)):
    # img_name.append(df.loc[i,'文件名'])
    if df.loc[i,'角度'].isna():
    # img_label.append(df.loc[i,'角度'])
      print(df.loc[i,'角度'])
print(img_name)
print(len(img_label))
'''