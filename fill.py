# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:59:07 2020

@author: win10
"""
import cv2 as cv
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pylab as plt
from PIL.ImageChops import add, subtract, multiply, difference, screen

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


image = cv.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\M7.jpg")

im_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

th,imbinary = cv.threshold(im_gray, 128, 255, cv.THRESH_BINARY)

imbinary2=Image.fromarray(imbinary)

imbinary2 = imbinary2.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\binary.jpg")

output_image = cv.morphologyEx(imbinary, cv.MORPH_HITMISS, kernel)

rate = 50

kernel = (kernel + 1) * 127

kernel = np.uint8(kernel)

my_dpi=120


input_image=np.array(input_image)
output_image=np.array(output_image)

plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)


plt.subplot(141),plt.imshow(kernel, cmap = 'gray')
plt.title('kernel'), plt.xticks([]), plt.yticks([])


plt.subplot(142),plt.imshow(imbinary, cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])


plt.subplot(143),plt.imshow(output_image, cmap = 'gray')
plt.title('hit and miss'), plt.xticks([]), plt.yticks([])

imbinary=Image.fromarray(imbinary)
output_image=Image.fromarray(output_image)


add=add(imbinary,output_image)

addarray=np.array(add)

add2= add.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\fill.jpg")


kernel = np.ones((3,3),np.uint8)

apertura = cv.morphologyEx(addarray, cv.MORPH_OPEN, kernel)

apertura2=Image.fromarray(apertura)

apertura2= apertura2.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\apertura.jpg")

cierre = cv.morphologyEx(apertura, cv.MORPH_CLOSE, kernel)

cierre2=Image.fromarray(cierre)

cierre2= cierre2.save("C:\\Users\win10\Desktop\procesamiento de imagenes\\cierre.jpg")



plt.subplot(144),plt.imshow(add, cmap = 'gray')
plt.title('fill'), plt.xticks([]), plt.yticks([])