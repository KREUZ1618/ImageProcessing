# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:33:00 2020

@author: win10
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 23:58:23 2020

@author: win10
"""

# for inline image display inside notebook
# % matplotlib inline
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from skimage.io   import imread, imsave, imshow, show, imread_collection
from skimage.io import imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl
from skimage.util import invert, random_noise, montage
import matplotlib.image as mpimg
import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
from scipy import misc


import cv2
import numpy as np
 


img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\A1.jpg")

im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

th,imbinary = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY)


kernel = np.ones((5,5),np.uint8)


erosion = cv2.erode(imbinary,kernel,iterations = 1)


img=Image.fromarray(imbinary)
erosion=Image.fromarray(erosion)

dif=subtract(img,erosion)

my_dpi=120

plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)


plt.subplot(141),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])


plt.subplot(142),plt.imshow(imbinary, cmap = 'gray')
plt.title('Binaria'), plt.xticks([]), plt.yticks([])


plt.subplot(143),plt.imshow(erosion, cmap = 'gray')
plt.title('Erosión'), plt.xticks([]), plt.yticks([])


plt.subplot(144),plt.imshow(dif, cmap = 'gray')
plt.title('extraccion de contorno'), plt.xticks([]), plt.yticks([])
