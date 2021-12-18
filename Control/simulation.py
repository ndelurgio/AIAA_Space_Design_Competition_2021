#from state import State
#from vehicle import Vehicle
#from enviornment import Enviornment
import numpy as np
import matplotlib.pyplot as plt
#from eom import EOM
class Simulation():
    def __init__(self,dt,t0,tf,vehicle,enviornment,eom):
        self.t = t0
        self.tf = tf
        self.dt = dt
        self.vehicle = vehicle
        self.enviornment = enviornment
        self.eom = eom
        
        #Create data collection arrays
        arr_length = int((tf-t0)/dt)
        self.t_history = np.empty(arr_length)
        self.q_history = np.empty((arr_length,4))
        self.w_history = np.empty((arr_length,3))
        self.x_history = np.empty((arr_length,3))
        self.v_history = np.empty((arr_length,3))
        self.e_history = np.empty((arr_length,3))
        
    def run(self):
        for i in range(self.t_history.size):
            self.t += self.dt                                                       # Begin new time step
            self.enviornment.update(self.vehicle.state,self.vehicle)                # Update Environmental Forces/Moments
            self.vehicle.update()                                                   # Update Vehicle Forces/Moments
            qdot, wdot, xdot, vdot = self.eom.solve(self.vehicle,self.enviornment)  # Compute state derivates
            self.vehicle.state.propagate(qdot,wdot,xdot,vdot,self.dt)               # Propogate vehicle state using state derivates
            ## Assign new state to the state history
            self.t_history[i] = self.t
            self.q_history[i] = self.vehicle.state.q
            self.w_history[i] = self.vehicle.state.w
            self.x_history[i] = self.vehicle.state.x
            self.v_history[i] = self.vehicle.state.v
            self.e_history[i] = self.vehicle.state.e
            #print(self.vehicle.state.w)
            
    def plot(self):
        
        ## Body Rates
        plt.figure(figsize=[8,5])
        plt.subplot(3,1,1)
        plt.title("Vehicle Body Rates (rad/s)")
        plt.plot(self.t_history,self.w_history[:,0],"r")
        plt.ylabel("\u03C9x")
        plt.xlim(left=self.t_history[0])
        plt.subplot(3,1,2)
        plt.plot(self.t_history,self.w_history[:,1],"g")
        plt.ylabel("\u03C9y")
        plt.xlim(left=self.t_history[0])
        plt.subplot(3,1,3)
        plt.plot(self.t_history,self.w_history[:,2],"b")
        plt.ylabel("\u03C9z")
        plt.xlim(left=self.t_history[0])
        plt.xlabel("Time (s)")
        
        ## Velocity
        plt.figure(figsize=[8,5])
        plt.subplot(3,1,1)
        plt.title("Vehicle Inertial Velocity (m/s)")
        plt.plot(self.t_history,self.v_history[:,0],"r")
        plt.ylabel("Vel X")
        plt.xlim(left=self.t_history[0])
        plt.subplot(3,1,2)
        plt.plot(self.t_history,self.v_history[:,1],"g")
        plt.ylabel("Vel Y")
        plt.xlim(left=self.t_history[0])
        plt.subplot(3,1,3)
        plt.plot(self.t_history,self.v_history[:,2],"b")
        plt.ylabel("Vel Z")
        plt.xlim(left=self.t_history[0])
        plt.xlabel("Time (s)")
        
        ## Position
        plt.figure(figsize=[8,5])
        plt.subplot(3,1,1)
        plt.title("Vehicle Inertial Position (m)")
        plt.plot(self.t_history,self.x_history[:,0],"r")
        plt.ylabel("Pos X")
        plt.xlim(left=self.t_history[0])
        plt.subplot(3,1,2)
        plt.plot(self.t_history,self.x_history[:,1],"g")
        plt.ylabel("Pos Y")
        plt.xlim(left=self.t_history[0])
        plt.subplot(3,1,3)
        plt.plot(self.t_history,self.x_history[:,2],"b")
        plt.ylabel("Pos Z")
        plt.xlim(left=self.t_history[0])
        plt.xlabel("Time (s)")
        
        ## Quaternion
        plt.figure(figsize=[8,5])
        plt.subplot(4,1,1)
        plt.title("Vehicle Inerital to Body Quaternion")
        plt.plot(self.t_history,self.q_history[:,0],"r")
        plt.ylabel("q0 (scalar)")
        plt.xlim(left=self.t_history[0])
        plt.subplot(4,1,2)
        plt.plot(self.t_history,self.q_history[:,1],"g")
        plt.ylabel("q1")
        plt.xlim(left=self.t_history[0])
        plt.subplot(4,1,3)
        plt.plot(self.t_history,self.q_history[:,2],"b")
        plt.ylabel("q2")
        plt.xlim(left=self.t_history[0])
        plt.subplot(4,1,4)
        plt.plot(self.t_history,self.q_history[:,3],"y")
        plt.ylabel("q3")
        plt.xlim(left=self.t_history[0])
        plt.xlabel("Time (s)")
        
        ## Euler Angles (3-2-1 Yaw-Pitch-Roll)
        plt.figure(figsize=[8,5])
        plt.subplot(3,1,1)
        plt.title("Vehicle Inertial to Body Euler Angles (deg)")
        plt.plot(self.t_history,self.e_history[:,2]*180/np.pi,"r")
        plt.ylabel("Roll")
        plt.xlim(left=self.t_history[0])
        plt.subplot(3,1,2)
        plt.plot(self.t_history,self.e_history[:,1]*180/np.pi,"g")
        plt.ylabel("Pitch")
        plt.xlim(left=self.t_history[0])
        plt.subplot(3,1,3)
        plt.plot(self.t_history,self.e_history[:,0]*180/np.pi,"b")
        plt.ylabel("Yaw")
        plt.xlim(left=self.t_history[0])
        plt.xlabel("Time (s)")
        
        plt.show()
        

        