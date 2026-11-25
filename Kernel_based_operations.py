import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.ndimage import convolve
img=cv2.imread(r"D:\ACB-Backup-25-12-24\ACPC-Ira\Photo-sign\myphoto1.jpg",0)

kernel=[[0,0,0],[5,5,5],[0,0,0]]
im=np.array(img,dtype=float)
img2=convolve(im,kernel)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(img2,cmap='gray')
plt.show()
# perform 7-different kernel operations over your own image and observe output...define kernel of your own choice
#second task make a kernel where center of image is proper and rest part is blur.
#1 operation: 5x5 kerne with weights[[1,1,1,1,1], [1,1,1,1,1],[1,1,-5,1,1],[1,1,1,1,1],[1,1,1,1,1]]
#2 operation kernel=np.ones((7,7),np.float32)/49
#3 operation kernel=[[0,0,0],[1,1,1],[0,0,0]]
#4 operation kernel=[[0,0,0],[-1,5,-1],[0,0,0]]