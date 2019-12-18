"""
Name: Archit Jaiswal
UTA ID: 1001543326
HW 10: Blind source seperation - Seperates sound from background noise
"""


import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import FastICA, PCA


def unmixAudio(leftName, rightName) :
    mixed0 , fs0 = sf.read(leftName) # fs0 is the sample frequency of mixed0 
    mixed1 , fs1 = sf.read(rightName)

    inputSignals = np.c_[mixed0, mixed1]
    
    #this is the sourse reperation from the instructions provided
    ica = FastICA(n_components=2)
    S_ = ica.fit_transform(inputSignals)
    A_ = ica.mixing_  # Get estimated mixing matrix
    S_ = S_.T # transposing to get the signals as rows of 2D matrix

    unmixed0 = S_[0] # this is 1st indepedent source
    unmixed1 = S_[1] # this is 2nd indepedent source

    # seperated signal will have less amplitude so multiplying it by 10
    unmixed0 = unmixed0 * 10 
    unmixed1 = unmixed1 * 10
    
    
    # wrinting to the file
    sf.write('unmixed0.wav', unmixed0, fs0)
    sf.write('unmixed1.wav', unmixed1, fs1)
    
    #plotting in time domain
    fig, plots = plt.subplots(4)
    plots[0].plot(mixed0)
    plots[0].set_title(leftName)
    
    plots[1].plot(mixed1)
    plots[1].set_title(rightName)
    
    plots[2].plot(unmixed0)
    plots[2].set_title('unmixed0.wav')
    
    plots[3].plot(unmixed1)
    plots[3].set_title('unmmixed1.wav')
    
    plt.tight_layout() 
    plt.show()
    
    
###################  main  ###################
if __name__ == "__main__" :
    leftName = "darinSiren0.wav"
    rightName = "darinSiren1.wav"
    unmixAudio(leftName, rightName)
