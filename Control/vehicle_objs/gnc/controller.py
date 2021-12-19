import numpy as np

class Controller():
    def __init__(self,vehicle):
        self.ctrl_cmd = {
            "main_engine": [False,1.0],
            "test_actuator": [False,np.array([0.0,0.0,0.0]),np.array([0.0,0.0,0.0])]
        }
        self.vehicle = vehicle
    def updateCtrlCmd(self,estimator,guidance):
        self.ctrl_cmd["main_engine"] = [True,1]