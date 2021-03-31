# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:32:09 2020

@author: DELL
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from Bordesx import Bordesx as Bx
from Bordesy import Bordesy as By
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
idx=0
b=0 #Tipo de borde
msc=np.array([[1,3,1],[3,8,3],[1,3,1]])
r=msc.shape[0] #Tamaño de la máscara
msc2=np.zeros(shape=(r,r))
vec=np.zeros(shape=(np.sum(msc)))
for u in range(0,w):
    for i in range(0,v):
        for j in range(0,t):
            for m in range(int(-(r-1)/2),int((r-1)/2)+1):
                for n in range(int(-(r-1)/2),int((r-1)/2+1)):
                    idx_i=Bx(i+m,v,m,b)
                    idx_j=By(j+n,t,n,b)
                    msc2[m+int((r-1)/2)][n+int((r-1)/2)]=im[idx_i,idx_j,u]
                    q=0
                    while(q<msc[m+int((r-1)/2)][n+int((r-1)/2)]):
                        vec[idx+q]=msc2[m+int((r-1)/2)][n+int((r-1)/2)]
                        if(q==(msc[m+int((r-1)/2)][n+int((r-1)/2)]-1)):
                            idx=q
                        q=q+1
            im1[i,j,u]=np.median(vec)
            idx=0
            vec=0
plt.imshow(im1.astype(np.uint8))
plt.axis('off')
plt.show()
H(im1,1,w,v,t)