import cv2

image = cv2.imread('dots-bin.png',1) #Loads image with 1 channel.

# Create a kernel, i chose an elipse 7 pixels wide 7 pixels heigh.
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))

# Create an erosion image (Removes noise)
erosion = cv2.erode(image,kernel,1)
# Create a dilation image (Brings back objects to normal size)
dilate = cv2.dilate(erosion,kernel,1)

# Subtract the eroded image from the dilated to get the boundaries.
boundary = cv2.subtract(dilate,erosion)


# Show images
cv2.imshow("Source",image)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilate)
cv2.imshow("Boundary",boundary)

# Quit program is 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()