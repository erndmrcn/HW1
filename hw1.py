# Eren Demircan - 2237246
# CEng483 - Computer Vision
# HW1 - Instance Recognition with Histogram

# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

allImages = []
imageInstances = []
imageNames = []

# utility functions

def parseInstances(fileName):
    global imageNames
    with open(fileName) as f:
        imageNames = f.readlines()
    
    for i in range(len(imageNames) - 1):
            imageNames[i] = imageNames[i][:-1]
    return

# read image
def readImage(filePath):
    img = plt.imread(filePath)
    return img

# create image grids with given size
def divideImage(im, row, column):
    return

def histogram(im, bin):
    hist, bin_edges = np.histogram(im, bin)
    return hist, bin_edges

def plotHistogram():
    return

def showImage():
    return

def readImages(folder):
    for fileName in os.listdir(folder):
        img = mpimg.imread(os.path.join(folder, fileName))
        if img is not None:
            allImages.append(img)
    
    return

# queries
readImages("query_1")
print(len(allImages))
# print(allImages)
parseInstances("InstanceNames.txt")
img = readImage("query_1/" + imageNames[0])


plt.imshow(img)
plt.show()