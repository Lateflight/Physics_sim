import numpy as np


class Missile:
    missile_list=[]
    def __init__(self,x,mass=1):
        
        self.X = np.array(x,dtype=float) #x,y,z,vx,vy,vz...
        self.mass = mass
        Missile.missile_list.append(self)
    def return_values(self):
        
        return (self.X.copy())
