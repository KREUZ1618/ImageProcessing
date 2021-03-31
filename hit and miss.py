# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:51:07 2020

@author: win10
"""

import cv2 as cv
import numpy as np
import matplotlib.pylab as plt
input_image = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 0, 0, 255],
    [0, 255, 0, 255, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 255, 0, 0],
    [0, 0, 255, 0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0, 255, 255, 0],
    [0,255, 0, 255, 0, 0, 255, 0],
    [0, 255, 255, 255, 0, 0, 0, 0]), dtype="uint8")
kernel = np.array((
        [1, 1, 1],
        [1, -1,1],
        [1, 1, 1]), dtype="int")


image = cv.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg",0)

output_image = cv.morphologyEx(image, cv.MORPH_HITMISS, kernel)

rate = 50

kernel = (kernel + 1) * 127

kernel = np.uint8(kernel)

my_dpi=120


input_image=np.array(input_image)
output_image=np.array(output_image)

plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)


plt.subplot(141),plt.imshow(kernel, cmap = 'gray')
plt.title('kernel'), plt.xticks([]), plt.yticks([])


plt.subplot(142),plt.imshow(image, cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(143),plt.imshow(output_image, cmap = 'gray')
plt.title('hit and miss'), plt.xticks([]), plt.yticks([])




plt.subplot(144),plt.imshow(output_image, cmap = 'gray')
plt.title('fill'), plt.xticks([]), plt.yticks([])

