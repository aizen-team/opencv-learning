import cv2 as cv
import numpy as np

blank = np.zeros((600,600,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[:] = 0, 255,0 # Green
# blank[:] = 0,0,255 # Read
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=cv.FILLED)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300, 400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Nguyen Trieu', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

# img = cv.imread('photos/cat.jpg')
# cv.imshow('Cat', img)

cv.waitKey(0)