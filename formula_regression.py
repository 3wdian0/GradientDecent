# coding: utf-8
import numpy as np

def loss(x,l):
    y = wx+b
    loss = 1./2*(y-l)*(y-l)

# 数据
X = np.array([1.,       3,       5,       7,       9],      dtype=np.float32)
Y = np.array([1*2+0.3, 3*2+0.3, 5*2+0.3, 7*2+0.3, 9*2+0.3],dtype=np.float32)

# 变量
w,b = 0.,0.

# 优化算法三要素
# 0.初始参数
# 1.学习率
# 2.梯度
# 3.参数更新方式
eta  = 0.0001

# 停止条件
step = 3000
for i in range(step):
    x = X[i%len(X)]
    y = Y[i%len(Y)]
    delta_w = (w*x+b-y)*x
    delta_b = (w*x+b-y)*1.
    w = w - eta*delta_w
    b = b - eta*delta_b
    if i%100==0:
        print i,delta_w
print w,b
# 1.99934497056 0.304301451133
