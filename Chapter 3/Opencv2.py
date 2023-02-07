#Install library OpenCV
import cv2

#Membaca gambar
img = cv2.imread('kucing.png')
#Menampilkan gambar
cv2.imshow('kucing',img)
#Menyimpan gambar
cv2.imwrite('save_kucing.png',img)

#Menunda windows terdestroy
cv2.waitKey(0)
#Mendestroy windows
cv2.destroyAllWindows()