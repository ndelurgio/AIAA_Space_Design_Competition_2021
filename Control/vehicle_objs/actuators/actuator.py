import numpy as np

class Actuator():
    def __init__(self,isOn,F,M):
        self.isOn = isOn
        self.F = F
        self.M = M
    def toggle(self,isOn):
        self.isOn = isOn
    def getForce(self):
        return self.F
    def getMoment(self):
        return self.M
        