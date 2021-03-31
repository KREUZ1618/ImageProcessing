

from PIL import Image
import math as m
import numpy as np
import matplotlib.pyplot as plt


im=Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\M10.jpg")
im1=Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\M10.jpg")
print(im.width,im.height)
ancho=im.width
alto=im.height
im=np.array(im)
im1=np.array(im1)
print(im.ndim)
print(len(im))
print(im.shape)
g=255/(1-m.exp(-2))

for i in range(0,3):
    for j in range(0,alto):
        for k in range(0,ancho):                               
            u=int(round(g*((1-m.exp((-2*im[j,k,i])/255)))))
            if(u>255):
                print("ERROR!!!")
                i=3
                j=alto
                k=ancho
            im[j,k,i]=u
            u=0

im = Image.fromarray(im)      

im1 = im.save("C:\\Users\win10\Desktop\procesamiento de imagenes\exponencial.jpg")


plt.imshow(im)
plt.axis('off')
plt.show()