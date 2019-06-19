#-*- coding:utf- -*-
import os
import sys
import json
import logging
import base64
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.escape
import numpy as np
import cv2
sys.path.append("D:/program files/git/RotNet/")
model_location = os.path.join("D:/program files/git/RotNet/",'train','models', 'rotnet_street_view_resnet50_01-0.0145_mixed.hdf5')
from rote_img import angle_model

m = angle_model()
m.retrive_model(model_location)
logger = logging.getLogger()

# 实现目标检测的句柄
class object_detectionHandler(tornado.web.RequestHandler):

    def post(self):
        # da = self.request.body
        da = self.get_argument("img")
        data = base64.b64decode(da)

        # 避免图片数据在本地存储
        img_array = np.fromstring(data,np.uint8)  # 图片传输的格式转化
        img = cv2.imdecode(img_array,cv2.IMREAD_COLOR)
        angle = m.predict(img)

        '''
        # data = self.request.files['image'][0]
        data = self.request.files.get('image')[0]
        dir = "E:/tem_image/"   # 路径的生成
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(dir+data['filename'], 'wb') as f:
            f.write(data['body']) # 先保存，然后再读入数据
            # img_box = object_detection(dir+data['filename'])
            image_init = cv2.imread(dir+data['filename'])
            image = cv2.resize(image_init, (300, 300))  # 输入图片的大小需要重新调整
            image_input = np.asarray([image], dtype='float32')  # 图像的传输格式要限制（4维的输入数据）
            if image_input.ndim == 3:
                image_input = np.expand_dims(image_input, axis=3)

            y_pred = np.argmax(model.predict(image_input), axis=1)
        #img_box = json.dumps(img_box)
        #self.write(img_box)
        '''
        da = json.dumps({"pred":int(angle)})
        self.write(da)

if __name__== '__main__':
    application = tornado.web.Application([(r"/", object_detectionHandler)]) # 路由分发
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(80)
    tornado.ioloop.IOLoop.current().start()