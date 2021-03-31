# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:19:46 2020

@author: DELL
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from Bordesx import Bordesx as Bx
from Bordesy import Bordesy as By

im=Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\V6.jpg")
v=im.size[1]   #Dimensión uno
t=im.size[0]   #Dimensión dos
w=3

im=np.array(im)


im1=np.zeros(shape=(v,t,w))

b=0 #Tipo de borde
r=11 #Tamaño de la máscara
msc2=np.zeros(shape=(r,r))

for u in range(0,w):
    for i in range(0,v):
        for j in range(0,t):
            for m in range(int(-(r-1)/2),int((r-1)/2)+1):
                for n in range(int(-(r-1)/2),int((r-1)/2+1)):
                    idx_i=Bx(i+m,v,m,b)
                    idx_j=By(j+n,t,n,b)
                    msc2[m+int((r-1)/2)][n+int((r-1)/2)]=im[idx_i,idx_j,u]
            im1[i,j,u]=np.median(msc2)
            

plt.subplot(121),plt.imshow(im, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(im1.astype(np.uint8), cmap = 'gray')
plt.title('Filtro'), plt.xticks([]), plt.yticks([])