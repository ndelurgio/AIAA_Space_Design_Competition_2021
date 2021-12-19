import numpy as np
from vehicle_objs.actuators.actuator import Actuator

class Thruster(Actuator):
    def __init__(self,isp,mdot_max,throttle_min,thrust_vector,isOn,pos):
        self.isp = isp
        self.mdot_max = mdot_max
        self.g0 = 9.81
        self.thrust_vector = thrust_vector/np.linalg.norm(thrust_vector)
        self.throttle_min = throttle_min
        self.throttle = 1
        self.isOn = isOn
        self.pos = pos
    def set(self,cmd):
        self.isOn = cmd[0]
        throttle = cmd[1]
        if(throttle > 1.0 or throttle < self.throttle_min):
            print("Error setting throttle: outside bounds")
        else:
            self.throttle = throttle
    def getForce(self):
        if self.isOn:
            thrust = (self.mdot_max*self.throttle) * (self.isp*self.g0) * self.thrust_vector
            #print(thrust)
            return thrust
        else:
            return np.array([0.0,0.0,0.0])
    def getMoment(self):
        thrust = self.getForce()
        moment = np.cross(self.pos,thrust)
        return moment
            