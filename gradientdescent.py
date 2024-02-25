import numpy as np
def gradientdescent(x,y):
    m_curr=0
    b_curr=0
    iterations=10
    learning_rate=0.01
    n=len(x)
    for i in range(iterations):
        y_predicted=m_curr*x+b_curr
        md=-(2/n)*sum(x*y-y_predicted)
        bd=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        print("m{},b{},iterations{}".format(m_curr,b_curr,i))
x=np.array([1,2,3,4,5,6])
y=np.array([4,5,6,7,8,8])
gradientdescent(x,y)