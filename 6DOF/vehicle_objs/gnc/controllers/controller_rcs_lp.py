import numpy as np
import scipy.optimize as opt

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
        self.kp = 2 * np.pi / 180
        
        self.curr_linmomentum = np.array([0.0,0.0,0.0])
        self.curr_angmomentum = np.array([0.0,0.0,0.0])        
        ## Compute current time A matrix, which is used to store forces/torques of the RCS configuration
        F = 580.0 #580.080015
        r = 4.0
        l = 8.0
        R = F * r
        L = F * l / 2
        self.A = np.array([[0,0,0,0,0,0,0,-F,F,0,-F,F,0,0,0,0,0,0,0,-F,F,0,-F,F],
                          [0,-F,F,0,-F,F,0,0,0,0,0,0,0,-F,F,0,-F,F,0,0,0,0,0,0],
                          [-F,0,0,-F,0,0,-F,0,0,-F,0,0,F,0,0,F,0,0,F,0,0,F,0,0],
                          [0,L,-L,0,L,-L,-R,0,0,R,0,0,0,-L,L,0,-L,L,R,0,0,-R,0,0],
                          [R,0,0,-R,0,0,0,-L,L,0,-L,L,-R,0,0,R,0,0,0,L,-L,0,L,-L],
                          [0,-R,R,0,R,-R,0,R,-R,0,-R,R,0,-R,R,0,R,-R,0,R,-R,0,-R,R]])
        self.c = np.ones(24)
        self.dt = np.zeros(24) # For storing thruster on time commands
        ## Vector to store thruster on time
        self.timer = 0.0
        self.cmd_on = False # Is a command being executed?
        self.hCmd_prev = np.zeros(3)
        self.pCmd_prev = np.zeros(3)
        self.angError_prev = 0.0
        self.ang_threshold = 2.5
        self.over = False
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
        self.curr_angmomentum = self.vehicle.inertia.dot(estimator.state_est.w)
        
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
        rateCmd = -self.kp * l #self.kp * angError * l
        ## Bang-Bang Controller for rateCmd -> ang. momentum command
        if self.cmd_on == False:
            if angError > self.ang_threshold * np.pi/180 and (self.over == False or angError > self.angError_prev):
                hCmd = self.vehicle.inertia.dot(rateCmd)
                self.over = True
                self.ang_threshold = 0.5
            elif angError > self.ang_threshold * np.pi/180 and self.over == True:
                hCmd = self.hCmd_prev
                pCmd = self.pCmd_prev
            else:
                hCmd = np.array([0.0,0.0,0.0])
                self.ang_threshold = 1
                self.over = False
            ## Temporary zero linear momentum command
            pCmd = np.array([0.0,0.0,0.0])
        else:
            hCmd = self.hCmd_prev
            pCmd = self.pCmd_prev
            
        ## Determine if a LP needs to be solved
        if self.cmd_on == False and (any(hCmd != self.hCmd_prev) or any(pCmd != self.pCmd_prev)):
            ## Compute Required change in momentum
            delta_h = hCmd - self.curr_angmomentum
            delta_p = pCmd - self.curr_linmomentum
            b = np.concatenate((delta_p,delta_h))
            ## Solve for dt via linear program
            res = opt.linprog(self.c,None,None,self.A,b,)
            self.dt = res.x
            self.cmd_on = True
            self.timer = 0.0
            
        if self.cmd_on == True and max(self.dt) > 0.01:
            self.timer += 0.01 # From Simulation Time step
            for indx, val in enumerate(self.ctrl_cmd):
                if val == "main_engine":
                    continue
                elif self.timer < self.dt[indx - 1]:
                    self.ctrl_cmd[val] = [True,1.0]
                else:
                    self.ctrl_cmd[val] = [False,1.0]
            if self.timer > max(self.dt):
                self.cmd_on = False
            
        ## Update previous hCmd and pCmd
        self.hCmd_prev = hCmd
        self.pCmd_prev = pCmd
        self.angError_prev = angError