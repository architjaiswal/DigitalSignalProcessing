"""
Name: Archit Jaiswal
UTA ID: 1001543326
HW 4 

Applying the filters to image

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


import glob
originalImage = []
lowpass_output = []
highpass_output = []
filenames = []

h_lowpass = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1] #impulse respose of a low pass filter
h_highpass = [1 , -1] # impulse respose of a high pass filter

for filename in glob.glob('*.tiff'): #this will read all the .tiff files in the directory
    ima=plt.imread(filename) #stores an 2D array of image in "ima"
    plt.title(f'{filename}') #prints the original name of file
    plt.imshow(ima, cmap='gray') # shows the original image back but 'gray' is needed to see clear image
    plt.show()
    originalImage.append(ima) #keeping the track of original image in "originalImage" list
    filenames.append(filename) #storing all the file names in "filenames" list
    
    arrLow = list( ima) # "ima" cannot be modified so it has to be stored befor convolving
    arrHigh = list(ima)
 
    for i in range(len(ima)):
        arrLow[i] = np.convolve(ima[i],h_lowpass ) #convolving the image with lowpass 
        arrHigh[i] = np.convolve(ima[i], h_highpass) #convolving the image with highpass

    #plotting the image processed from low pass filter    
    plt.title("%s with lowpass filter" %filename)
    plt.imshow(arrLow, cmap = 'gray')
    plt.show()
    lowpass_output.append(arrLow) # storing the output result in "lowpass_output" list
    
    #plotting the image processed from high pass filter    
    plt.title("%s with highpass filter" %filename)
    plt.imshow(arrHigh, cmap = 'gray')
    plt.show()
    lowpass_output.append(arrHigh) #storing the output result in "highpass_output" list
        
    
for filename in glob.glob('*.jpg'): #it will read all the .jpg file
    ima=plt.imread(filename)
    plt.title(f'{filename}')
    plt.imshow(ima, cmap='gray')
    plt.show()
    arrLow = list( ima)
    arrHigh = list(ima)
    for i in range(len(ima)):
        arrLow[i] = np.convolve(ima[i],h_lowpass ) # processing image from lowpass filter
        arrHigh[i] = np.convolve(ima[i], h_highpass)

    #plotting the image obtained from low pass filter        
    plt.title("%s with lowpass filter" %filename)
    plt.imshow(arrLow, cmap = 'gray')
    plt.show()
    
    #plotting the image processed from high pass filter    
    plt.title("%s with highpass filter" %filename)
    plt.imshow(arrHigh, cmap = 'gray')
    plt.show()
    
    # processing the image with median filter 
    outputImage = ndimage.median_filter(ima,5)
    plt.title("%s with median filter" %filename)
    plt.imshow(outputImage, cmap = 'gray')
    plt.show()
    