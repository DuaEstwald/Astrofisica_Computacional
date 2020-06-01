# Para convertir imagenes jpg en fits y viceversa

import numpy as np
from PIL import Image
from astropy.io import fits
import img_scale

def jpg_to_fits(filename):
    image = Image.open(filename)
    xsize,ysize = image.size
    r,g,b = image.split()
    
    r_data = np.array(r.getdata())
    r_data = r_data.reshape(ysize,xsize)
#    red = fits.PrimaryHDU(data=r_data)
#    red.header['LATOBS'] = "32:11:56"
#    red.header['LONGOBS'] = "110:56"
#    red.writeto(str(filename[:-4])+'_red.fits')

    g_data = np.array(g.getdata())
    g_data = g_data.reshape(ysize,xsize)
#    green = fits.PrimaryHDU(data=g_data)
#    green.header['LATOBS'] = "32:11:56"
#    green.header['LONGOBS'] = "110:56"
#    green.writeto(str(filename[:-4])+'_green.fits')

    b_data = np.array(b.getdata())
    b_data = b_data.reshape(ysize,xsize)
#    blue = fits.PrimaryHDU(data=b_data)
#    blue.header['LATOBS'] = "32:11:56"
#    blue.header['LONGOBS'] = "110:56"
#    blue.writeto(str(filename[:-4])+'_blue.fits')
    return r_data,g_data,b_data

def fits_to_jpg(rfile,gfile,bfile,name):
    r = fits.getdata(rfile)
    b = fits.getdata(bfile)
    g = fits.getdata(gfile)
    img = np.zeros((r.shape[0],r.shape[1],3),dtype=float)

    img[:,:,0] = img_scale.sqrt(r,scale_min=r.min(),scale_max=r.max()+50)
    img[:,:,1] = img_scale.sqrt(g,scale_min=g.min(),scale_max=g.max()+50)
    img[:,:,2] = img_scale.sqrt(b,scale_min=b.min(),scale_max=b.max()+50)

    import matplotlib.pyplot as plt
    plt.imshow(img,aspect='equal')
    plt.savefig(str(name)+'.jpg')
