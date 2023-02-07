import cv2
import matplotlib.pyplot as plt
import numpy as np
 
img = cv2.imageread(‘namafile’)
 
np.copy() merupakan fungsi untuk mengcopy array dari image.
 
img_bgr = np.copy(img)
 
cv2.cvtColor(source_img, color_space) merupakan fungsi yang di gunakan untuk melakukan konversi color space. Seperti yang sudah kita dibahas sebelumnya defaul dari Opencv merupakan BGR.
 
cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) aka melakukan konversi dari BGR menjadi RGB.
 
img_rgb = cv2.cvtCOLOR(img_bgr, cv2COLOR_BGR2RGB)
 