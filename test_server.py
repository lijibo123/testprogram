import sys 
import json
import base64
import requests
import os
import cv2
import pickle
import time

# 提取图片的类型
def img_read(fname):
    """
    :param fname:
    """
    image = open(fname, 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    #print(image_64_encode)

    files = {
           'file': image_64_encode
         }

    r = requests.post('http://*.*.*.*:9001/ticket/classify', data=files)
    print(r.text)
    con = json.loads(r.text)
    image.close()
    # 返回数据
    return con

# 调整图片的边缘
def img_size_chang(min, max,length):
    """
    :param min:
    :param max:
   """
    scope = 0.1*(max-min)
    min_ = 0 if min < scope else min-scope
    max_ = length if max+scope > length else max+scope
    return int(min_), int(max_)

# 图片切割
def img_cut(img, path, file_name, stor_list):

    """
    :param img:
    :param path:
    :param file:
    :param stor_list:
    """
    pat = 'E:/temp/'   # 切割后的图片存储位置（可修改）
    image = cv2.imread(path)
    height, weight = image.shape[:2]

    sta = img['status']['boxes']# 判断状态码
    lenth = len(img['data'])
    # 异常处理
    try:
     # 图片属性读取
     if sta == 200 and lenth > 0:
        i=0
        for boxs in img['data']['boxes']: # 根据接口返回的数据类型，提取图片属性
            tag = boxs['tag']
            ymin, xmin, ymax, xmax = boxs['box']
            confi = boxs['confidence']

            # 图像边缘调整
            y_min, y_max = img_size_chang(int(ymin*height), int(ymax*height), height)
            x_min, x_max = img_size_chang(int(xmin*weight), int(xmax*weight), weight)
            mid_img =image[y_min:y_max, x_min:x_max]

            # 文件名提取、文件保存
            (img_name, extension) = os.path.splitext(file_name)
            if lenth == 1:
                with open(os.getcwd()+'single_img_info.txt','a') as singlefile: #根据文件名进行测试文件
                    singlefile.write(file_name+','+tag+','+confi)
            if lenth > 1:
                img_id = "%02d" % i  # 数字格式化输出
                record = img_name + img_id + extension  # 注意将数字转化为字符串
                stor_list.append({'img_name':record,'img_tag':tag,'img_confi':confi})
                # 保存切割后的图片
                cv2.imwrite(pat + img_name + img_id + extension, mid_img)
                i = i+1
    except:
        return ("Error happend!")

    else:
      return ("ok!")

if __name__ == "__main__":

    with open(os.getcwd(),'a') as csvfile: # 创建新的文件头
        csvfile.write('img_name,'+'tag,'+'confidence')

    path = "D:/graph/"  # 图片的存储位置
    store_path = "E:/temp/record.txt" # 这是pickle文件的存储位置

    store_list = []

    # 这里需要进行批量处理
    for file_name in os.listdir(path):
        content = img_read(path + file_name)
        time.sleep(1)
        sta = img_cut(content, path + file_name, file_name, store_list)

    # 将数据保存为pickle类型文件
    with open(store_path, 'wb') as f:
        pickle.dump(stor_list, f)
    print(sta)
