import numpy as np
from vehicle_objs.state import State
from vehicle_objs.actuators.thruster import Thruster
from vehicle_objs.actuators.actuator import Actuator
from vehicle_objs.sensors.perfect import Perfect
from vehicle_objs.gnc.estimator import Estimator
from vehicle_objs.gnc.guidance import Guidance
from vehicle_objs.gnc.controller import Controller
from simulation import Simulation
from vehicle import Vehicle
from enviornment import Enviornment
from eom import EOM

## CREATE SIMULATION PARAMETERS
dt = 0.01
t0 = 0
tf = 50

## INITIALIZE STATE
q0 = np.array([1,0,0,0])
w0 = np.array([0,0,0])
x0 = np.array([0,0,0])
v0 = np.array([0,0,0])
EEV_state = State(q0,w0,x0,v0)

## CREATE VEHICLE
m = 6000
r = 4
l = 8
I = np.array([[0.25*m*r**2 + 1/12*m*l**2,0,0],[0,0.25*m*r**2 + 1/12*m*l**2,0],[0,0,m*r**2]])
mdot = 0.0
Idot = np.array([[0,0,0],[0,0,0],[0,0,0]])
F = np.array([0.0,0.0,0.0])
M = np.array([0.0,0.0,0.0])
cg = np.array([0.0,0.0,0.0])
#Sensors
state = Perfect(EEV_state)
sensors = {
    "state": state
}
#Actuators
main_engine = Thruster(300, 10, 0.40, np.array([0.0,0.0,1.0]), True, np.array([0.0,0.0,-2.0]))
test_actuator = Actuator(True, np.array([0.0,0.0,0.0]), np.array([0.0,0.0,0.0]))
actuators = {
    "main_engine": main_engine,
    "test_actuator": test_actuator
}
#GNC
est = Estimator(EEV_state)
guidance = Guidance(State(q0,w0,x0,v0))
#control = Controller(actuators)
EEV = Vehicle(m,I,cg,mdot,Idot,EEV_state,actuators,sensors,guidance,est)


## CREATE ENVIORNMENT
disturbance_F = np.array([0,0,-100])
disturbance_M = np.array([0,0,0])
env = Enviornment(disturbance_F,disturbance_M)

## CREATE EQUATIONS OF MOTION
eqm = EOM()

sim = Simulation(dt,t0,tf,EEV,env,eqm)
sim.run()
sim.plot()


#print(sim.w_history)
## DEBUG: RUN SIMULATION
#t = t0
#while t < tf:
#    qdot = np.array([0,0,0,0])
#    wdot = np.array([0,0,0])
#    xdot = np.array([0,0,0])
#    vdot = np.array([0,0,0])
#    EEV.state.propagate(qdot,wdot,xdot,vdot,dt)
#    print(EEV.state.x)
#    t += dt


