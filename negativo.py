# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im=Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg")
im=np.array(im)
im1=Image.open("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg")
print(im1.width,im1.height)
a=int(round(im1.width*(1050/720)))
b=int(round(im1.height*(9/4)))

im_1=im1.resize((a,b),Image.BILINEAR)
im_1=np.array(im_1)
im2=255-im

            
im = Image.fromarray(im2)
        
im1 = im.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\negativo.jpg")

plt.imshow(im)
plt.axis('off')
plt.show()