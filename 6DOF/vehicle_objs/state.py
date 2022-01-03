import numpy as np
from eom import EOM
class State():
    def __init__(self, q0, w0, x0, v0): # q = [w v1 v2 v3]
        self.q = q0
        self.w = w0
        self.x = x0
        self.v = v0
        self.e = np.array([0,0,0],dtype=np.float64)
        self.dcm = np.array([[1,0,0],[0,1,0],[0,0,1]],dtype=np.float64)
        self.q2dcm()
        self.dcm2euler()
        self.eom = EOM()
        
        ## Previous statedots
        self.qdot_prev = np.array([0,0,0,0])
        self.wdot_prev = np.array([0,0,0])
        self.xdot_prev = np.array([0,0,0])
        self.vdot_prev = np.array([0,0,0])
        
    def setState(self,q,w,x,v):
        
        self.q = q
        self.w = w
        self.x = x
        self.v = v
    #def __init__(self): # q = [w v1 v2 v3]
    #    self.q = np.array([1,0,0,0])
    #    self.w = np.array([0,0,0])
    #    self.x = np.array([0,0,0])
    #    self.v = np.array([0,0,0])
    
    def propagate(self,qdot,wdot,xdot,vdot,dt):
        #Propogate Elements
        self.q = self.q + 0.5*(self.qdot_prev + qdot)*dt
        self.q = self.q / np.linalg.norm(self.q)
        self.w = self.w + 0.5*(self.wdot_prev + wdot)*dt
        self.x = self.x + 0.5*(self.xdot_prev + xdot)*dt
        self.v = self.v + 0.5*(self.vdot_prev + vdot)*dt
        
        self.qdot_prev = qdot
        self.wdot_prev = wdot
        self.xdot_prev = xdot
        self.vdot_prev = vdot
        
        #Compute DCM and Euler Angles
        self.q2dcm()
        self.dcm2euler()
        #print(self.dcm)
        
        # self.q = self.q + qdot*dt
        # self.q = self.q / np.linalg.norm(self.q)
        # self.w = self.w + wdot*dt
        # self.x = self.x + xdot*dt
        # self.v = self.v + vdot*dt
    def dcm2euler(self): #Roll, Pitch, Yaw
        self.e[0] = np.arctan2(self.dcm[0][1], self.dcm[0][0]) # YAW
        self.e[1] = -np.arcsin(self.dcm[0][2]) # PITCH
        self.e[2] = np.arctan2(self.dcm[1][2], self.dcm[2][2]) # ROLL
        
    def q2dcm(self):
        #(2*self.q[0]**2 - 1)*np.eye(3) + 2*np.transpose([self.q[1:3]])*self.q[1:3] - 2*self.q[0].dot(self.S(self.q[1:3]))
        self.dcm = np.array([[2*self.q[0]**2 - 1 + self.q[1]**2            , 2*self.q[1]*self.q[2] + 2*self.q[3]*self.q[0], 2*self.q[1]*self.q[3] - 2*self.q[2]*self.q[0]],
                             [2*self.q[1]*self.q[2] - 2*self.q[3]*self.q[0], 2*self.q[0]**2 - 1 + 2*self.q[2]**2          , 2*self.q[2]*self.q[3] + 2*self.q[1]*self.q[0]],
                             [2*self.q[1]*self.q[3] + 2*self.q[0]*self.q[2], 2*self.q[2]*self.q[3] - 2*self.q[0]*self.q[1], 2*self.q[0]**2 - 1 + 2*self.q[3]**2]])
    def S(self,v):
        return np.array([[    0, -v[2],  v[1]],
                         [ v[2],     0, -v[0]],
                         [-v[1],  v[0],    0]])