# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:02:24 2020

@author: win10
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:48:51 2020

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
 


img = cv2.imread("C:\\Users\win10\Desktop\procesamiento de imagenes\A2_Gaussian_FPBidealDC100.jpg")

im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


kernel = np.ones((2,2),np.uint8)


apertura = cv2.morphologyEx(im_gray, cv2.MORPH_OPEN, kernel)

my_dpi=120

plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(apertura, cmap = 'gray')
plt.title('Apertura'), plt.xticks([]), plt.yticks([])

