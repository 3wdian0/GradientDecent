# coding: utf-8
# 数据
X = [1,       3,       5,       7,       9]
Y = [1*2+0.3, 3*2+0.3, 5*2+0.3, 7*2+0.3, 9*2+0.3]

# 变量
w,b = 0.,0.
def loss(x,l):
    y = wx+b
    loss = 1./2*(y-l)*(y-l)


step = 10000
eta  = 0.0001

for i in range(step):
    x = X[i%len(X)]
    y = Y[i%len(Y)]
    delta_w = (w*x+b-y)*x
    delta_b = (w*x+b-y)*1
    w = w - eta*delta_w
    b = b - eta*delta_b
    if abs(delta_w) < 0.00001:
        print delta_w
        break
print w,b
# 1.99934497056 0.304301451133
