import cv2
import sys

# Open webcam as video capture
cap = cv2.VideoCapture(0)

if (cap.isOpened() is False):
    print("Failed to initialize capture from webcam. Exiting... \n")
    sys.exit(0)


print("Press 'q' to exit!")
# Main loop
while (True):
    # Read image from webcam
    ret, frame = cap.read()
    if (ret is False):
        break


    # Find redish colours
    red_mask = cv2.inRange(frame, (10, 10, 90), (50, 50, 150))

    kernel_large = cv2.getStructuringElement(cv2.MORPH_RECT, (35, 35))
    kernel_small = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))


    #Apply Opening (Noise removal)
    red_erosion = cv2.erode(red_mask, kernel_small, 1)
    red_opening = cv2.dilate(red_erosion, kernel_large, 1)

    # Apply Closing (Object sharpening)
    red_unify = cv2.dilate(red_opening, kernel_small, 1)


    #Calculate Center og blob
    # calculate moments of binary image
    M = cv2.moments(red_unify)
    # calculate x,y coordinate of center
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # put text and highlight the center
        cv2.circle(frame, (cX, cY), 10, (255, 255, 0), -1)
    else:
        cX, cY = 0, 0




    cv2.imshow("Feed", frame)
    cv2.imshow("Red", red_mask)
    cv2.imshow("Red_Opened", red_opening)
    cv2.imshow("Red Unification",red_unify)
    # Quit program is 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()