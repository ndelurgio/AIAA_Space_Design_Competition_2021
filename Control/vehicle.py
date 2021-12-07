import numpy as np
class Vehicle():
    def __init__(self,mass,inertia,mdot,Idot,F,M,state):
        self.mass = mass
        self.inertia = inertia
        self.mdot = mdot
        self.Idot = Idot
        self.F = F
        self.M = M
        self.state = state
    #def __init__(self,mass,inertia):
    #    self.mass = mass
    #    self.inertia = inertia
    #    self.mdot = 0
    #    self.Idot = 0
    #    self.F = 0
    #    self.M = 0
        
    def setForce(self,F):
        self.F = F
    def setMoment(self,M):
        self.M = M
    def update(self):
        self.F += 0
        self.M += 0
        