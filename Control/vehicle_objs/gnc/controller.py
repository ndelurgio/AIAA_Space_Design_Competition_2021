import numpy as np

class Controller():
    def __init__(self,vehicle):
        self.ctrl_cmd = {
            "main_engine": [False,1.0],
            "test_actuator": [False,np.array([0.0,0.0,0.0]),np.array([0.0,0.0,0.0])]
        }
        self.vehicle = vehicle
    
    def posError(self,estimator,guidance):
        return guidance.state_cmd.x - estimator.state_est.x
    def velError(self,estimator,guidance):
        return guidance.state_cmd.v - estimator.state_est.v
    def angError(self,estimator,guidance):
        q_error = guidance.state_cmd.q - estimator.state_est.q
        q_error = q_error / np.linalg.norm(q_error)
        return q_error
    def rateError(self,estimator,guidance):
        return guidance.state_cmd.w - estimator.state_est.w
    def updateCtrlCmd(self,estimator,guidance):
        posError = self.posError(estimator,guidance)
        posErrorZ = posError[2]
        #print(guidance.state_cmd.x)
        if abs(posErrorZ) > 5.0:
            self.ctrl_cmd["main_engine"] = [True,1.0]
        else:
            self.ctrl_cmd["main_engine"] = [False, 1.0]
        #self.ctrl_cmd["main_engine"] = [False,1]