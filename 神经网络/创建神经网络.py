import numpy as np

def sigmoid(x,deriv = False):
    #反向传播
    if (deriv == True):
    #sigmoid的导数是sigmoid*(1-sigmoid) 这里是x是经过sigmoid之后得到的值
        return x*(1-x)
    return 1/(1+np.exp(-x))

x = np.array([[0,0,1],
           [0,1,1],
           [1,0,1],
           [1,1,1],
           [0,0,1]]
)
y = np.array([[0],[1],[1],[0],[0]])
np.random.seed(1)
#random生成的是0到1的浮点数 乘2再减去1得到的是-1到1之间的值
w0 = 2 * np.random.random((3,4))-1
w1 = 2 * np.random.random((4,1))-1

for j in range(60000):
    #正向传播
    l0 = x
    l1net = np.dot(l0,w0)
    l1out = sigmoid(l1net)
    l2net = np.dot(l1out,w1)
    l2out = sigmoid(l2net)
    #dEout2
    l2_error = y-l2out
    if (j%10000==0):
        print("Error:%2f"%(np.mean(np.abs(l2_error))))
    #反向传播 w1对损失值的影响
    dout2net2 = l2out * (1-l2out)
    dnet2w1 = l2out.T
    w1effect = dnet2w1.dot(l2_error * dout2net2)
    #dEnet2=dEout2*dout2net2
    dEnet2 = l2_error * dout2net2
    #dEout1=dEnet2 * dnet2out1
    dEout1 = dEnet2.dot(w1.T)
    dout1net1 = l1out * (1-l1out)
    dnet1w0 = l0.T
    w0effect = dnet1w0.dot(dEout1 * dout1net1)
    w1+= w1effect
    w0+= w0effect

