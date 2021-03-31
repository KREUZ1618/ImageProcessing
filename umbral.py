# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 00:14:00 2020

@author: win10
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg",0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Imagen Original','Binaria','Binaria inversa','Truncada','A cero','A cero inversa']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
miArray = np.arange(6)
for i in miArray:
  plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])

plt.show()