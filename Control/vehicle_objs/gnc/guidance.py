import numpy as np

class Guidance():
    def __init__(self,state_cmd):
        self.state_cmd = state_cmd
    def updateStateCmd(self,state_cmd):
        self.state_cmd = state_cmd
    def getStateCmd(self):
        return self.state_cmd