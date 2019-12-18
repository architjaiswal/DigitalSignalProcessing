"""
Name: Archit Jaiswal
HW 3: decode a message by using match filter that is dot product
"""
import numpy as np
from numpy.linalg import norm

file = open("data-communications.csv", "r") #this is a file object
input = np.fromfile(file, float, -1, ',') #it seperates the ',' from input
file.close()

arrayOfInput = np.array(input) 
numOfarraysRequired = len(arrayOfInput)/10 #each vector has 0 elements because each pulse has 10 values

vector = np.array_split(arrayOfInput, numOfarraysRequired ) #splitting the input into various vector with 10 elements

# below 4 lines were provided in the question
pulse0 = np.ones( 10 )
pulse0 = pulse0/np.linalg.norm(pulse0)
pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
pulse1 = pulse1/np.linalg.norm(pulse1)
normPulse0 = norm(pulse0) #finding the magnitude of vector 
normPulse1 = norm(pulse1)

message = [] #this will contain the final decoded message as a list
bits = [] #it contains binary for each character to be decoded (8 bit binary is 1 character)
index = 0 #to reset the bits list after filling it for 1 character

for i in range(int(numOfarraysRequired)):
    if( (np.dot(pulse0, vector[i])/(norm(vector[i]) * normPulse0)) < (np.dot(pulse1, vector[i])/(norm(vector[i]) * normPulse1)) ):
        bits.append(1) #storing bit 1 in the bits list
        
    else:
        bits.append(0) #storing bit 0 in the bits list
    
    index = index + 1 #increading the index to keep track of how many bits are obtained
    
    if( index > 7):
        index = 0
        res = 0
        for ele in bits: #this converts binary to integer
            res = (res << 1) | ele
        message.append(chr(res)) #it pushes the binary value to ASCII character in message list
        bits = [] # resetting the list to store another binary value of a character
        
StrFromList = ' '.join([str(elem) for elem in message]) #merging the list in a string
print(StrFromList)

    