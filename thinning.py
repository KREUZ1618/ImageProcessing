# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:59:07 2020

@author: win10
"""
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pylab as plt

 
# Create an image with text on it
img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\cierre.jpg",0)



img1=img.copy()
 
# Structuring Element
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# Create an empty output image to hold values
thin = np.zeros(img.shape,dtype='uint8')

for var in list(range(50)):
            # Erosion
            erode = cv2.erode(img1,kernel)
    # Opening on eroded image
            opening = cv2.morphologyEx(erode,cv2.MORPH_OPEN,kernel)
    # Subtract these two
            subset = erode - opening
    # Union of all previous sets
            thin = cv2.bitwise_or(subset,thin)
    # Set the eroded image for next iteration
            img1 = erode.copy()
   
    
        
        
        


    

img=Image.fromarray(img)
thin=Image.fromarray(thin)


my_dpi=120

plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])



thinning2= img.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\thinning.jpg")





    


