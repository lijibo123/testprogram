import cv2
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
#PATH =''  # 模型存放的路径
#此程序为前后端集成的后台程序

'''
with tf.Session() as sess:
    saver = tf.train.import_meta_graph('E:/model_data/model.ckpt-2257.meta')
    #saver = tf.train.Saver()
    saver.restore(sess, 'E:/model_data/model.ckpt')
    #graph = tf.get_default_graph()

'''
PATH ='/model_data/&&&&.pb'  # 模型存放的路径
#图像基于.pb 模型进行推断
# 图像的输入函数并定义
def image_object_detect(path, sess, detection_graph):

    image = cv2.imread(path)
    #对图片的维度进行修改
    image_expanded = np.expand_dims(image, axis=0)
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    gboxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    gscores = detection_graph.get_tensor_by_name('detection_scores:0')
    gclasses = detection_graph.get_tensor_by_name('detection_classes:0')
    gnum_detections = detection_graph.get_tensor_by_name('num_detections:0')
    #进行检测
    (boxes, scores, classes, num_detections) = sess.run([gboxes, gscores, gclasses, gnum_detections],
                                                       feed_dict={image_tensor: image_expanded})
    #检测结果展示
    boxes = np.squeeze(boxes)
    box = []
    box_dic = {}
    scores = np.squeeze(scores)
    height, width = image.shape[:2]
    for i in range(boxes.shape[0]):
        if (scores is None or scores[i]>0.5): #判断图片的预测结果是否满足对应的阈值
            ymin, xmin, ymax, xmax = boxes[i]
            ymin = int(ymin*height)
            ymax = int(ymax*height)
            xmin = int(xmin*width)
            xmax = int(xmax*width)
            box.append([ymin,ymax,xmin,xmax])
    if len(box) > 0:
        box_dic['box'] = box
    else:
        box_dic = {"status":404,"response":"Can't recognitize image!"}

        '''
        score = None if scores is None else scores[i]
        font = cv2.FONT_HERSHEY_SIMPLEX #嵌入字体的类型
        text_x = np.max((0, xmin - 10)) #字体的左下角的位置
        text_y = np.max((0, ymin - 10))
        cv2.putText(image, 'Detection score: ' + str(score)+ str(np.max(classes, 1)), (text_x, text_y), font, 0.4, (0, 0, 0))
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 0), 2)
        '''
    #os.remove(path) #删除暂存在临时文件中的图片
    return box_dic

if __name__ == '__main__':
    # 定义默认图，并将存储的图结构导入
    detect_graph = tf.Graph()
    with detect_graph.as_default():
        graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH, 'rb') as fid:
            graph_def.ParseFromString(fid.read())
            tf.import_graph_def(graph_def, name='')
        image_tensor = detect_graph.get_tensor_by_name('image_tensor:0')
        gboxes = detect_graph.get_tensor_by_name('detection_boxes:0')
        gscores = detect_graph.get_tensor_by_name('detection_scores:0')
        gclasses = detect_graph.get_tensor_by_name('detection_classes:0')
        gnum_detections = detect_graph.get_tensor_by_name('num_detections:0')

        sess = tf.Session(graph=detect_graph)  # 启动会话
        image = cv2.imread('D:/graph/pay.jpg')  # 读取图像
        out_image = image_object_detect(image, sess, detect_graph)
        #cv2.imshow('img',out_image) # 图像的输出
        #cv2.waitKey(0)
        plt.imshow(out_image)
        plt.show()