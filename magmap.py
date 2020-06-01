# Codigo para generar un mapa de magnitudes

import numpy as np
import lens as l
import matplotlib.pyplot as plt

ny=401
yl=3.

b=np.zeros((ny,ny))
raypix=100.  # el numero de rayos por pixel en ausencia de lensing
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

for i in yr: # loop sobre todos los rayos
    if ((i*100/nx)>=perc): #chequeamos si tenemos completado el perc
        perc=perc+perc0
        print(round(i*100/nx),"%    ")

    x1=-xl+y*xs
    x2=-xl+x*xs
    y1,y2=l.ChangRefsdal(x1,x2,0.,0.,0.5,0.15,0.5)

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
plt.imshow(np.log10(b))


#ploteamos el centro con respecto a la distancia

plt.figure()
x = np.linspace(0.0,200.0,len(b[200]))
plt.plot(x,np.log10(b[200]))

plt.savefig('magfig.png')
