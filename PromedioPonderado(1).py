# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:02:31 2020

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

msc=np.array([[1,3,1],[3,8,3],[1,3,1]])
r=msc.shape[0] #Tamaño de la máscara

for u in range(0,w):
    for i in range(0,v):
        for j in range(0,t):
            for m in range(int(-(r-1)/2),int((r-1)/2)+1):
                for n in range(int(-(r-1)/2),int((r-1)/2+1)):
                    idx_i=Bi(i+m,v,m,b)
                    idx_j=Bj(j+n,t,n,b)
                    im1[i,j,u]=im1[i,j,u]+(im[idx_i,idx_j,u]*msc[m+int((r-1)/2),n+int((r-1)/2)])
q=np.sum(msc)
for i in range(0,w):
    for j in range (0,v):
        for k in range(0,t):
            im1[j,k,i]=int(round(im1[j,k,i]/q))
plt.imshow(im1.astype(np.uint8))
plt.axis('off')
plt.show()

H(im,0,w,v,t)