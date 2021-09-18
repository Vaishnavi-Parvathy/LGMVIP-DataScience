#IMPORTING lIBRARY
import cv2
from IPython.display import Image

#LOADING THE IMAGE
i=" "  #any image_name in the format jpg/png 
img=cv2.imread(i)
print("Original_image")
Image(filename=i)

#CONVERTING IMAGE TO GREY-SCALE IMAGE
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_image.jpg",grayImg)
print("GREY_IMAGE")
Image(filename='gray_image.jpg') 

# CONVERTING GREY IMAGE TO INVERTED-GREY-IMAGE
invertedgrayImg=255-grayImg
cv2.imwrite("Inverted_gray_image.jpg",invertedgrayImg)
print("INVERTED_GRAY_IMAGE")
Image(filename='Inverted_gray_image.jpg') 

# CONVERTING INVERTED GREY IMAGE TO GAUSSIAN BLURRED IMAGE 
gaussianblurimg=cv2.GaussianBlur(invertedgrayImg,(21,21),0)
cv2.imwrite("gaussianImage.jpg",gaussianblurimg)
print("GAUSSIAN_BLURRED_IMAGE")
Image(filename='gaussianImage.jpg') 

#CONVERTING GAUSSIAN IMAGE TO INVERTED BLUR IMAGE
invertedblurImg=255-gaussianblurimg
cv2.imwrite("Inverted_blurred_image.jpg",invertedblurImg)
print("INVERTED_BLURRED_IMAGE")
Image(filename='Inverted_blurred_image.jpg') 

#CONVERTING INVERTED BLURRED IMAGE TO PENCIL-SKETCH
pencilsketch=cv2.divide(grayImg,invertedblurImg,scale=256.0)
cv2.imwrite("Pencil_sketch_image.jpg",pencilsketch)
print("PENCIL_SKETCH_IMAGE")
Image(filename='Pencil_sketch_image.jpg') 
