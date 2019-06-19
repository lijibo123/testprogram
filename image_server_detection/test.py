import cv2
import tensorflow as tf
import numpy as np
from tensorflow.python.platform import gfile
import time
import h5py
# .hdf5类型的文档处理后的情况
image_path = "D:/00e8564494844ee9aca763536fb528e5DPC.jpg"
img = cv2.imread(image_path, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
image = cv2.resize(img, (300, 300))  # 输入图片的大小需要重新调整
image_input = np.asarray([image], dtype='float32')

if image_input.ndim == 3:
    image_input = np.expand_dims(image_input, axis=3)
'''
with h5py.File("D:/program files/git/RotNet/train/models/rotnet_street_view_resnet50.hdf5",'r') as f:

      x_data = f['x_data']
      model.predict(x_data)
'''

# pb文档的提取
with gfile.FastGFile("model.pb",'rb') as file:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(file.read())

# 会话开始
with tf.Session() as sess:
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')
    graph = tf.get_default_graph()
    input = graph.get_tensor_by_name("input_1:0")
    out = graph.get_tensor_by_name("outname:0")

    image_path = "D:/00e8564494844ee9aca763536fb528e5DPC.jpg"
    img = cv2.imread(image_path, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
    image = cv2.resize(img, (300, 300))  # 输入图片的大小需要重新调整
    image_input = np.asarray([image], dtype='float32')

    if image_input.ndim == 3:
        image_input = np.expand_dims(image_input, axis=3)
    start = time.clock()
    sess.run(tf.global_variables_initializer())

    predict = sess.run(out, feed_dict={input:image_input})
    print(np.argmax(predict, axis=1))

    end0 = time.clock()
    print(end0 - start)
