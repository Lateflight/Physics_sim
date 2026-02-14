import numpy as np
import forces as Forces
import time
#import forces
delt = 0.01

class ZeroException(Exception):
    
    pass

def set_dt(dt = delt):
    global delt
    delt = dt
    return dt

def acceleration(obj,callables):
    
    F=Forces.assemble_forces(obj,callables)
    A=F/obj.mass
    if obj.X[2]<0:

        return 1
    
    
    acc=apply_translation(obj,A)


    return acc




def apply_translation(obj,A,dt=delt):

    args=A
    
    state = obj.X

    
    state[3:6]+=args*dt


    state[0:3]+=state[3:6]*dt
    

    if obj.X[2]<0:
        return 1

    return 0
