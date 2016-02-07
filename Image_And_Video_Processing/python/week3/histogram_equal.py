import cv2
import numpy as np
from matplotlib import pyplot as plt

oriImg = cv2.imread('unEqImg.jpg',0)
oriHist,oriBins = np.histogram(oriImg.flatten(), 256,[0,256])

oriImgCdf = oriHist.cumsum()

f,plotA = plt.subplots(2, sharex = True)

plotA[0].plot(oriImgCdf, color = 'b')
plotA[1].hist(oriImg.flatten(), 256,[0,256], color = 'r')

eqedImg = cv2.equalizeHist(oriImg)
eqedHist,eqedBins = np.histogram(eqedImg.flatten(), 256,[0,256])

eqedImgCdf = eqedHist.cumsum()

f,plotB = plt.subplots(2, sharex = True)

plotB[0].plot(eqedImgCdf, color = 'b')
plotB[1].hist(eqedImg.flatten(), 256,[0,256], color = 'r')

plt.show()

res = np.hstack((oriImg, eqedImg))
cv2.imwrite('result.png', res)

print 'done'
