import cv2 as cv
import numpy as np
import tkinter
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')

img = cv.imread('opencv.jpeg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag_spec = 20*np.log(np.abs(fshift))

dft = cv.dft(np.float32(img),flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fft2(dft)

#mag = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(mag_spec, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(123),plt.imshow(dft, cmap = 'gray')
plt.title('Magnitude Spectrum2'), plt.xticks([]), plt.yticks([])
plt.show()