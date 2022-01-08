import numpy as np
from vehicle_objs.gnc.estimator import Estimator
from vehicle_objs.gnc.guidance import Guidance
#from vehicle_objs.gnc.controller import Controller
from vehicle_objs.gnc.controllers.controller_rcs_lp import Controller
from vehicle_objs.gnc.gnc import GNC

class Vehicle():
    def __init__(self,mass,inertia,cg,mdot,Idot,state,actuators,sensors,guidance,estimator):
        self.mass = mass
        self.inertia = inertia
        self.cg = cg
        self.mdot = mdot
        self.Idot = Idot
        #self.F = F
        #self.M = M
        #self.F_const = F
        #self.M_const = M
        self.state = state
        self.actuators = actuators
        self.sensors = sensors
        
        control = Controller(self)
        self.gnc = GNC(guidance,estimator,control)
        
    #def setForce(self,F):
    #    self.F = F
    #    self.F_const = F
    #def setMoment(self,M):
    #    self.M = M
    #    self.M_const = M
    def updateSensorMeasurements(self):
        for i in self.sensors:
            self.sensors[i].updateMeas(self.state)
    def getSensorMeasurements(self):
        measurements = {}
        for i in self.sensors:
            measurements[i] = self.sensors[i].getMeas()
        return measurements
    def update(self):
        ## Update Sensor Measurements
        self.updateSensorMeasurements()
        ## Update State Estimate, Guidance Command, and Actuator Commands.
        self.gnc.setActuatorCmds(self.getSensorMeasurements())
        ## Apply Actuator Commands
        for i in self.gnc.controller.ctrl_cmd:
            self.actuators[i].set(self.gnc.controller.ctrl_cmd[i])
        ## Update Forces/Moments
        self.F = np.array([0.0,0.0,0.0])
        self.M = np.array([0.0,0.0,0.0])
        for i in self.actuators:
            self.F += self.actuators[i].getForce()
            self.M += self.actuators[i].getMoment(self.cg)

        
        