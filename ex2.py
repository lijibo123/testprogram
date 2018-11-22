import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
'''
# this a simple test of neural net
x_data = np.float32(np.random.rand(2, 100))
y_data = np.dot([0.100, 0.200], x_data) + 0.300

b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

print(init)

sess = tf.Session()
sess.run(init)

for step in range(0, 201):
    sess.run(train)
    if step % 20 ==0:
        print(step, sess.run(W), sess.run(b))
'''
def add_layer(inputs,in_size,out_size,activation_function = None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
       outputs = Wx_plus_b
    else:
       outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1, 1, 300, dtype = np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data)-0.5 + noise  # has question?

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

l1 = add_layer(xs, 1, 10, activation_function = tf.nn.relu)
prediction = add_layer(l1, 10, 1, activation_function = None)
tf.summary.histogram("yuce", prediction)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
tf.summary.scalar("loss", loss)

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init = tf.global_variables_initializer()

sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('logs/', sess.graph)
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)

for i in range(2000):
   _, su = sess.run([train_step, merged], feed_dict={xs: x_data, ys: y_data})
   writer.add_summary(su, global_step = i)
   if i%50 == 0:
       #print(sess.run(loss,feed_dict={xs: x_data,ys: y_data}))
      try:
          ax.lines.remove(lines[0])
      except Exception:
          pass
      prediction_value = sess.run(prediction,feed_dict={xs: x_data})
      lines = ax.plot(x_data,prediction_value, 'r-', lw=5)
      plt.pause(1)
writer.close()