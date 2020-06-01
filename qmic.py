# COGIDO PARA GENERAR MICROLENSING


import numpy as np
from math import pi
import matplotlib.pyplot as plt
from random import seed, uniform
from time import time, clock, sleep
from pyfits import writeto

startt = time()

# ******************* Model Parameters ************************

kappa = 0.59  # Total convergence
gamma = 0.61  # Shear
alpha = 0.999  # Fraction of mass in form of microlenses
raypix = 15.0  # Rays per pixels in absence of lensing
ny = 1000  #  Pixels in the magnification map
yl = 10  # Half size of magnification map in Einstein Radii
eps = 0.02  # Maximum fraction of flux lost

# ********* Make some preliminary calculations *****************

ks = kappa*alpha  # Convergence in microlenses
kc = kappa*(1.-alpha)  # Convergence in smooth matter
ys = 2.*yl/(ny-1)  # Pix size in the image plane
ooys = 1./ys  # Inverse of pixel size on image plane
sqrpix = np.sqrt(raypix) # Rays per pixel in one dimension
f1 = 1./abs(1.-kappa-gamma)  # Exp. factor on horizontal axis
f2 = 1./abs(1.-kappa+gamma)  # Exp. factor on vertical axis
fmax = max(f1,f2)  # Max Exp factor
xl1, xl2 = 1.5*yl*f1, 1.5*yl*f2 # Half size of shooting region in x and y
xl = 1.5*yl*fmax # Longest half side of shooting region
nsmin = 3*ks**2/eps/abs((1.-kappa)**2-gamma**2) # Min number of stars
xmin = np.sqrt(pi*nsmin/ks)/2 # Min half side of star region
xls = xl+xmin # Expand o account for shooting region
nx1 = np.int16(np.round(1.5*ny*f1*sqrpix)) # Rays in shoot, reg. along x axis
nx2 = np.int16(np.round(1.5*ny*f2*sqrpix)) # Rays in shoot. reg. along y axis
nx = max(nx1,nx2) # Number of rays along longest side
xs = 2.*xl1/(nx1-1) # Pixel side on image plane
xnl = abs(ks*(2*xls)*(2*xls)/pi)  # Number of microlenses
nl = int(xnl) # Number of microlentes (int)
thmag = 1./(1-kappa-gamma)/(1-kappa+gamma) # Theorerical value of magnification


print("******************************************************")
print("Half Size of map in Einstein radii       =",yl)
print("Number of pixels of magnification map    =",ny)
print("Half size of shooting region             =",xl)
print("Number of rays along the longest axis    =",nx)
print("Half size of region with microlenses     =",xls)
print("Total Converge,                        k =",kappa)
print("Shear,                             gamma =",gamma)
print("Fraction of mass in microlenses,   alpha =",alpha)
print("Convergence in from of microlenses,   ks =",ks)
print("Number of microlenses                    =",nl)
print("Rays per unlensed pixel,          raypix =",raypix)
print("Theoretical Mean Magnification,       mu =",thmag)
print("******************************************************")

b = np.zeros((ny,ny)) # Initialize magnification map

# ********* Randomly distribute stars in region ************

x1l = np.zeros(nl) # Initialize microlens positions to zero
x2l = np.zeros(nl)
seed(1.0)   # Initialize random number generator

for i in range(nl): # Generate position to microlenses
    x1l[i] = uniform(-xls,xls)
    x2l[i] = uniform(-xls,xls)
    
# ***********************************************************

perc0 = 0.5  # Percentage step to show progress
perc = 5.  # Initial percentage
yr = np.arange(0,nx2)  # Array for looping over rows of rays
y,x = np.mgrid[0.0:1.0,0:nx1]  # These are arrays with x and y coords of one row of rays in image plane

nlrange = np.arange(nl)  # Array for looping over lenses

# *********************** MAIN LOOP *************************

for i in yr:  # Main loop over rows of rays
    if ((i*100/nx2)>=perc): # If perc is completed, then show progress
        perc = perc+perc0
        print(round(i*100/nx2),"%        ", round(time()-startt,3), "  secs")
        # print completed fraction and elapsed execution time
    x2 = -xl2+y*xs # Convert pixels to coordinates in the image plane
    x1 = -xl1+x*xs 
    y2 = x*0.0  # Initialize variables
    y1 = x*0.0
    for ii in nlrange:  # Loop over microlenses
        x1ml = x1-x1l[ii]
        x2ml = x2-x2l[ii]
        d = x1ml**2+x2ml**2  # Distance to lens ii squared
        y1 = y1+x1ml/d  # Deflect x coordinate due to lens ii
        y2 = y2+x2ml/d  # Deflect y coordinate due to lens ii 
        del x1ml,x2ml,d
    y2 = x2-y2-(kc-gamma)*x2  # Calculate total y deflection
    y1 = x1-y1-(kc+gamma)*x1  # Calculate total x deflection
    i1 = (y1+yl)*ooys  # Convert coordinates to pixels on source plane
    i2 = (y2+yl)*ooys
    i1 = i1.astype(int)  # Maks indices integer
    i2 = i2.astype(int)
    ind = (i1>=0)&(i1<ny)&(i2>=0)&(i2<ny) # Select indices of rays falling onto our source plane

    i1n = i1[ind] # Array of x coordinates of rays within map
    i2n = i2[ind] # Array of y coordinates of rays within map
    for ii in range(np.size(i1n)): # Loop over rays hitting the source plane
        b[i2n[ii],i1n[ii]]+=1  # Increase map in one unit if ray hit 
    y =y+1.0  # Move on to next row rays

# **********************************************************

b = b/raypix # Normalize by rays per unlensed pixel

print("**********************************************************")
print("Measured mean magnification        =",np.mean(b))
print("Theoretical magnification is       =",thmag)
print("**********************************************************")

if thmag<0:  # Vertical or horizontal flip in some cases
    if gamma<0: 
        b = np.flipud(b)
    else:
        b = np.fliplr(b)

# ******************** Display result **********************

ax = plt.subplot(121)  # left plot
plt.plot(x1l,x2l,'+') # plot positions of stars
rayboxx = [-xl1,-xl1,xl1,xl1,-xl1] 
rayboxy = [-xl2,xl2,xl2,-xl2,-xl2]
plt.plot(rayboxx,rayboxy) # show shooting regions
mapboxx = np.array([-yl,-yl,yl,yl,-yl])
mapboxy = np.array([-yl,yl,yl,-yl,-yl])
plt.plot(mapboxx*f1,mapboxy*f2,'r') # show region mapped onto map
plt.xlim(-1.1*xls,1.1*xls)
plt.ylim(-1.1*xls,1.1*xls)
ax.set_aspect('equal') # keep aspect ratio
plt.subplot(122) # Right plot
implot = plt.imshow(b,origin='lower') # Display magnification map

# **********************************************************
print("Exec. time = ",round(time()-startt,3),'seconds') # Print execution time
plt.show()

# ***************** Save result as fits file? **************
save = ''
while (save not in ['y','n']): # Wait for input unless it is 'y' or 'n'
    save = raw_input("Save file (y/n)? ")
    if (save == 'y'):
        filename = ''
        filename = 'IMG/'+raw_input("Filename = ")+'.fits'
        writeto(filename,b) # Write fits file



    
