
import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread("M2_agent_robot.png",cv2.IMREAD_UNCHANGED) # rgb
#Show the colored image
#cv2.imshow('Original',img)
#Convert the colored image into grey and store into a separte variable then show
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    ## grayscale
#cv2.imshow('Grey',gray_img)
#print type(img)
print ('RGB shape: ', img.shape)        # Rows, cols, channels
#print 'ARGB shape:', alpha_img.shape
print ('Gray shape:', gray_img.shape)
print ('img.dtype: ', img.dtype)
print ('img.size: ', img.size)
print ('img_gray.dtype: ', gray_img.dtype)
print ('img_gray.size: ', gray_img.size)
"""
As first input, the circle function receives the image on which we want to draw the circle.
As second, it receives a tuple with the x and y coordinates of the center of the circle.
As third argument, we need to pass the radius of the circle 
and as fourth, we need to specify another tuple with the color of the circle, in BGR (Blue, Green and Red) format.
"""
cv2.circle(img,(100, 0), 25, (0,255,0))
cv2.circle(gray_img,(0, 100), 25, (0,0,255))
 
cv2.circle(img,(100, 100), 50, (255,0,0), 3)
cv2.rectangle(img,(100, 100), (200,180), (255,0,0), 4)
img2 = cv2.imread("M2_agent_robot.png")

blurred_img = cv2.blur(img2, (9,5) )
cv2.imshow('Test image',img)

cv2.imshow('Test image_gray',gray_img)
"""
#he waitKey function, which will wait for a keyboard event.
#This function receives as input a delay, specified in milliseconds. 
#Nonetheless, if we pass the value 0, then it will wait indefinitely until
# a key event occurs.
"""
cv2.waitKey(0)
"""
#once the user pressed a key, we call the destroyAllWindows function,
# which will destroy the previously created windows.
"""
cv2.destroyAllWindows()

