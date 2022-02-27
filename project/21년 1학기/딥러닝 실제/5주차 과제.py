import numpy as np

def AND(A, B):
    x = np.array([A, B])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(A, B):
    x = np.array([A, B])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NAND(A, B):
    x = np.array([A, B])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def XOR(A, B):
    s1 = NAND(A, B)
    s2 = OR(A, B)
    y = AND(s1, s2)
    return y

def Full_Adder(A, B, C_in):
    S = XOR(XOR(A, B), C_in)
    C_out = OR(AND(XOR(A, B), C_in), AND(A, B))
    return S, C_out


print(Full_Adder(0, 0, 0))
print(Full_Adder(0, 0, 1))
print(Full_Adder(0, 1, 0))
print(Full_Adder(0, 1, 1))
print(Full_Adder(1, 0, 0))
print(Full_Adder(1, 0, 1))
print(Full_Adder(1, 1, 0))
print(Full_Adder(1, 1, 1))