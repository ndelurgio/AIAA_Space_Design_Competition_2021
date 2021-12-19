import numpy as np
#import vehicle_objs.state as State

class Estimator():
    def __init__(self,state):
        self.state_est = state
    def updateStateEst(self,measurements):
        state = measurements["state"]
        #print(state)
        self.state_est.setState(state["q_meas"], state["w_meas"], state["x_meas"], state["v_meas"])
        #self.state_est = State(state["q_meas"], state["w_meas"], state["x_meas"], state["v_meas"])