import numpy as np

x_all = np.array(([2, 9], [1, 5], [3, 6], [5, 10]), dtype=float) # input data
y = np.array(([92], [86], [89]), dtype=float) # output

x_all = x_all/np.amax(x_all, axis=0)
y = y/100 

X = np.split(x_all, [3])[0] 
x_predicted = np.split(x_all, [3])[1]

class neural_network(object):
  def __init__(self):
    #parameters
    self.inputSize = 2
    self.outputSize = 1
    self.hiddenSize = 3

    #weights
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize) 
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

  def forward(self, X):
    self.z = np.dot(X, self.W1) 
    self.z2 = self.sigmoid(self.z) 
    self.z3 = np.dot(self.z2, self.W2) 
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))

nn = neural_network()

o = nn.forward(X)

print ("Predicted Output: \n" + str(o))
print ("Actual Output: \n" + str(y))
