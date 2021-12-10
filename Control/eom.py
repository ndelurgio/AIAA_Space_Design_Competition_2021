import numpy as np
from Control.test import q_matrix
from state import State
from vehicle import Vehicle
from enviornment import Enviornment
class EOM():
    def solve(self,vehicle,enviornment):
        Fb = vehicle.F + enviornment.F
        Fi = self.rotate(vehicle.state.q,Fb)
        Mb = vehicle.M + enviornment.M
        xdot = vehicle.state.v #Earth Frame
        vdot = Fi / vehicle.mass #Earth Frame
        qdot = 0.5*self.omega(vehicle.state.w)*vehicle.state.q
        wdot = np.linalg.inv(vehicle.inertia).dot((Mb - np.cross(vehicle.state.w,(vehicle.inertia*vehicle.state.w)) - vehicle.Idot*vehicle.state.w)) # Check
        ## Next step: write function that rotates a vector using quaternion. Need to rotate vehicle.F.
        
    def omega(w):
        omega = np.array([[0   , -w[0],  -w[1], -w[2]], 
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
    
    def rotate(self,q,va):
        qinv = np.array([q[0],-q[1],-q[2],-q[3]])
        va = np.array([0,va[0],va[1],va[2]])
        vb = self.q_mult(self.q_mult(qinv,va),q)
        return np.array([vb[1],vb[2],vb[3]])
        
    
        