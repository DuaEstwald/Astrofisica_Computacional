# Es la parte de las curvas de luz de magnificacion

import numpy as np
from math import sqrt

def profile(c,x0,y0,x1,y1,method='nn'): # Las coordenadas se dan en pixel
    num = int(round(sqrt((x1-x0)**2+(y1-y0)**2))) #Longitud del track en pixeles
    xp,yp = np.linspace(x0,x1,num),np.linspace(y0,y1,num) # x and y sendo las coordenadas del track
    zp = c[yp.astype(np.int),xp.astype(np.int)]
    return zp[:-1]
