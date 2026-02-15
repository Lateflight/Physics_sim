import numpy as np
import forces as Forces
from target import Rocket
#import forces

def set_dt(dt):
    delt = dt
    return dt

def step(obj,callables,dt):
    
    F=Forces.assemble_forces(obj,callables)
    if np.isnan(F).any():
        print("EXITCODE: FORCE UNDEFINED")
        return 2
    
    A=F/obj.mass
    
    acc=apply_translation(obj,A,dt)
    print(acc)
    return acc


def apply_translation(obj,A,dt):

    state = obj.X    
    state[3:6]+=A*dt
    state[0:3]+=state[3:6]*dt
    print(obj,"STATE: ", state[0:3])
    if obj.X[2]<0 and isinstance(obj,Rocket):
        return 1
    
    return 0
