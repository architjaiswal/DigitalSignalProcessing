"""
Name: Archit Jaiswal

HW 08: Learn to amplify or attenuate a particular range of frequencies.
"""


import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf



def applyShelvingFilter(inName, outName, g, fc) :
    signal , fs = sf.read(inName) # fs is the sample frequency of inputfile
    N = len(signal)
    
    mue = 10 ** ( g/20 )
    
    w = 2 * np.pi * fc / fs
    gamma = (1 - ((4/(1+mue)) * np.tan(w/2)) ) / (1 + (4/(1+mue)) * np.tan(w/2))
    alpha = (1- gamma) / 2
    
    u = []
    y = [] # this will contain the final filtered signal
    
    for i in range(N):
        if((i-1) < 0):
            u.append(alpha * (signal[i] + 0) + 0)
        else:
            u.append(alpha * (signal[i] + signal[i-1]) + gamma * u[i-1])
        
        y.append( signal[i] + (mue - 1) * u[i] )

    fftsignal = np.fft.fft(signal)
    signalSampleFreq = np.fft.fftfreq(N, d = 1/fs)
    
    fftY = np.fft.fft(y)
    filteredSampleFreq = np.fft.fftfreq(len(fftY), d = 1/fs)
    
    
    originalMax = max(abs(fftsignal))
    filteredMax = max(abs(fftY))
    
    yMax = max(originalMax, filteredMax) + 100 #this determines the maximum of y axis for plots
    
    #plotting for original signal

    fig, plots = plt.subplots(nrows=1, ncols=2)
    plots[0].plot(abs(signalSampleFreq[:int(N/4)]), abs(fftsignal[:int(N/4)])) 
    plots[0].set_title("Original Signal")
    plots[0].set_xlabel('Hz')
    plots[0].set_ylim([0,yMax])
    
    plots[1].plot(abs(filteredSampleFreq[:int(N/4)]), abs(fftY[:int(N/4)])) 
    plots[1].set_title("Filtered Signal")
    plots[1].set_xlabel('Hz')
    plots[1].set_ylim([0,yMax])
    plt.tight_layout()
    plt.show()
    
    sf.write(outName, y, fs)
    
##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -10  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
