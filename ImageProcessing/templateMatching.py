"""
Name: Archit Jaiswal


Image recognization using the Cross Correlation technique

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.feature import match_template

# this function was ready on the website as mentioned in HW instructions
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])



def findImage(mainImage, template) :
    ima=plt.imread(mainImage) #stores an 2D array of image in "ima"
    plt.title('Original Image') #prints the original name of file
    plt.imshow(ima) # shows the original image back but 'gray' is needed to see clear image
    plt.show()
    
    img = mpimg.imread(mainImage)
    gray = rgb2gray(img)    # converting the image to grayscale becuase coloured image has 3 layers and correlation will not work
    plt.title('Gray Scale Image')
    plt.imshow(gray, cmap='gray') #plotting image in the grayscale
    plt.show()
    
    tempImage = rgb2gray(mpimg.imread(template)) # converting template in gray scale
    plt.title('Gray Scale Template Image')
    plt.imshow(tempImage, cmap='gray') #plotting image in the grayscale
    plt.show()
    
    
    result = match_template(gray, tempImage) # this will have the corrosponding values of correllation (-1<= value <=1)
    plt.imshow(result, cmap='gray')
    r, c = np.unravel_index(np.argmax(result), result.shape) #it gives the point where maximum value of correlation is observed
    r_1, c_1 = tempImage.shape #this is the dimensions of image which is being matched
    
    
    gray[r:r + r_1, c:c + c_1] = 0 #setting the matching region to 0 for blacking it out
    plt.title('Final Match Image')
    plt.imshow(gray, cmap='gray') #printing the image 
    
    return r,c #returns the coordinates of row and coloums of maximum correlation to the main function
    
    
#############  main  #############
# this function should be how your code knows the names of
#   the images to process
# it will return the coordinates of where the template best fits

if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    r, c = findImage(mainImage, template)

    print("coordinates of match = (%d, %d)" % (r, c))
