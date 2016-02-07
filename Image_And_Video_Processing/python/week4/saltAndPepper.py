import numpy as np
import os
import cv2

def saltAndPepperNoise(image):	
	row,col = image.shape
	mean = 0
	#var = 0.1
	#sigma = var**0.5
	gauss = np.random.normal(mean,100,(row,col))
	gauss = gauss.reshape(row,col)
	saltAndPepperNoise = image + gauss
	return saltAndPepperNoise

kabutoMaskImage = cv2.imread('kabuto.jpg', cv2.IMREAD_GRAYSCALE)
kabutoMaskImage = saltAndPepperNoise(kabutoMaskImage)
cv2.imshow('kabuto', kabutoMaskImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
