import numpy as np
class State():
    def __init__(self, q0, w0, x0, v0): # q = [w v1 v2 v3]
        self.q = q0
        self.w = w0
        self.x = x0
        self.v = v0
    #def __init__(self): # q = [w v1 v2 v3]
    #    self.q = np.array([1,0,0,0])
    #    self.w = np.array([0,0,0])
    #    self.x = np.array([0,0,0])
    #    self.v = np.array([0,0,0])
    
    def propagate(self,qdot,wdot,xdot,vdot,dt):
        self.q = self.q + qdot*dt#0.5*dt*(self.q + (self.q + qdot*dt))
        self.q = self.q / np.linalg.norm(self.q)
        self.w = self.w + wdot*dt#0.5*dt*(self.w + (self.w + wdot*dt))
        self.x = self.x + xdot*dt#0.5*dt*(self.x + (self.x + xdot*dt))
        self.v = self.v + vdot*dt#0.5*dt*(self.v + (self.v + vdot*dt))
    