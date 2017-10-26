import numpy as np

# define various logical gates
# AND
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

# NAND
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

# OR
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3

    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1
# XOR
def XOR(x1, x2):
    x = np.array([x1, x2])

    return AND(NAND(x1, x2), OR(x1, x2))
