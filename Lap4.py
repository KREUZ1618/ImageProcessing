# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:20:52 2020

@author: DELL
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from Bordesi import Bordesi as Bi
from Bordesj import Bordesj as Bj
from Histograma import Histograma as H
im=Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\V6.jpg")
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

msc=np.array([[0,1,0],[1,-4,1],[0,1,0]])
r=msc.shape[0] #Tamaño de la máscara

for u in range(0,w):
    for i in range(0,v):
        for j in range(0,t):
            for m in range(int(-(r-1)/2),int((r-1)/2)+1):
                for n in range(int(-(r-1)/2),int((r-1)/2+1)):
                    idx_i=Bi(i+m,v,m,b)
                    idx_j=Bj(j+n,t,n,b)
                    im1[i,j,u]=im1[i,j,u]+(im[idx_i,idx_j,u]*msc[m+int((r-1)/2),n+int((r-1)/2)])


a=np.zeros(shape=(v,t)) #Matriz apoyo
Imax=np.zeros(shape=(w))
Imin=np.zeros(shape=(w))

for i in range(0,w):
    for j in range(0,v):
        for k in range(0,t):
            a[j,k]=im1[j,k,i]
    Imax[i]=np.amax(a)
    Imin[i]=np.amin(a)


for i in range(0,w):
    for j in range (0,v):
        for k in range(0,t):
            im1[j,k,i]=int(round(255*(im1[j,k,i]-Imin[i])/(Imax[i]-Imin[i])))


plt.imshow(im1.astype(np.uint8))
plt.axis('off')
plt.show()

H(im1,1,w,v,t)