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

im = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\FPApasabandasSigmaMenor70SigmaMayor80.jpg",0) # read the image, provide the
im2 = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\P5_FRBan_butterworth_Dcl70_nl8_Dch80_nh2.png",0)




import cv2
import numpy as np
 
img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\FPApasabandasSigmaMenor70SigmaMayor80.jpg",0)
kernel = np.ones((7,7),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)


plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])


plt.subplot(132),plt.imshow(erosion, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(substraction, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])


