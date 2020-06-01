# Vamos a realizar otro intento para realizar la astrofisica computacional

import numpy as np



# realizamos la fuente de la lente, siendo esta 


# ============================ FUENTES ================================


# FUENTE CIRCULAR GAUSIANA
def gcirc(n_y,rad,x1=0.,y1=0.):
    x,y = np.mgrid[0:n_y,0:n_y] # Esto crea el plano de la fuente
    r2 = (x-x1-n_y/2.)**2.+(y-y1-n_y/2.)**2.
    a = np.exp(-r2*0.5/rad**2.)
    return a/a.sum()

# FUENTE COMO IMAGEN

from astropy.io.fits import getdata
from convert import *

def fitsim(filename,jpg):
    if jpg == True:
        r,g,b = jpg_to_fits(filename)
        for a in (r,g,b):
            if len(a.shape)>2:
                a = a[0]
                a = a*1.0/a.sum() 
        return r,g,b # devuelve la imagen normalizada

    if jpg == False:
        a = getdata(filename)
        if len(a.shape)>2:
            a = a[0]
        return a*1.0/a.sum()
