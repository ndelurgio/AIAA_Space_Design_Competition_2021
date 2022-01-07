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
        self.kp = 10
        
        self.curr_linmomentum = np.array([0.0,0.0,0.0])
        self.curr_angmomentum = np.array([0.0,0.0,0.0])
        
        self.A = np.zeros((6,24)) # For LP
    def q_matrix(self,q):
        qmat = np.array([[q[0],-q[1],-q[2],-q[3]],
                         [q[1], q[0], q[3],-q[2]],
                         [q[2],-q[3], q[0], q[1]],
                         [q[3], q[2],-q[1], q[0]]])
        return qmat
    def q_mult(self,r,s):
        t = self.q_matrix(r).dot(s)
        return t
    def posError(self,estimator,guidance):
        return guidance.state_cmd.x - estimator.state_est.x
    def velError(self,estimator,guidance):
        return guidance.state_cmd.v - estimator.state_est.v
    def qError(self,estimator,guidance):
        q_error = self.q_mult(guidance.state_cmd.q,estimator.state_est.q)
        #q_error = guidance.state_cmd.q - estimator.state_est.q
        #q_error = q_error / np.linalg.norm(q_error)
        return q_error
    def angError(self,estimator,guidance):
        q_error = self.qError(estimator,guidance)
        theta_error = 2 * np.arccos(q_error[0]) #Rad
        if abs(theta_error) < 10**-8:
            return theta_error, np.array([0.0,0.0,0.0]) 
        l = q_error[1:4] / np.sin(theta_error / 2)
        l = l / np.linalg.norm(l)
        return theta_error, l
    def rateError(self,estimator,guidance):
        return guidance.state_cmd.w - estimator.state_est.w
    def updateMomentum(self,estimator):
        self.curr_linmomentum = self.vehicle.mass * estimator.state_est.v
        self.curr_angmomentum = self.vehicle.inertia * estimator.state_est.w
        
    def updateCtrlCmd(self,estimator,guidance):
        ## Compute new position and angular error
        posError = self.posError(estimator,guidance)
        velError = self.velError(estimator,guidance)
        angError, l = self.angError(estimator,guidance)
        qError = self.qError(estimator,guidance)
        rateError = self.rateError(estimator,guidance)
        ## Update Momentum State
        self.updateMomentum(estimator)
        
        ## Principal Angle Proportional Rate Controller
        rateCmd = self.kp * angError * l
        ## Bang-Bang Controller for rateCmd -> ang. momentum command
        if angError < 1 * np.pi/180:
            hCmd = self.vehicle.inertia.dot(rateCmd)
        else:
            hCmd = np.array([0.0,0.0,0.0])
        ## Temporary zero linear momentum command
        pCmd = np.array([0.0,0.0,0.0])
        
        ## Compute Required change in momentum
        delta_h = hCmd - self.curr_angmomentum
        delta_p = pCmd - self.curr_linmomentum
        
        ## Compute current time A matrix, which is used to store forces/torques of the RCS configuration
        F = 580.0 #580.080015
        r = 4.0
        l = 8.0
        R = F * r
        L = F * l / 2
        self.A = np.array([0,0,0,0,0,0,0,-F,F,0,-F,F,0,0,0,0,0,0,0,-F,F,0,-F,F],
                          [0,-F,F,0,-F,F,0,0,0,0,0,0,0,-F,F,0,-F,F,0,0,0,0,0,0],
                          [-F,0,0,-F,0,0,-F,0,0,-F,0,0,F,0,0,F,0,0,F,0,0,F,0,0],
                          [0,L,-L,0,L,-L,-R,0,0,R,0,0,0,-L,L,0,-L,L,R,0,0,-R,0,0],
                          [R,0,0,-R,0,0,0,-L,L,0,-L,L,-R,0,0,R,0,0,0,L,-L,0,L,-L],
                          [0,-R,R,0,R,-R,0,R,-R,0,-R,R,0,-R,R,0,R,-R,0,R,-R,0,-R,R])
        if abs(angError) > 1 * np.pi/180:
            #self.ctrl_cmd["main_engine"] = [True,1.0]
            self.ctrl_cmd["rcs_pz_px_py"] = [True,1.0]
            self.ctrl_cmd["rcs_pz_mx_py"] = [True,1.0]
            self.ctrl_cmd["rcs_mz_px_my"] = [True,1.0]
            self.ctrl_cmd["rcs_mz_mx_my"] = [True,1.0]
        else:
            self.ctrl_cmd["rcs_pz_px_py"] = [False,1.0]
            self.ctrl_cmd["rcs_pz_mx_py"] = [False,1.0]
            self.ctrl_cmd["rcs_mz_px_my"] = [False,1.0]
            self.ctrl_cmd["rcs_mz_mx_my"] = [False,1.0]
        #self.ctrl_cmd["main_engine"] = [False,1]