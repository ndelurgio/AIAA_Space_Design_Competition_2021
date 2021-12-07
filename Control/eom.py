import numpy as np
from state import State
from vehicle import Vehicle
from enviornment import Enviornment
class EOM():
    def solve(self,vehicle,enviornment):
        F = vehicle.F + enviornment.F
        M = vehicle.M + enviornment.M
        xdot = vehicle.state.v #Earth Frame
        vdot = F / vehicle.mass #Earth Frame
        qdot = 0.5*self.omega(vehicle.state.w)*vehicle.state.q
        wdot = np.linalg.inv(vehicle.inertia)*(M - np.cross(vehicle.state.w,(vehicle.inertia*vehicle.state.w)) - vehicle.Idot*vehicle.state.w) # Check
        ## Next step: write function that rotates a vector using quaternion. Need to rotate vehicle.F.
        
    def omega(w):
        omega = np.matrix([[0   , -w[0],  -w[1], -w[2]], 
                           [w[0],     0,   w[2], -w[1]],
                           [w[1],  -w[2],     0,  w[0]],
                           [w[2],   w[1], -w[0],    0]])
        return omega
        