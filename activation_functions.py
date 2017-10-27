'''
    write various activation functions.

'''


import numpy as np

# step functions
def step_function(x):
    return np.array(x > 0, dtype = np.int)

# sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Rectified Linear Unit
def relu(x):
    return np.maximum(0, x)
