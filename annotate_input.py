import cv2
import numpy as np

# Global variables
points = []

# Load the image
img = cv2.imread('input.png')

# Mouse callback function
def draw_points(event, x, y, flags, param):
    global points
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print("Point added: ({}, {})".format(x, y))
        text = '({}, {})'.format(x, y)
        cv2.circle(img, (x, y), 4, (255, 0, 0), 2)
        img = cv2.putText(img, text, (x-10,y-10), cv2.FONT_HERSHEY_PLAIN,
                            1, (0, 0, 255), 1, cv2.LINE_AA)
        # Create a window and set the mouse callback function
        cv2.namedWindow('image')
        cv2.imshow('image', img)



# Create a window and set the mouse callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_points)

# Display the image
cv2.imshow('image', img)
#cv2.imwrite('image_anotated.png', img)

# Wait for a key press and then save the points to a file
cv2.waitKey(0)

cv2.imwrite('image_anotated_calibration.png', img)
np.save("final_cord_calibration.npy", points)
# Close the window
cv2.destroyAllWindows()
