# Name: Archit Jaiswal

# HW7: produce a filter bank to detect which of several frequencies are present in a signal. Also learn to apply bandpass filters.
#ASSUMPTION: signal length is a should be divisible by the number of samples per tone

# Decoding the numbers from sound

from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import spectrogram


def processTones(name, L, fs, samplesPerTone) :
    
    file = open(name, "r") #this is a file object
    inputData = np.fromfile(file, float, -1, ',') #it seperates the ',' from input
    file.close()

    totalNumberOfTones = len(inputData)/samplesPerTone #number of splits required in inputArray
    splited_Input = np.array_split(inputData,totalNumberOfTones) #array seperated based on number of tones

    bank = []#this is a bank of filters, it has all the bandpass filters and it is a 2D array
    
    fb = [697, 770, 852, 941, 1209, 1336, 1477]# only this frequencies will be checked
    
    for i in range (0, len(fb)):# creating the filter for bandpass
        bank.append([])
        for j in range (0, L):
            bank[i].append( (2/L) * np.cos( (2 * np.pi * fb[i] * j) /fs ) )
              
        
    #figure 1
    for i in range (0, len(bank)) : #converting it to frequency domain
        x, y = freqz(bank[i])
        plt.plot(((x*8000)/(2*np.pi)), abs(y))
    plt.xlabel("Hertz")
    plt.title("Frequency Responses of Bandpass Filters")
    plt.show()
    
    number = [] #this will store the phone number
    
    for i in range(0, len(splited_Input)):
        maxVal = []
        
        for j in range(0, len(bank)):
             maxVal.append(np.mean((np.convolve(splited_Input[i], bank[j]))**2))
            
        
        if(maxVal[0] == max(maxVal[:4])) :
            if(maxVal[4] == max(maxVal[4:])) : 
                number.append('1')
            elif(maxVal[5] == max(maxVal[4:])) : 
                number.append('2')
            else : 
                number.append('3')
        elif(maxVal[1] == max(maxVal[:4])) : 
            if(maxVal[4] == max(maxVal[4:])) : 
                number.append('4')
            elif(maxVal[5] == max(maxVal[4:])) : 
                number.append('5')
            else : 
                number.append('6')
        elif(maxVal[2] == max(maxVal[:4])) : 
            if(maxVal[4] == max(maxVal[4:])) : 
                number.append('7')
            elif(maxVal[5] == max(maxVal[4:])) : 
                number.append('8')
            else : 
                number.append('9')
        else : 
            if(maxVal[4] == max(maxVal[4:])) : 
                number.append('*')
            elif(maxVal[5] == max(maxVal[4:])) : 
                number.append('0')
            else : 
                number.append('#')      

    number = ''.join(number)
    
    
    f, t, Sxx = spectrogram(inputData, fs) #figure 2
    plt.pcolormesh(t, f, Sxx)
    plt.xlabel('Time [sec]')
    plt.ylabel('Frequency [Hz]')
    plt.show()
    
    
    return number
        
   

#############  main  #############
if __name__ == "__main__":
    filename = "tones.csv"  #  name of file to process
    L = 64                  #  filter length
    fs = 8000               #  sampling rate
    samplesPerTone = 4000   #  4000 samples per tone, 
                            #    NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)
    
    print(phoneNumber)
