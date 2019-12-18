#Name: Archit Jaiswal
#UTAID: 1001543326
#HW 10: weather analysis


import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict



def getData(fn) :

    columns = defaultdict(list) # each value in each column is appended to a list

    with open(fn) as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
                                
    data = np.asarray(columns['HLY-TEMP-NORMAL'], dtype = float)
    N = len(data)
    return data, N

def analysis(temps, tfft, N) :
    fs = 1 # sample per hour
    n = tfft.size
    freq = np.fft.fftfreq(n)
    print('Sampling rate:%d sample per hour'%fs)
    f0 = fs / N
    print('Fundamental frequency:%f samples per hour'%f0)
    absolute = np.abs(tfft)
    indices = absolute.argsort()[-3:][::-1]
    print("Index of the DFT coefficient with the largest magnitude: %d"%indices[0])
    print("Index of the DFT coefficient with the 2nd largest magnitude: %d"%indices[1])
    print("Index of the DFT coefficient with the 3rd largest magnitude: %d"%indices[2])
    print('The temprature data has most frequecy of: %f'%freq[indices[0]])
    print('The temprature data has 2nd most frequecy of: %f'%freq[indices[1]])
    print('The temprature data has 3rd most frequecy of: %f'%freq[indices[2]])


    
def plotTemps(t, tfft, N) :
    plt.plot(t[:24])
    plt.xlabel('hours')
    plt.ylabel('temprature')
    plt.title('first 24 hours of temprature')
    plt.show()
    
    plt.plot(t[:7*24])
    plt.xlabel('days')
    plt.ylabel('temprature')
    plt.title('first 7 days of temprature')
    plt.show()
    
    plt.plot(t[:365*24])
    plt.xlabel('days')
    plt.ylabel('temprature')
    plt.title('first 365 days of temprature')
    plt.show()
    
    mag = np.abs(tfft)
    halfNum=  len(tfft)//2
    n = tfft.size
    freq = np.fft.fftfreq(n)
    plt.plot(abs(freq[:halfNum]), mag[:halfNum])
    plt.xlabel('hours')
    plt.title('magnitude of DFT')
    plt.show()

    X_db = 20*np.log(mag);
    plt.plot(abs(freq[:halfNum]), X_db[:halfNum])
    plt.xlabel('hours')
    plt.title('logs magnitude of DFT')
    plt.show()

##################  main  ##################
#   DO NOT CHANGE THIS
fn = "weather.csv"

#  temps = list or ndarray of temperature values
#      N = number of elements in temps
temps, N = getData(fn)

#  tfft = DFT coefficents of temps
tfft = np.fft.fft(temps)

analysis(temps, tfft, N)
plotTemps(temps, tfft, N)
