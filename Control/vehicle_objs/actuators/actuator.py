import numpy as np

class Actuator():
    def __init__(self,isOn,F,M):
        self.isOn = isOn
        self.F = F
        self.M = M
    def set(self,cmd):
        self.isOn = cmd[0]
        self.F = cmd[1]
        self.M = cmd[2]
    #def toggle(self,isOn):
    #    self.isOn = isOn
    def getForce(self):
        return self.F
    def getMoment(self,cg):
        return self.M
        