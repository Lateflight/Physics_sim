#main

from target import Rocket
import physics as phy
import quick_grapher as gph
from missile import Missile

def main():
    

    state_vector =   [10,0,100,0,0,10,0,0,0,0,0,0] #3 positionals, 3 velocity,3 angles, 3 angular
    #theta is pitch, phi is yaw
    m_state_vector = [10,0,10,0,0,10,0,0,0,0,0,0]
    
    T=1
    M=1

    target_rocket = Rocket(state_vector,mass=1)
    missile = Missile(m_state_vector,mass=2)
    
    bundle=[]
    time_values = []
    objects = [target_rocket,missile]

    for i in range(len(objects)):

        bundle.append([])

    def sim_loop():
            
        t = 0
        dt = phy.set_dt()

        while True:

            exit_flag = False

            for index, obj in enumerate(objects):
                result = phy.acceleration(obj, True, True)
                if result == 1:
                    exit_flag = True

            
            for index, obj in enumerate(objects):
                bundle[index].append(obj.return_values())

            t += dt
            time_values.append(t)

            if exit_flag:
                return

    sim_loop()
    gph.graph(bundle,time_values)    

    
    
    

        








if __name__=="__main__":
    main()


