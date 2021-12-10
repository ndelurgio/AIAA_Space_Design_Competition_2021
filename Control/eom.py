import numpy as np
from state import State
from vehicle import Vehicle
from enviornment import Enviornment
class EOM():
    def solve(self,vehicle,enviornment):
        Fb = vehicle.F + enviornment.F
        Fi = self.rotate(self.q_inv(vehicle.state.q),Fb)
        Mb = vehicle.M + enviornment.M
        xdot = vehicle.state.v #Inertial Frame
        vdot = Fi / vehicle.mass #Inertial Frame
        qdot = 0.5*self.omega(vehicle.state.w).dot(vehicle.state.q)
        wdot = np.linalg.inv(vehicle.inertia).dot((Mb - np.cross(vehicle.state.w,(vehicle.inertia.dot(vehicle.state.w))) - vehicle.Idot.dot(vehicle.state.w))) # Check
        return qdot, wdot, xdot, vdot
        
    def omega(self,w):
        omega = np.array([[0,    -w[0], -w[1], -w[2]], 
                          [w[0],     0,  w[2], -w[1]],
                          [w[1], -w[2],     0,  w[0]],
                          [w[2],  w[1], -w[0],    0]])
        return omega
    def q_matrix(self,q):
        qmat = np.array([[q[0],-q[1],-q[2],-q[3]],
                         [q[1], q[0], q[3],-q[2]],
                         [q[2],-q[3], q[0], q[1]],
                         [q[3], q[2],-q[1], q[0]]])
        return qmat
    
    def q_inv(self,q):
        return np.array([q[0],-q[1],-q[2],-q[3]])
    
    def q_mult(self,r,s):
        t = self.q_matrix(r).dot(s)
        return t
    
    def rotate(self,q,va):
        qinv = self.q_inv(q)
        va = np.array([0,va[0],va[1],va[2]])
        vb = self.q_mult(self.q_mult(qinv,va),q)
        return np.array([vb[1],vb[2],vb[3]])
        
    
        