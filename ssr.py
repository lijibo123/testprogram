# 实现图像的增强算法
import cv2
import numpy as np
import matplotlib.pyplot as plt
#r, g, b = cv2.split(img)
#img_r = img[:, :, 2]

# dc = cv2.min(cv2.min(r,g),b)
# img_r = cv2.GaussianBlur(r, (11, 11), 0)
def singleScaleRectinex(img,sigma):
    temp = cv2.GaussianBlur(img, (0,0), sigma)
    gaussian = np.where(temp == 0, 0.1, temp)
    change_img = np.log10(img + 1.0) - np .log10(gaussian)
    return change_img

if __name__ == '__main__':
    # 图像增强算法的实现（SSR方法）
    img = cv2.imread('payment30.jpg')  # 彩色图像BGR的形式
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 105, 255, cv2.THRESH_BINARY)
    img = np.float32(img)
    dc = singleScaleRectinex(img, 100)
    # print(dc)
    dc = np.power(10, dc)
    maxn = np.max(dc)
    minn = np.min(dc)
    dc = 255*(dc - minn)/(maxn - minn)  # 图像的线性转换
    dc = np.uint8(dc)
    # print(dc)
    # cv2.imwrite('change.jpg', dc)
    hue_img = cv2.cvtColor(dc, cv2.COLOR_RGB2HSV)
    cv2.imwrite('daxie.jpg', img[1])
    plt.imshow(img[1])
    plt.show()

