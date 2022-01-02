import numpy as np

class Controller():
    def __init__(self,vehicle):
        self.ctrl_cmd = {
            "main_engine": [False,1.0],
            "rcs_pz_px_mz": [False,1.0],
            "rcs_pz_px_my": [False,1.0],
            "rcs_pz_px_py": [False,1.0],
            
            "rcs_pz_mx_mz": [False,1.0],
            "rcs_pz_mx_my": [False,1.0],
            "rcs_pz_mx_py": [False,1.0],
            
            "rcs_pz_py_mz": [False,1.0],
            "rcs_pz_py_mx": [False,1.0],
            "rcs_pz_py_px": [False,1.0],
            
            "rcs_pz_my_mz": [False,1.0],
            "rcs_pz_my_mx": [False,1.0],
            "rcs_pz_my_px": [False,1.0],
            
            "rcs_mz_px_pz": [False,1.0],
            "rcs_mz_px_my": [False,1.0],
            "rcs_mz_px_py": [False,1.0],
            
            "rcs_mz_mx_pz": [False,1.0],
            "rcs_mz_mx_my": [False,1.0],
            "rcs_mz_mx_py": [False,1.0],
            
            "rcs_mz_py_pz": [False,1.0],
            "rcs_mz_py_mx": [False,1.0],
            "rcs_mz_py_px": [False,1.0],
            
            "rcs_mz_my_pz": [False,1.0],
            "rcs_mz_my_mx": [False,1.0],
            "rcs_mz_my_px": [False,1.0]
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
            #self.ctrl_cmd["main_engine"] = [True,1.0]
            self.ctrl_cmd["rcs_mz_px_pz"] = [True,1.0]
            self.ctrl_cmd["rcs_mz_mx_pz"] = [True,1.0]
            self.ctrl_cmd["rcs_mz_py_pz"] = [True,1.0]
            self.ctrl_cmd["rcs_mz_my_pz"] = [True,1.0]
        else:
            self.ctrl_cmd["rcs_mz_px_pz"] = [False,1.0]
            self.ctrl_cmd["rcs_mz_mx_pz"] = [False,1.0]
            self.ctrl_cmd["rcs_mz_py_pz"] = [False,1.0]
            self.ctrl_cmd["rcs_mz_my_pz"] = [False,1.0]
        #self.ctrl_cmd["main_engine"] = [False,1]