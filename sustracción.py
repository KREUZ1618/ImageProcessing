# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 00:26:54 2020

@author: win10
"""

import numpy as np
from PIL import Image, ImageFont, ImageDraw
import math 

import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
from scipy import misc

im = Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg") 
im1 = Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg")# read the image, provide the
im2 = Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\A2.jpg")

print(im.width,im.height)
ancho=im.width
alto=im.height
im=np.array(im)
im2=im2.resize((ancho,alto))

im2=np.array(im2)
print(im.ndim)
print(len(im))
print(im.shape)



for i in range(0,3):
    for j in range(0,alto):
        for k in range(0,ancho):
            u =int(round(abs((int(im[j,k,i])-int(im2[j,k,i])))))
            if(u>255):
                print("ERROR!!!")
                i=3
                j=alto
                k=ancho
            im[j,k,i]=u
            u=0
            
            
im = Image.fromarray(im)      

im1 = im.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\resta.jpg")
 

plt.imshow(im)
plt.axis('off')
plt.show()