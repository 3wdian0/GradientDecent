# coding: utf-8
import numpy as np

X = np.array([1,       3,       5,       7,       9],      dtype=np.float32)
Y = np.array([1*2+0.3, 3*2+0.3, 5*2+0.3, 7*2+0.3, 9*2+0.3],dtype=np.float32)


w,b = 0.,0.
def loss_w(x,l,delta):
    y = (w+delta)*x+b
    loss = 1./2*(y-l)*(y-l)
    return loss

def loss_b(x,l,delta):
    y = w*x+(b+delta)
    loss = 1./2*(y-l)*(y-l)
    return loss




step = 1000000
eta  = 0.001
delta= 0.00000001

for i in range(step):
    x = X[i%len(X)]
    y = Y[i%len(Y)]
    delta_w = (loss_w(x,y,0.)-loss_w(x,y,delta))/(0.-delta)
    delta_b = (loss_b(x,y,0.)-loss_b(x,y,delta))/(0.-delta)
    w = w - eta*delta_w
    b = b - eta*delta_b
    if i%100==0:
        print i,delta_w
    if abs(delta_w) < 0.000000001:
        print delta_w
        break
print w,b
# 1.99999998285 0.300000081993
