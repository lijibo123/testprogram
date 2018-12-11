import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('D:/label/test/payment20.jpg')
hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

low_range = np.array([160, 110, 120])  # 饱和度及其亮度需要进行调整
high_range = np.array([180, 255, 255])
th = cv2.inRange(hue_image, low_range, high_range)  # 生成掩模矩阵
# img1 = cv2.bitwise_and(image,image,mask=th)
index1 = th == 255
img = np.zeros(image.shape, np.uint8)
img[:, :] = (255, 255, 255)
img[index1] = image[index1]
plt.imshow(img)
plt.show()


'''
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 当前路径
IMG_DIR = os.getcwd()
image = cv2.imread(os.path.join(IMG_DIR, 'payment9.jpg'))
fig = plt.figure(figsize=(18, 14))
color_range = [(140, 180), (110, 130), (0, 30)]  # GBR 在HSV空间的阈值范围

# 调整图像的颜色范围
for thresh in color_range:
    hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_range = np.array([thresh[0], 50, 120])
    high_range = np.array([thresh[1], 255, 255])
    th = cv2.inRange(hue_image, low_range, high_range)  # 生成掩模矩阵
    if th.max() == 255:
        # print(th.max())
        break
# img1 = cv2.bitwise_and(image, image, mask=th) # 背景颜色为黑色
index1 = th == 255
img = np.zeros(image.shape, np.uint8)
img[:, :] = (255, 255, 255)
img[index1] = image[index1]

# cv2.imwrite('payment1.jpg',image)
plt.imshow(img)
plt.show()
'''
