import numpy as np
from vehicle_objs.sensors.sensor import Sensor


class Perfect(Sensor):
    def __init__(self,state):
        self.q_meas = state.q
        self.w_meas = state.w
        self.x_meas = state.x
        self.v_meas = state.v
        #self.e_meas = state.e
    def updateMeas(self,state):
        self.q_meas = state.q
        self.w_meas = state.w
        self.x_meas = state.x
        self.v_meas = state.v
    def getMeas(self):
        measurements = {
            "q_meas": self.q_meas,
            "w_meas": self.w_meas,
            "x_meas": self.x_meas,
            "v_meas": self.v_meas
        }
        return measurements