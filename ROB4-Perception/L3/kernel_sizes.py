import cv2

image = cv2.imread('board.tif',1) #Loads the image with 1 channel.

print("Press 'q' to exit!")

# Blur frame to remove noise
imageGauss = cv2.GaussianBlur(image, (9, 9),0) #9x9 Kernel, must be uneven numbers
imageBlur = cv2.blur(image,(5,5)) #5x5 kernel, must be uneven.
imagemedianBlur = cv2.medianBlur(image,3) #Pretty sure it must be uneven.


# Display result
cv2.imshow("Original", image)
cv2.imshow("Gaussian", imageGauss)
cv2.imshow("Blur", imageBlur)
cv2.imshow("Median Blur", imagemedianBlur)

# Quit program is 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


