# Name: Archit Jaiswal
# adding the sinusoids of specific frequencies to lead a "twinkle - twinkle rhyme"

import numpy as np
import soundfile as snf
 

A = 1
key = np.array([52, 52, 59, 59, 61, 61, 59, 59, 57, 57, 56, 56, 54, 54, 56, 32, 59, 59, 57, 57, 56, 56, 54, 54])


Ts = 0.008
T = 0.5
t = np.arange( 0, 0.5, 1/8000)
print(np.arange(0, 5 , 1/2))

abc = []
 
for i in key:
    f = 440 * 2 ** ((i-49)/12)
    audio = A * np.cos( 2 * np.pi * f * t )
    abc = np.append(abc, audio)
    #print(audio)
   
snf.write( "twinkle.wav", abc, 8000)