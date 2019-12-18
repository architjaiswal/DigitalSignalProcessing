# Name: Archit Jaiswal

# HW8: apply a notch filter to a signal to eliminate a specific frequency. Also gain experience with z-transforms.


import numpy as np
import matplotlib.pyplot as plt


def applyNotch(fs, dataFile) :
    file = open(dataFile, "r") #this is a file object
    x = np.fromfile(file, float, -1, ',') #it seperates the ',' from input
    file.close()
    y = []
    N = len(x) #it has the length of input signal

    
    f = 17 #this is the frequency which needs to be filtered
    w = 2 * np.pi * f / fs #this is the omega cap for cos function in the difference equation
    
    # y[n] = 1.8744 * cos(w) * y[n-1] - 0.8783 * y[n-2] + x[n] - 2 * cos(w) * x[n-1] + x[n-2] 
    
    for i in range(N+100):
        if((i-1)<0 ):
            y.append(0 - 0 + x[i] - 0 + 0)
            
        elif((i-1)>=0 and (i-2)<0):
            y.append(1.8744 * np.cos(w) * y[i-1] - 0 + x[i] - 2 * np.cos(w) * x[i-1] + 0)
            
        elif(i<N):
            y.append(1.8744 * np.cos(w) * y[i-1] - 0.8783 * y[i-2] + x[i] - 2 * np.cos(w) * x[i-1] + x[i-2])
            
        elif(i>=N and i-1 < N):
             y.append(1.8744 * np.cos(w) * y[i-1] - 0.8783 * y[i-2] + 0 - 2 * np.cos(w) * x[i-1] + x[i-2])
    
        elif(i>=N and i-1 >= N and i-2 < N):
             y.append(1.8744 * np.cos(w) * y[i-1] - 0.8783 * y[i-2] + 0 - 0 + x[i-2])
             
        else:
            y.append(1.8744 * np.cos(w) * y[i-1] - 0.8783 * y[i-2] + 0 - 0 + 0)
    
    
    # plotting original signal and filtered signal
    plt.title('Original Signal X')
    plt.xlim([-25, 625])
    plt.plot(x)
    plt.show()    
    plt.title('Filtered Signal Y')
    plt.ylim([-2.25, 2.25])
    plt.plot(y)
    plt.show()
    
    # preparing 10 Hz and 33 Hz signal
    t= np.arange(0, 1, 1/fs )
    y10Hz = np.cos(2*np.pi* 10 * t)
    y33Hz = np.cos(2 * np.pi * 33 * t)
    
    tempSignal = np.add(y10Hz, y33Hz) # adding the amplitudes of signals in time domain
    
    #plotting the combined signal
    plt.title('Combined 10 Hz and 33 Hz signal')
    plt.xlim([-25,625])
    plt.plot(tempSignal)
    plt.show()
    



############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
