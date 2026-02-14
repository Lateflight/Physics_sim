import numpy as np

class InvalidInputError(Exception):

    pass



def Force_help():
        
        while True:
            try:
                print("---FORCES HELP---")

                help_index = input("Forces (prints out all forces)\nForce [force_name] [force_args] (prints out all force args)\n>>")
            
                if help_index.lower() == "q":

                    break

                elif help_index == "Forces":
                    print("Gravity (default on)\nAerodynamic Force:\n\t[|]Drag\n\t[|]Lift\n")

                else:
                    raise InvalidInputError
                
            except Exception as e:
                print(e)
                print(f"Error: {e}\n\n")












def assemble_forces(obj, callable):
    
    """
    Docstring for assemble_forces
    
    :param callable: HAS TO HAVE THE FOLLOWING STRUCTURE ((func1,arg1),(func2,obj2)...)
        EXAMPLE: ((gravity,arg1))
        args are a tuple
    :to see list of available forces, Force_help()
    """
    
    
        

    def gravity(obj):

        return np.array([0,0,-obj.mass*9.81])

    def lift(obj,k,coeff):
        F=np.zeros(3)
        V=obj.X[3:6]
        
        V=np.array(V,dtype=float)
        
        vel=(V@V)**(1/2)
        
        if vel!=0:
            v_vec=V/vel
            up = [0,0,1]
            v_interim = np.cross(v_vec,up)
            interim_norm = np.linalg.norm(v_interim)
            if interim_norm < 1e-8:
                
                L_hat= -v_vec
                L = (k*coeff*vel**2)*L_hat
                F+=L
            else:
                L_hat = np.cross(v_interim,v_vec)
                L = (k*coeff*vel**2)*L_hat
                F+=L
        
        return F


    def drag(obj,k,coeff):
        
        F=np.zeros(3)

        V=obj.X[3:6]
        
        V=np.array(V,dtype=float)
        
        vel=(V@V)**(1/2)
        
        if vel!=0:
        
            dirh=-V/vel
            D=k*vel**2
            D_dir=dirh*D
            F+=D_dir

        return F
    #returns drag force as k, which represents the 1/2 p r Cd A part
    
    ret = np.zeros(3)

    func_dict = {'drag': drag, 'lift': lift, 'gravity': gravity}

    for to_call in callable.keys():
        args = callable[to_call]
        ret+=func_dict[to_call](*(obj,*args))
    
    return ret

