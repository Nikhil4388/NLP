# demonstrates how to do gradient descent with numpy matrices.
#
# the notes for this class can be found at: 
# https://www.udemy.com/data-science-logistic-regression-in-python

import numpy as np
import matplotlib.pyplot as plt

N = 100
D = 2


X = np.random.randn(N,D)

# center the first 50 points at (-2,-2)
X[:50,:] = X[:50,:] - 2*np.ones((50,D))

# center the last 50 points at (2, 2)
X[50:,:] = X[50:,:] + 2*np.ones((50,D))

# labels: first 50 are 0, last 50 are 1
T = np.array([0]*50 + [1]*50)

# add a column of ones
ones = np.array([[1]*N]).T
Xb = np.concatenate((ones, X), axis=1)

# randomly initialize the weights
w = [0, -1, 1]

# calculate the model output
z = Xb.dot(w)

def sigmoid(z):
    return 1/(1 + np.exp(-z))


Y = sigmoid(z)

# calculate the cross-entropy error
def cross_entropy(T, Y):
    E = 0
    for i in xrange(N):
        if T[i] == 1:
            E -= np.log(Y[i])
        else:
            E -= np.log(1 - Y[i])
    return E


def plot_w(linestyle, label):
    x_axis = np.linspace(-6, 6, 100)
    y_axis = w[0] + x_axis * (-w[2] / w[1])
    return plt.plot(x_axis, y_axis, linestyle=linestyle, label=label)

legend1, = plot_w('--', 'start')
# let's do gradient descent 100 times
learning_rate = 0.1
for i in xrange(100):
    if i % 10 == 0:
        print cross_entropy(T, Y)

    # gradient descent weight udpate
    derivatives = np.dot((T - Y).T, Xb)
    w += learning_rate * derivatives

    # recalculate Y
    Y = sigmoid(Xb.dot(w))


print "Final w:", w

# plot the data and separating line
plt.scatter(X[:,0], X[:,1], c=T, s=100, alpha=0.5)

legend2, = plot_w('-', 'final')
plt.legend([legend1, legend2])
plt.show()

