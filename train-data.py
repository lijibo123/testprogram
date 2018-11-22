import input_data
import tensorflow as tf
from tensorflow.python.framework.graph_util import convert_variables_to_constants
#import tensorboard
mnist = input_data.read_data_sets("Minist_data/", one_hot = True)
x = tf.placeholder("float", [None, 784], name="input")  # 输入的数据集
y_ = tf.placeholder("float", [None, 10])

#  这里可以添加1隐藏层（具有神经元的隐藏层）
W1 = tf.Variable(tf.random_normal([784, 30]))
b1 = tf.Variable(tf.random_normal([30]))
y1 = tf.matmul(x, W1) + b1
output1 = tf.nn.sigmoid(y1) #激活函数

W2 = tf.Variable(tf.random_normal([30, 30]))
b2 = tf.Variable(tf.random_normal([30]))
y2 = tf.matmul(output1, W2) + b2
output2 = tf.nn.sigmoid(y2)

# 输出层
#W = tf.Variable(tf.zeros([20, 10]))
#b = tf.Variable(tf.zeros([10]))

W = tf.Variable(tf.random_normal([30, 10]),name='w')
b = tf.Variable(tf.random_normal([10]))
yy = tf.matmul(output2, W) + b
output = tf.nn.sigmoid(yy)

y = tf.nn.softmax(output, name = "final_result")

cross_entropy = -tf.reduce_sum(y_*tf.log(y)) # 基于训练数据计算误差估计的参数
train_step = tf.train.AdamOptimizer(0.01).minimize(cross_entropy)

#sess = tf.Session()
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(10000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict = {x: batch_xs, y_: batch_ys})
# 如何与前面训练好的模型进行交互？
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float32'))
    print(sess.run(accuracy, feed_dict = {x: mnist.test.images, y_: mnist.test.labels}))
    #saver = tf.train.Saver()
    #saver.save(sess, 'E:\\model_data/model.ckpt')
    #saver.restore(sess,"E:\\model_data/model.ckpt")
    graph_def = tf.get_default_graph().as_graph_def()  # 设置默认图
    output_graph_def = tf.graph_util.convert_variables_to_constants(sess, graph_def,['final_result'])
    with tf.gfile.GFile("test.pb",'wb') as f:
        f.write(output_graph_def.SerializeToString())





