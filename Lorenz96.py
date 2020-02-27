
import numpy as np

def Deriv96(x,t, F):
    up = np.append(x[1:],x[:1])
    down2 = np.append(x[-2:],x[:-2])
    down1 = np.append(x[-1:],x[:-1])
    return (up - down2)*down1 - x + F
