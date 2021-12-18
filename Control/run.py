import numpy as np
from vehicle_objs.state import State
from vehicle_objs.actuators.thruster import Thruster
from vehicle_objs.actuators.actuator import Actuator
from simulation import Simulation
from vehicle import Vehicle
from enviornment import Enviornment
from eom import EOM

## CREATE SIMULATION PARAMETERS
dt = 0.01
t0 = 0
tf = 10

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
mdot = 0
Idot = np.array([[0,0,0],[0,0,0],[0,0,0]])
F = np.array([0,0,0])
M = np.array([0,0,0])
cg = np.array([0,0,0])
#Sensors
#Actuators
main_engine = Thruster(300, 10, 0.40, np.array([1,0,0]), True, np.array([0,0,0]))
test_actuator = Actuator(True, np.array([0.0,0.0,0.0]), np.array([100,0.0,0.0]))
actuators = {
    "main_engine": main_engine,
    "test_actuator": test_actuator
}
EEV = Vehicle(m,I,cg,mdot,Idot,F,M,EEV_state,actuators)

## CREATE ENVIORNMENT
disturbance_F = np.array([0,0,0])
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


