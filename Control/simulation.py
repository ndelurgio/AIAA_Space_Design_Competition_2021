from state import State
from vehicle import Vehicle
from enviornment import Enviornment
#from eom import EOM
class Simulation():
    def __init__(self,dt,t0,tf,vehicle,enviornment,eom):
        self.t = t0
        self.tf = tf
        self.dt = dt
        #self.state = state
        self.vehicle = vehicle
        self.enviornment = enviornment
        self.eom = eom
    def run(self):
        while self.t <= self.tf:
            self.enviornment.update(self.vehicle.state)
            self.vehicle.update()
            self.eom.solve(self.vehicle,self.enviornment,self.state)
            self.t += self.dt
        