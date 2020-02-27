import cv2

Source = cv2.imread("dots-lines.png",1) #loads the source image, 1 channel.

# Create a dot shaped kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (12, 12))

# Use Opening method first erode away and then dilate again.
erosion = cv2.erode(Source,kernel,1)
dilation = cv2.dilate(erosion,kernel,1)



# Show images
cv2.imshow("Source",Source)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation + Erosion",dilation)


# Quit program is 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()