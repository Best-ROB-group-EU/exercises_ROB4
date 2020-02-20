import cv2

image = cv2.imread('papir.jpg',1) #Loads image with 1 channel.

# Blurs the image so you get the general pixel intensity of the background
imageBackground = cv2.blur(image,(50,50))
# Subtracts the background
imagesubtract = cv2.subtract(imageBackground,image)

#Show the results
cv2.imshow("Background blur", imageBackground)
cv2.imshow("Original", image)
cv2.imshow("Subtracted", imagesubtract)



# Quit program is 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()