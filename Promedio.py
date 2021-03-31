# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:21:34 2020

@author: DELL
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from Bordesx import Bordesx as Bx
from Bordesy import Bordesy as By

im=Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\Ruido_gaussiano\A1_gauss.png")
v=im.size[1]   #Dimensión uno
t=im.size[0]   #Dimensión dos
w=3

im=np.array(im)
im1=np.zeros(shape=(v,t,w))
b=0 #Tipo de borde
r=4 #Tamaño de la máscara
msc=np.ones(shape=(r,r))

for u in range(0,w):
    for i in range(0,v):
        for j in range(0,t):
            for m in range(int(-(r-1)/2),int((r-1)/2)+1):
                for n in range(int(-(r-1)/2),int((r-1)/2+1)):
                    idx_i=i+m 
                    idx_j=j+n
                    idx_i=Bx(i+m,v,m,b)
                    idx_j=By(j+n,t,n,b)
                    im1[i,j,u]=im1[i,j,u]+(im[idx_i,idx_j]*msc[m+int((r-1)/2),n+int((r-1)/2)])


q=np.sum(msc)
for i in range(0,w):
    for j in range (0,v):
        for k in range(0,t):
            im1[j,k,i]=int(round(im1[j,k,i]/q))






plt.subplot(121),plt.imshow(im, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(im1.astype(np.uint8), cmap = 'gray')
plt.title('Filtro'), plt.xticks([]), plt.yticks([])

