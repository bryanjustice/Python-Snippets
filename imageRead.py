"""
Basic image read and manipulation in OpenCV Python
"""

import cv2

img = cv2.imread("scheyer.jpg", cv2.IMREAD_COLOR)

# Show the image, arguments are upper caption and image handle
cv2.imshow("Scheyer Face!", img)

# Wait for three seconds
# TODO: For some readon this is not working with waitKey(0)
cv2.waitKey(3000)

#close window
cv2.destroyAllWindows()



