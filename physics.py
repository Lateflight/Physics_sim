import numpy as np
import time

def acceleration(obj,drag=False, k=0.1):
    # a super simplified forces model`
    g=-9.81
    A=np.array([0,0,-9.81],dtype=float)
    if drag==True:
        #returns drag force as k, which represents the 1/2 p r Cd A part
        V=obj.X[3:6]
        V=np.array(V,dtype=float)
        
        vel=(V@V)**(1/2)
        
        if vel!=0:
        
            dirh=-V/vel
            D=k*vel**2
            aD=(D/obj.mass)
            aD_dir=dirh*aD
            A+=aD_dir
    acc = apply_translation(obj,A)    
    return acc


def apply_translation(obj,A,dt=0.01):

    args=A

    for i in range(len(args)):
        #obj.X is a nmpy array
        obj.X[i+3]+=args[i]*dt
        obj.X[i]+=obj.X[i+3]*dt
        
    if obj.X[2]<0:
        return 1

    return 0
