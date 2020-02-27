import cv2

Source = cv2.imread("apple.jpg") #Reads the image


# Isolate leaf (Using HSV)
## convert to hsv
hsv = cv2.cvtColor(Source, cv2.COLOR_BGR2HSV)

leaf = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

# Isolate the stalk
stalk = cv2.inRange(Source,(20,20,80),(100,100,150))

# Masking by colour (Finding apple)
apple = cv2.inRange(Source, (0, 0, 50), (200, 200, 255))

# Subtracting the leaf and stalk
mask = cv2.subtract(apple,leaf)
#mask = cv2.subtract(mask,stalk)

# Performing Opening
# Create a dot shaped kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
erosion = cv2.erode(mask,kernel,1)
opening = cv2.dilate(erosion,kernel,1)

# Perform Closing and bring back the apple
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
dilation = cv2.dilate(opening,kernel,1)
closing = cv2.erode(dilation,kernel,1)

#Create a comparison
comparison = Source & cv2.cvtColor(closing, cv2.COLOR_GRAY2BGR)

# Show images
cv2.imshow("Source",Source)
cv2.imshow("leaf",leaf)
cv2.imshow("Stalk",stalk)
cv2.imshow("Apple", apple)

cv2.imshow("Mask", mask)
cv2.imshow("Opening", opening)

cv2.imshow("Final", closing)
cv2.imshow("Comparison", comparison)
# Quit program is 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()