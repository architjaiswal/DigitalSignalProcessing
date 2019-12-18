"""
Name: Archit Jaiswal

HW 6

Knowing the frequecy of noise and manually zeroing the noise frequecies to filter
Then doing inverse FFT to obtain the original signal back after filtering the signal
Noise removal using the FFT (FAST FOURIER TRANSFORM)

"""
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import freqz


def processFile(fn, offset) :
    signal , Fs = sf.read(fn)
    fftSignal = np.fft.fft(signal)
    ifftSignal = fftSignal
    
    fig, plots = plt.subplots(nrows=1, ncols=2)
    plots[0].plot(np.abs(fftSignal)) #plotting the FFT
    plots[0].set_title("Original Signal")
  
    midpoint = len(fftSignal)/2
    start = (int)(midpoint - offset)
    end = (int)(midpoint + offset)
    
    ifftSignal[start:end]= 0
        
    final = np.fft.ifft(ifftSignal)
    sf.write( "cleanMusic.wav", np.real(final), Fs) #only need the real part 
    plots[1].plot(np.abs(ifftSignal)) # plotting the modified FFT not IFFT
    plots[1].set_title("ifft Signal")
    plt.tight_layout()
    plt.show()
   

##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 10000

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)
