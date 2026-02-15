import numpy as np


def getfrom_sensor(obj1,obj2):
    
    target=obj1.X
    missile = obj2.X

    difference = target[0:3] - missile[0:3]
    sigma = 1 # meters
    noise = np.random.normal(0, sigma, size=3)

    measured = difference 


    print(f"+-----------+\n    BEEP\ndifference: {measured}\ncheating! Noise: {noise}+-----------+\n\n\n")
    
    return measured

    



