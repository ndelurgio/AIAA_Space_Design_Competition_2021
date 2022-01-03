import numpy as np

class GNC():
    def __init__(self,guidance,estimator,controller):
        self.guidance = guidance
        self.estimator = estimator
        self.controller = controller
    def setActuatorCmds(self,measurements):
        self.estimator.updateStateEst(measurements)
        self.guidance.updateStateCmd(self.guidance.getStateCmd())
        self.controller.updateCtrlCmd(self.estimator,self.guidance)
        #return self.controller.