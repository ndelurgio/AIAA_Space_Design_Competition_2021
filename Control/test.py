import numpy as np
def omega(w):
        omega = np.matrix([[0   , -w[0],  -w[1], -w[2]], 
                           [w[0],     0,   w[2], -w[1]],
                           [w[1],  -w[2],     0,  w[0]],
                           [w[2],   w[1], -w[0],    0]])
        return omega

def q_matrix(q):
        qmat = np.array([[q[0],-q[1],-q[2],-q[3]],
                         [q[1], q[0], q[3],-q[2]],
                         [q[2],-q[3], q[0], q[1]],
                         [q[3], q[2],-q[1], q[0]]])
        return qmat
def q_mult(r,s):
    t = q_matrix(r).dot(s)
    return t
def rotate(q,va):
    qinv = np.array([q[0],-q[1],-q[2],-q[3]])
    va = np.array([0,va[0],va[1],va[2]])
    r = q_mult(qinv,va)
    vb = q_mult(q_mult(qinv,va),q)
    return np.array([vb[1],vb[2],vb[3]])
va = np.array([1,0,0])
q = np.array([0.707,0,0,0.707])
vb = rotate(q,va)
print(vb)
#x = np.array([1,2,3,4])
#y = q_matrix(x)
#z = y.dot(x)
#print(y)
#print(x)
#print(z)
#w = np.array([1,2,3])
#o = omega(w)
#print(o)