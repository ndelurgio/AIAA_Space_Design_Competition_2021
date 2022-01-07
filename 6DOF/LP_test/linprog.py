import numpy as np
import scipy.optimize as opt

#c = np.array([1.0,1.0,1.0,1.0])
#A = np.array([[1.0,2.0,3.0,4.0],[5.0,6.0,7.0,8.0]])
#b = np.array([10.0,10.0])
#res = opt.linprog(c,None,None,A,b)
#print(res)

F = 580.0 #580.080015
r = 4.0
l = 8.0
R = F * r
L = F * l / 2
A = np.array([[0,0,0,0,0,0,0,-F,F,0,-F,F,0,0,0,0,0,0,0,-F,F,0,-F,F],
            [0,-F,F,0,-F,F,0,0,0,0,0,0,0,-F,F,0,-F,F,0,0,0,0,0,0],
            [-F,0,0,-F,0,0,-F,0,0,-F,0,0,F,0,0,F,0,0,F,0,0,F,0,0],
            [0,L,-L,0,L,-L,-R,0,0,R,0,0,0,-L,L,0,-L,L,R,0,0,-R,0,0],
            [R,0,0,-R,0,0,0,-L,L,0,-L,L,-R,0,0,R,0,0,0,L,-L,0,L,-L],
            [0,-R,R,0,R,-R,0,R,-R,0,-R,R,0,-R,R,0,R,-R,0,R,-R,0,-R,R]])
c = np.ones(24)
b = np.array([0,0,0,1000,1500,1430])
bounds = (0,None)

res = opt.linprog(c,None,None,A,b,bounds)
#print(res.x)
for i in range(0,len(res.x)):
    print(res.x[i])