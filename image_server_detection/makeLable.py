import os
import math
import PIL.ImageDraw as ImgD
from PIL import Image

SINGLES = '/home/data/single_img_info.txt'
IMG_DIR = '/home/**/image/data/orginal_images/'
BOX_RCD = '/home/***/image/data/label_files/csv/records_rectify.csv'
OUT_DIR = '/home/***/img/'
SIZE = (480, 480)

# 单票据图片信息提取
def getImgList(singles):
    #TODO
    #读取单个图片文件的信息
    single_imgs = []
    with open(singles, 'rb') as single_img_fil:
        for line in single_img_fil.readlines():
           img_name = line.decode(encoding='utf-8').replace('\n', '').split(',')[0]
           if img_name[:4] != 'name':
               single_imgs.append(img_name)
        return single_imgs


def data_compare_imgsize(var, length, resize):
    if var < 0:
        var = 0
    if var > length:
        var = length
    var = math.ceil(resize*var/length) # 向上取值
    return var

# 提取box顶点信息
def getBox(single_img_name):
    #TODO
    # resize to SIZE
    label = False
    with open(BOX_RCD, 'rb') as file_:
        for line in file_.readlines():
            img_info = line.decode(encoding='utf-8').replace('\n', '').split(',')
            img_name = img_info[0]
            if img_name.split('/')[-1] == single_img_name:
               img_weight = img_info[2]
               img_height = img_info[3]
               (x1, y1) = img_info[6:8]
               (x2, y2) = img_info[8:10]
               (x3, y3) = img_info[10:12]
               (x4, y4) = img_info[12:14]

               # x方向的数据处理
               x1 = data_compare_imgsize(int(x1), int(img_weight), SIZE[0])
               x2 = data_compare_imgsize(int(x2), int(img_weight), SIZE[0])
               x3 = data_compare_imgsize(int(x3), int(img_weight), SIZE[0])
               x4 = data_compare_imgsize(int(x4), int(img_weight), SIZE[0])

               # y方向的数据处理
               y1 = data_compare_imgsize(int(y1), int(img_height), SIZE[1])
               y2 = data_compare_imgsize(int(y2), int(img_height), SIZE[1])
               y3 = data_compare_imgsize(int(y3), int(img_height), SIZE[1])
               y4 = data_compare_imgsize(int(y4), int(img_height), SIZE[1])
               label = True
               box = list(zip([x1,x2,x3,x4],[y1,y2,y3,y4]))
               return tuple(box), label  # 以元组的数据形式返

        if not label:
              box = list(zip([0, 0, 0, 0], [0, 0, 0, 0]))
              return box, label

# 输入图片大小的调整
def createInput(img):
    #TODO resize image to SIZE
    # save to os.path.join(OUT_DIR, 'inputs', '***')
    image = Image.open(os.path.join(IMG_DIR, img))
    image = image.resize((SIZE[0], SIZE[1]))
    img_path = os.path.join(OUT_DIR, 'inputs')

    if not os.path.isdir(img_path):
        os.mkdir(img_path)
    image.save(img_path + '/' + img)
    return (img_path + '/' + img)

# 创建标签
def createLabel(box,img):

    lbimg = Image.new('L', SIZE, (0))
    lbimg = addLine(lbimg, box, color='l')
    lbl_path = os.path.join(OUT_DIR, 'lables')
    if not os.path.isdir(lbl_path):
        os.mkdir(lbl_path)
    lbimg.save(lbl_path+ '/' +img)
    return (lbl_path + '/' + img)

# add outline to img 
def addLine(bgimg, box, color='r'):
    cmap = {'r': (255, 0, 0),
            'g': (0, 255, 0),
            'b': (0, 0, 255),
            'w': (255, 255, 255),
            'l': (255),
            }
    draw = ImgD.Draw(bgimg)
    d1 = (box[3][0], box[3][1])
    for i in range(0, 4):
        d2 = (box[i][0], box[i][1])
        draw.line((d2, d1),fill=cmap[color], width=3)
        d1 = d2
    return bgimg

if __name__ == '__main__':
    imgs = getImgList(SINGLES)
    csv = open(os.path.join(OUT_DIR, 'inputs.csv'), 'wb')
    print(len(imgs))
    for img in imgs:
        box, label = getBox(img)

        if label:
           img_path = createInput(img)
           lbl_path = createLabel(box, img)
           line = img_path + ',' + lbl_path + '\n'
           csv.write(line.encode(encoding='utf-8'))

        if not label:
           with open(os.path.join(OUT_DIR,'un_find_img.csv'),'a') as unfindfile:
               unfindfile.write(img + '\n')
    csv.close()
    print('over!')



