#main

from target import Rocket
import physics as phy
import quick_grapher as gph
import sys
from missile import Missile

def main():
    

    aero = (0.001,.99)
    bare_minimum_forces={'drag': aero,
        'lift': aero,
         'gravity': ()}
    
    state_vector =   [-300,200,1,100,200,2000,0,0,0,0,0,0] #3 positionals, 3 velocity,3 angles, 3 angular
    #theta is pitch, phi is yaw
    m_state_vector = [0,0,10,0,0,10,0,0,0,0,0,0]
    
    
    
    target_rocket = Rocket(state_vector,mass=1,permitted_forces=bare_minimum_forces.copy())
    
    missile = Missile(m_state_vector,mass=2,permitted_forces=bare_minimum_forces.copy(),thrust=40)
    
    bundle=[]
    time_values = []
    objects = [target_rocket,missile]

    for i in range(len(objects)):

        bundle.append([])

    def sim_loop():
            
        t=0
        dt = phy.set_dt(0.01)

        while True:

            exit_flag = False

            for index, obj in enumerate(objects):
                
                if isinstance(obj,Missile):
                    M=missile.measure(target_rocket)
                    missile.simple_thrust(M,kp=0.1,kd=0.1,dt=0.01)
                result = phy.step(obj, obj.call,dt)
                print(result)
            
                
                if result == 1:
                    exit_flag = True
                    print("Triggered")
                if result == 2:
                    errorexit = int(input("Error deteced: 0 to exit to graph, 1 to exit program:\n>>>"))
                    if errorexit==0:
                        exit_flag = True
                    else:
                        sys.exit()

                

            for index, obj in enumerate(objects):
                bundle[index].append(obj.return_values())

            t += dt
            time_values.append(t)
            
            if exit_flag:
                print("Got here")
                return
            

    sim_loop()
    gph.graph(bundle,time_values)    

    
    
    

        








if __name__=="__main__":

    main()


