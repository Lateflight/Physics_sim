import numpy as np
import sensor

class Missile:
    missile_list=[]
    def __init__(self,x,mass=1, moment = 1, thrust=100,permitted_forces={}):
        
        self.X = np.array(x,dtype=float) #x,y,z,vx,vy,vz...
        self.mass = mass
        self.thrust = thrust
        self.call=permitted_forces
        self.call['thrust'] = ()
        self.old = 0
        self.old_d = 0

        Missile.missile_list.append(self)
    def return_values(self):
        
        return (self.X.copy())

    def measure(self,target):
        measurement = sensor.getfrom_sensor(target,self)
        return measurement
    
    def simple_thrust(self,signal,kp,kd,dt=0.01):
        signal = (signal+self.old)/2
        thrust_signal = signal*kp+(kd*(signal-self.old)/dt)
        print(thrust_signal)
        if thrust_signal.all() < 0:

            thrust_signal=0
            
        elif thrust_signal.all() > 1:

            thrust_signal = 1
        
        ret = self.thrust*thrust_signal
        self.call['thrust']=tuple([ret])
        self.old = signal
        self.old_d = (signal-self.old)/dt



