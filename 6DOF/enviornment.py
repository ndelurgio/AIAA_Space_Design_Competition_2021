
class Enviornment():
    def __init__(self,F,M):
        self.F = F
        self.M = M
    def setForce(self,F):
        self.F = F
    def setMoment(self,M):
        self.M = M
    def update(self,state,vehicle):
        self.F += 0
        self.M += 0
        