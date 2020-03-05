import cv2
import numpy as np

#Import image
source = cv2.imread('tools-black.jpg', cv2.IMREAD_GRAYSCALE)
final = cv2.imread("tools-black.jpg")
ret, thresh = cv2.threshold(source, 180, 240, 0)

#Use median blur to remove even more noise.
median = cv2.medianBlur(thresh,3)

#Opening on the threshold against noise.
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
erosion = cv2.erode(median,kernel,1)
opening = cv2.dilate(erosion,kernel,1)

#closing
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 30))
dilation2 = cv2.dilate(opening,kernel2,1)
erosion2 = cv2.erode(dilation2,kernel2,1)

#contours, hierachy = cv2.findContours(source, 1, 2)
contours, hierarchy = cv2.findContours(erosion2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)

# FILL ALL THE CONTOURS
cv2.drawContours(final, contours, -1, (0,255,255), cv2.FILLED)


cv2.imshow("Source",source)
cv2.imshow("Final", final)
#cv2.imshow("Thresh",thresh)
#cv2.imshow("Opening",opening)
#cv2.imshow("Median", median)


# Quit program is 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()