# Una vez creada la fuente, vamos a realizar la lente

import numpy as np
import matplotlib.pyplot as plt
import sys
from parameters import *

#print(ny) 
def lensing(name): 
    import lens as l
    import source as s
    import img_scale

    print(nx)
    print(n_y)
    print(xl)
    print(yl)

        
    if jpg == True:
        r,g,bb = s.fitsim(filename,jpg)
        ss = r,g,bb
        imgb = np.zeros((nx,nx,3),dtype=np.int32)
        imga = np.zeros((r.shape[0],r.shape[1],3),dtype=np.int32)
    else:
        ss = s.fitsim(filename,jpg)
        imgb = np.zeros((nx,nx,3),dtype=float)
        imga = np.zeros((ss.shape[0],ss.shape[1],3),dtype=float)
# ================================================

    index = 0
    for a in ss: #EL PROBLEMA ESTA AQUI, NO PODEMOS USAR UNA IMAGEN Y ESTO A LA VEZ
#    print(a)
        ny = a[0].size
# Creamos el plano imagen

# ================ FUENTE ======================
    # calculamos el tamanio fisico de los pixeles
        xs = 2.*xl/(nx-1.)  #El menos 1 es porque esta considerando los centros de los pixeles
        ys = 2.*yl/(ny-1.)

        b = np.zeros((nx,nx))
 
    # Convertimos los pixeles de la imagenes a coordenadas 
        for j1 in range(nx):
            for j2 in range(nx):
                x1 = -xl+j1*xs
                x2 = -xl+j2*xs
                p = param(name)
        # APLICAMOS LA TRANSFORMACION INVERSA
                if name == 'Point':
                    y1,y2 = l.Point(x1,x2,p[0],p[1],p[2])
                elif name == 'TwoPoints':
                    y1, y2 = l.TwoPoints(x1,x2,p[0],p[1],p[2],p[3],p[4],p[5])
                elif name == 'ChangRefsdal':
                    y1,y2 = l.ChangRefsdal(x1,x2,p[0],p[1],p[2],p[3],p[4]) 
                elif name == 'SIS':
                    y1,y2 = l.SIS(x1,x2,p[0],p[1],p[2])
                elif name == 'SISChangRefsdal':
                    y1,y2 = l.SISChangRefsdal(x1,x2,p[0],p[1],p[2],p[3],p[4])

        # CONVERTIMOS LAS COORDENADAS A PIXELES

                i1 = int(round((y1+yl)/ys))
                i2 = int(round((y2+yl)/ys))

        # Vamos a ponerle una condicion para que los pixeles queden dentro de la fuente. En caso contrario les damos un valor arbitrario. Si i1,i2 estan contenidos en el rango (1,n) hacemos asignacion IMAGEN=FUENTE, sino, hacemos IMAGEN=C donde C es una constante arbitraria como por ejemplo el fondo de cielo
                if ((i1>=0)&(i1<ny)&(i2>=0)&(i2<ny)):
                    b[j1,j2]=a[i1,i2]
                else:
                    C = 1. # Esta constante puede ser cualquiera
                    b[j1,j2]=C
        

        imgb[:,:,index] = b
        imga[:,:,index] = a
#        index +=1

#        imgb = img_scale.sqrt(b,scale_min=b.min(),scale_max=b.max()+50)
        #imga = img_scale.sqrt(a,scale_min=a.min(),scale_max=a.max()+50)
            
        index +=1

    return imga,imgb
        

#ltype = 'Point' # ESTO VIENE EN PARAMETERS
a,b = lensing(ltype)

# ========================================================


# Ya hemos terminado, ahora vamos a plotear las cosas

plt.close()
plt.ion()
fig = plt.figure()
plt.title(str(ltype)+' LENS')
plt.axis('off')
fig.add_subplot(121)
plt.imshow(a,extent=(-yl,yl,-yl,yl))
plt.title('Plano de la fuente')
fig.add_subplot(122)
plt.imshow(b,extent=(-xl,xl,-xl,xl))
plt.title('Plano imagen')

if sour == 'fitsim':
    if jpg == True:
        plt.savefig(filename[:-4]+'0.png')
    else:
        plt.savefig(filename[:-5]+'0.png')

else:
    plt.savefig('lensing.png')
