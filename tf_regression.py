# coding: utf-8
import os
import numpy      as np
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"

def loss(x,l):
    y = wx+b
    loss = 1./2*(y-l)*(y-l)

# 数据
X = [1,       3,       5,       7,       9]
Y = [1*2+0.3, 3*2+0.3, 5*2+0.3, 7*2+0.3, 9*2+0.3]
x_train = tf.placeholder(shape=[None, 1], dtype=tf.float32);
y_train = tf.placeholder(shape=[None, 1], dtype=tf.float32);

# 变量
w = tf.Variable([[0.]],name="w")
b = tf.Variable([[0.]],name="b")

y = w*x_train+b
loss = 1./2*(y-y_train)*(y-y_train)

eta  = 0.0001
#optimizer = tf.train.AdagradOptimizer(eta)
optimizer = tf.train.GradientDescentOptimizer(eta)
train_op = optimizer.minimize(loss)

delta_w = tf.gradients(loss,w)

# 
init_op = tf.global_variables_initializer()
init_local_op = tf.local_variables_initializer()

# 优化算法三要素
# 0.初始参数
# 1.学习率
# 2.梯度
# 3.参数更新方式

# 停止条件
step = 3000
with tf.Session() as sess:
    sess.run(init_op)
    sess.run(init_local_op)
    for i in range(step):
        x = np.array([[X[i%len(X)]]])
        y = np.array([[Y[i%len(Y)]]])
        #print x.shape
        cur_loss, cur_train_op, cur_delta_w = sess.run([loss, train_op, delta_w], feed_dict={x_train: x, y_train:y})
        #print cur_delta_w
        cur_delta_w = cur_delta_w[0][0][0]
        if i%100==0:
            print "{}\t{}".format(i,cur_delta_w)
    print sess.run(w),sess.run(b)
# 1.99934497056 0.304301451133
