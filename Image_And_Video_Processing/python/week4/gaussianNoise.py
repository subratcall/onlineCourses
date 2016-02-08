import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def 

kabutoMaskImage = (misc.imread('kabuto.jpg')).astype(float)
print 'image type : ',kabutoMaskImage.dtype
print 'image shape :', kabutoMaskImage.shape

gaussianNoise = np.random.normal(0,100.0, (kabutoMaskImage.shape))

kabutoMaskImage = kabutoMaskImage + gaussianNoise

plt.imshow(kabutoMaskImage, cmap = plt.cm.gray)
plt.show()

