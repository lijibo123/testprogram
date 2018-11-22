import tensorflow as tf
import numpy as np
import input_data
from tensorflow.python.framework.graph_util import convert_variables_to_constants
#from tensorflow.python.framework import graph_util
minist = input_data.read_data_sets("Minist_data/" ,one_hot = 'False')
'''
# 模型的保存方式一（生成多个文件）
with tf.Session() as sess:
    saver = tf.train.import_meta_graph('E:\\model_data\\model.ckpt.meta')
    #saver = tf.train.Saver()
    saver.restore(sess, 'E:\\model_data\\model.ckpt')
    #graph = tf.get_default_graph()
    label1 = tf.placeholder("float",[None, 10])
    y1 = sess.graph.get_tensor_by_name('final_result:0')
    x = sess.graph.get_tensor_by_name('input:0')
    #output = tf.argmax(y1, 1)  # 使用tensorflow的函数，需要在Session中建立会话。
    #output1 = tf.argmax(label1, 1)
    output = sess.run(tf.argmax(y1,1),feed_dict = {x:minist.test.images})
    output2 = sess.run(tf.argmax(label1,1), feed_dict = {label1:minist.test.labels})
    #print(len(output),len(output2))
    num = 0
    for i in range(len(output)):
        if output[i] != output2[i]:
            print(output[i],output2[i])
            num += 1
    print(output2)
    #print(sess.run(output, feed_dict ={x:minist.test.images})) # 根据存储的模型进行预测处理
    #print(sess.run(output1, feed_dict = {label1:minist.test.labels})) #

    #print(sess.run('w:0'))
'''
with tf.Session() as sess:  # persisted_sess:
    with tf.gfile.FastGFile('test.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        #persisted_sess.graph.as_default()
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name = '')
    #with tf.Session() as sess:
        input_x = sess.graph.get_tensor_by_name("input:0")
        print(input_x)
        y = sess.graph.get_tensor_by_name("final_result:0")
        out = sess.run([y],feed_dict={input_x:minist.test.images})
        print(out)
        #w1 = sess.graph.get_tensor_by_name("w:0")

'''
class init(object):
    def __init__(self):
        #self.de = 10
        #self.le = 1
        print("hello world")

    def num(self,a,b):
        self.de = a
        self.le = b
        self.c = self.de + self.le
        #return True
    def out(self):
        resu = self.de + self.le
        print(self.c)
cf = init()
cf.num(2,3)
print(cf.de)
cf.out()
'''