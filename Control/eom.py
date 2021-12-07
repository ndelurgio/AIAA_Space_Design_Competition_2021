from state import State
from vehicle import Vehicle
from enviornment import Enviornment
class EOM():
    def solve(self,vehicle,enviornment,state):
        F = vehicle.F + enviornment.F
        M = vehicle.M + enviornment.M
        xdot = self.state.v
        vdot = F / vehicle.mass
        