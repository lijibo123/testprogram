
import tensorflow as tf
import numpy as ny

# 这个是 Tesorflow的一个测试程序情况
#node1 = tf.constant([-.3,4.0], tf.float32)
#node2 = tf.constant(4.0)
#node3 = tf.square(node2) #node1+node2 #tf.add(node1, node2)
sess = tf.Session()
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x + b
init = tf.global_variables_initializer()
sess.run(init)

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
#print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b,[1.])
sess.run([fixW, fixb])
#  print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
sess.run(init)
for i in range(1000):
    sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})
print(sess.run([W,b,loss],{x:[1,2,3,4],y:[0,-1,-2,-3]}))
