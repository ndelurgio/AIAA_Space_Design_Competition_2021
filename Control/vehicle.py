import numpy as np
class Vehicle():
    def __init__(self,mass,inertia,cg,mdot,Idot,F,M,state,actuators):
        self.mass = mass
        self.inertia = inertia
        self.cg = cg
        self.mdot = mdot
        self.Idot = Idot
        self.F = F
        self.M = M
        self.state = state
        self.actuators = actuators
        
    def setForce(self,F):
        self.F = F
    def setMoment(self,M):
        self.M = M
    def update(self):
        self.F = np.array([0.0,0.0,0.0])
        self.M = np.array([0.0,0.0,0.0])
        for i in self.actuators:
            self.F += self.actuators[i].getForce()
            self.M += self.actuators[i].getMoment()
        
        