"""
Name: Archit Jaiswal
UTA ID: 1001543326
HW 4 

Create a lowpass filter and a highpass filter by convolving the input with the 
 impulse responce of a system, whose function is given in the question
"""

#Low Pass filter

import numpy as np
import matplotlib.pyplot as plt

lowFs = 2000 # Sampling Frequency for low pass
lowFc = 50  # cut-off frequency for low pass
filterLenLowPass = 21 # filter length for low pass
M_lowPass = filterLenLowPass - 1 # M = filter length - 1 for low pass
extraLowFreq = 4

ft_lowPass = lowFc / lowFs # normalized cut-off frequency
impulseResponseLowPass = [] # systems response after low passing impulse response

file = open("data-filtering.csv", "r") #this is a file object
input = np.fromfile(file, float, -1, ',') #it seperates the ',' from input
file.close()

fig, LowPlot = plt.subplots(3) # it will show all 3 figures togather

# plotting the original        

LowPlot[0].plot(input)
LowPlot[0].set_title("Original Signal")

# creating an array of impulse response from the function given in the question
for i in range(0, filterLenLowPass):
    if (i != (M_lowPass/2)):
        impulseResponseLowPass.append(np.sin(2*np.pi*ft_lowPass*(i-(M_lowPass/2))) / (np.pi * (i-(M_lowPass/2))) )
        
    else:
        impulseResponseLowPass.append(2*ft_lowPass)
        
# plotting the 4 hz frequency as given in the question
t = np.arange(0, 1 , (1/lowFs))
LowPlot[1].plot(np.cos(2*np.pi * extraLowFreq * t))
LowPlot[1].set_title("%d Hz signal"% extraLowFreq)


# plotting the output after convolution

resultLowPass = np.convolve(impulseResponseLowPass, input) # convolving the input with the impulse responce to get the output of system
LowPlot[2].plot(resultLowPass)
LowPlot[2].set_title("application of lowpass filter")

fig.tight_layout() # this sets the layout proporly otherwise it mixes titles with graphs


# High Pass Filter

highFs = 2000 # Sampling Frequency for high pass
highFc = 280  # cut-off frequency for high pass
filterLenHighPass = 21 # filter length for high pass
M_highPass = filterLenHighPass - 1 # M = filter length - 1
extraHighFreq = 330

figHigh, HighPlot = plt.subplots(3) # it will show all 3 figures togather


ft_highPass = highFc / highFs # normalized cut-off frequency for high pass filter
impulseResponseHighPass = [] # systems response after high passing impulse response

# plotting only the first 100 values from input as mentioned in the question
HighPlot[0].plot(input[:100])
HighPlot[0].set_title("Original Signal")

#plotting the 330 hz signal as mentioned in the question
t = np.arange(0, 1 , (1/highFs))
HighPlot[1].plot(np.cos(2*np.pi * extraHighFreq * t)[:100])
HighPlot[1].set_title("%d Hz signal"%extraHighFreq)

# creating the impulse response array from the function given in the question
for i in range(0, filterLenHighPass):
    if (i != (M_highPass/2)):
        impulseResponseHighPass.append((-1) * np.sin(2*np.pi*ft_highPass*(i-(M_highPass/2))) / (np.pi * (i-(M_highPass/2))) )
        
    else:
        impulseResponseHighPass.append(1 - (2*ft_highPass))
        
# plotting only the first 100 values of input
resultHighPass = np.convolve(impulseResponseHighPass, input[:100]) # convolving the impulse response of the system with input to generate system output
HighPlot[2].plot(resultHighPass[:100])
HighPlot[2].set_title("application of highpass filter")

figHigh.tight_layout() # this sets the layout proporly otherwise it mixes titles with graphs
