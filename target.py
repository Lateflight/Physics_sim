#creates a simple, non evading target and updates it's position
import numpy as np

class Rocket:
    rocket_list=[]

    def __init__(self,x,mass=1):
        
        self.X = np.array(x,dtype=float) #x,y,z,vx,vy,vz...
        self.mass = mass
        Rocket.rocket_list.append(self)
    def return_values(self):
        
        return (self.X.copy())
