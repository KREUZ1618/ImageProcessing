# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:12:14 2020

@author: DELL
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from Bordesi import Bordesi as Bi
from Bordesj import Bordesj as Bj
from Histograma import Histograma as H
im=Image.open("C:/Users/DELL/Pictures/PI/Examen/A4.jpg")
v=im.size[1]   #Dimensión uno
t=im.size[0]   #Dimensión dos
w=3

im=np.array(im)
plt.imshow(im)
plt.axis('off')
plt.show()

H(im,0,w,v,t)

im1=np.zeros(shape=(v,t,w))
b=0 #Tipo de borde
r=11 #Tamaño de la máscara
msc2=np.zeros(shape=(r,r))
for u in range(0,w):
    for i in range(0,v):
        for j in range(0,t):
            for m in range(int(-(r-1)/2),int((r-1)/2)+1):
                for n in range(int(-(r-1)/2),int((r-1)/2+1)):
                    idx_i=Bi(i+m,v,m,b)
                    idx_j=Bj(j+n,t,n,b)
                    msc2[m+int((r-1)/2)][n+int((r-1)/2)]=im[idx_i,idx_j,u]
            im1[i,j,u]=np.amax(msc2)

plt.imshow(im1.astype(np.uint8))
plt.axis('off')
plt.show()

H(im1,1,w,v,t)