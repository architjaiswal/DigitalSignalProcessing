"""
Name: Archit Jaiswal

HW 5

Noise removal using a lowpass filter from an audio file

"""

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import freqz

#lowFs = 2000 # Sampling Frequency for low pass
Fc = 7500  # cut-off frequency for low pass
L = 101 # filter length for low pass
M = L - 1 # M = filter length - 1 for low pass

signal , Fs = sf.read('P_9_2.wav')


ft = Fc / Fs # normalized cut-off frequency
rectangular = [] # rectangular cooeficient
hamming = [] #hamming cooeficient
finalFilter = [] # element wise multiplication of hamming and rectangular

# creating an array of impulse response from the function given in the question
for i in range(0, L):
    
    hamming.append( 0.54 - ( (0.46) * np.cos( (np.pi * 2 * i)/M ) ) ) #hamming window
    
    if (i != (M/2)):
        rectangular.append( (np.sin(2*np.pi*ft*(i-(M/2))) / (np.pi * (i-(M/2)))  ))
    
    else:
        rectangular.append(2*ft)
    
    finalFilter.append(hamming[i] * rectangular[i])


plt.title("Frequency Response")
x1, y1 = freqz(rectangular, 1) #getting the frequency responce of rectangular
plt.plot(x1, abs(y1), label = 'original')


x2, y2 = freqz(finalFilter, 1) #getting the frequency responce of final window
plt.plot(x2, abs(y2), label = 'windowed')
plt.legend(loc = 'upper right')

outputAudio = np.convolve(finalFilter, signal)

sf.write( "cleanMusic.wav", outputAudio, Fs)

