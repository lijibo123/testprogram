#模型下载
import cv2
import numpy as np
import keras.backend as K
from keras.models import load_model

# 设置成服务框架的形式
class angle_model():

    # 构造函数
    def __init__(self):
        self.model = None

    # 角度误差计算
    def angle_error(self, y_true, y_pred):

         """
         Calculate the mean diference between the true angles
         and the predicted angles. Each angle is represented
         as a binary vector.
         """
         # diff = angle_difference(K.argmax(y_true
         # ), K.argmax(y_pred))
         diff = 0.0
         return K.mean(K.cast(K.abs(diff), K.floatx()))

    def retrive_model(self, model_location):
        """
         model_location: path of model
        """
        self.model = load_model(model_location, custom_objects={'angle_error':self.angle_error})
    # 角度预测
    def predict(self,image_init):
        """
         img:image
        """
        image_init = cv2.cvtColor(image_init,cv2.COLOR_BGR2RGB)
        image = cv2.resize(image_init, (300, 300))  # 图片的大小调整
        image_input = np.asarray([image], dtype='float32') # 维度调整
        if image_input.ndim == 3:
           image_input = np.expand_dims(image_input, axis=3)

        y_pred = np.argmax(self.model.predict(image_input), axis=1) # 角度预测
        label_map = {0:0, 1:90, 2:180, 3:270}  # 标签与角度映射
        y_pred = label_map[y_pred[0]] + 90
        return y_pred