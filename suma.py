# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:53:25 2020

@author: win10
"""

import numpy as np
from PIL import Image, ImageFont, ImageDraw
import cv2
import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
from scipy import misc

im =cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg",0)
im1 =cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg",0)
im2 =cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg",0)

ancho,alto=im.shape 

im=np.array(im)
im2=im2.resize((ancho,alto))
im1=np.array(im1)
im2=np.array(im2)
print(im.ndim)
print(len(im))
print(im.shape)

print(im2.shape)



for i in range(0,3):
    for j in range(0,alto):
        for k in range(0,ancho):
            u =int (round((int(im[k])+int(im2[k]))/2))
            if(u>255):
                print("ERROR!!!")
                i=3
                j=alto
                k=ancho
            im[j,k,i]=u
            u=0
            
            
im = Image.fromarray(im)      

im1 = im.save("C:\\Users\win10\Desktop\procesamiento de imagenes\suma.jpg")
 

plt.imshow(im)
plt.axis('off')
plt.show()