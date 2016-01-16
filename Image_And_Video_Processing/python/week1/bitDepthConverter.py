
from scipy import misc
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

bitReduceString = raw_input('reduce image to ... bit? ')

bitReduceInt = 0
try:
	bitReduceInt = int(bitReduceString)
except:
	bitReduceInt =0

if bitReduceInt > 1:
	#img = misc.img()
	img = misc.imread('bowie_on_tour.jpg')

	print 'img size: ', img.size
	print 'img size x: ', img.shape
	print 'img.dtype: ', img.dtype

	imgTrans = np.float32(img)
	print 'init'
	print imgTrans
	imgTrans = ndimage.gaussian_filter(imgTrans, sigma = 1.5)
	imgTrans = imgTrans / (2**bitReduceInt)
	imgTrans = np.floor(imgTrans)
	imgTrans = imgTrans * (2**bitReduceInt)
	imgTransInt = np.uint8(imgTrans)
	#imgTransInt = ndimage.gaussian_filter(imgTransInt, sigma = 1)

	print 'result'
	print imgTrans	

	print 'imgTrans size: ', imgTrans.size
	print 'imgTrans size x: ', imgTrans.shape
	print 'imgTrans.dtype: ', imgTrans.dtype

	plt.imshow(imgTransInt)
	plt.show()
else:
	print 'bit reduce should be more than 1' 
