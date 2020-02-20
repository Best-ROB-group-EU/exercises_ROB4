import cv2

image = cv2.imread('grpp.jpg',1) #Loads image with 1 channel.
resize = cv2.resize(image,(1008,756)) #Resize image to something workable

imagesobel = cv2.Sobel(resize,cv2.CV_16S,1,0,ksize=3) #WIP




#Show the results
cv2.imshow("Original", resize)
cv2.imshow("Sobeled", imagesobel)


# Quit program is 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()