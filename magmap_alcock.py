# Codigo para generar un mapa de magnitudes

import numpy as np
import lens as l
import matplotlib.pyplot as plt

ny=401
yl=3.

b=np.zeros((ny,ny))
raypix=15.  # el numero de rayos por pixel en ausencia de lensing
sqrpix=np.sqrt(raypix) # Raiz cuadrada de rayos por pixel en una direccion
sqrinpix=np.sqrt(1./raypix) 

ys=2.*yl/(ny-1) # tamanio del pixel en el plano fuente
xs=ys/sqrpix # tamanio del cuadrado del area transportado de vuelta por un rayo
xl=5.*yl #tamanio de la region de shooting del plano imagen
nx=np.round(2*xl/xs)+1 # numeros de rayos de una columna/fila en el plano imagen
yr=np.arange(0,nx) # array con los pixeles en y en una direccion
y,x=np.mgrid[0.0:1.0,0:nx] #grid con coordenadas pixeles por linea de la imagen
perc0=5. # porcentaje de pasos por progreso
perc=5. # valor inicial por perc


# PARAMETROS CARACTERISTICOS PARA EL LMC-9 EN ALCOCK.PY

from alcock import microlensing

ml1,ml2,x1l1,x2l1,x1l2,x2l2,theta,u0 = microlensing('LMC9')

# Pasamos a tamanio en pixel
 

for i in yr: # loop sobre todos los rayos
    if ((i*100/nx)>=perc): #chequeamos si tenemos completado el perc
        perc=perc+perc0
        print(round(i*100/nx),"%    ")

    x1=-xl+y*xs
    x2=-xl+x*xs
    y1,y2=l.TwoPoints(x1,x2,x1l1,x2l1,x1l2,x2l2,ml1,ml2)

    i1=(y1+yl)/ys
    i2=(y2+yl)/ys
    i1=np.round(i1)
    i2=np.round(i2)

    ind = (i1>=0)&(i1<ny)&(i2>=0)&(i2<ny)

    i1n=i1[ind]
    i2n=i2[ind]

    for j in range(np.size(i1n)):
        b[int(i2n[j]),int(i1n[j])]+=1
    y=y+1.0
b=b/raypix
print(np.mean(b))
plt.close()
plt.ion()
fig = plt.figure()
fig.add_subplot(121)
plt.imshow(np.log10(b),extent = (-yl,yl,-yl,yl),aspect='auto')

# Recreamos la recta que aparece en el LMC9
xpx = np.arange(len(b))
x = -yl+xpx*ys

y0 = np.tan(theta)*x+u0 # EL U0 HAY QUE PASARLO A PIXELES PARA QUE SURGA EFECTO

y1 = x

plt.plot(x,y0,'b')
plt.plot(x,y1,'g')


ypx0 = np.round((y0+yl)/ys).astype(int)
ypx1 = np.round((y1+yl)/ys).astype(int)
# Por otro lado, medimos la luz del mapa de magnificacion

from aux import profile

z0 = profile(b,xpx[0],ypx0[0],xpx[-1],ypx0[-1],'nn')
z1 = profile(b,xpx[0],ypx1[0],xpx[-1],ypx1[-1],'nn')


fig.add_subplot(122)
plt.plot(xpx,z0,'b')
plt.plot(xpx,z1[int((z1.shape[0]-xpx.shape[0])/2):-int((z1.shape[0]-xpx.shape[0])/2):],'g')

plt.savefig('mapfig.png')
