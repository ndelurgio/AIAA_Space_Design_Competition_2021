import numpy as np
def omega(w):
        omega = np.matrix([[0   , -w[0],  -w[1], -w[2]], 
                           [w[0],     0,   w[2], -w[1]],
                           [w[1],  -w[2],     0,  w[0]],
                           [w[2],   w[1], -w[0],    0]])
        return omega
    
w = np.array([1,2,3])
o = omega(w)
print(o)