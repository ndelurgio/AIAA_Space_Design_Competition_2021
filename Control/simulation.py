from state import State
from vehicle import Vehicle
from enviornment import Enviornment
import numpy as np
#from eom import EOM
class Simulation():
    def __init__(self,dt,t0,tf,vehicle,enviornment,eom):
        self.t = t0
        self.tf = tf
        self.dt = dt
        self.vehicle = vehicle
        self.enviornment = enviornment
        self.eom = eom
        
        #Create data collection arrays
        #self.state_history = np.empty((tf-t0) / dt, dtype=State)
    def run(self):
        while self.t <= self.tf:
            self.enviornment.update(self.vehicle.state,self.vehicle)
            self.vehicle.update()
            qdot, wdot, xdot, vdot = self.eom.solve(self.vehicle,self.enviornment)
            self.vehicle.state.propagate(qdot,wdot,xdot,vdot,self.dt)
            print(self.vehicle.state.w)
            self.t += self.dt
        