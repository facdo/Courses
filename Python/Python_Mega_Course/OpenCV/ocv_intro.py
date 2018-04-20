# introduction to the OpenCV package, for image manipulation, analysis, computer
# vision and pattern recognition

# Computer Vision is the field that acquires, analyses and makes decisions based
# on the image. An interesting application for that is motion detection algorithms,
# which we will star building in the next section

# Section 18 - 144: Loading, displaying and Writing images
import cv2

# to load an image to a numpy array we will use the imread method
# we need to pass the file name (with full path in case is not in the same directory)
# and a second argument, which is how we want to read that image (RGB=1, graysalce=0
# color but with transparency enabled = -1)
img = cv2.imread('galaxy.jpg',0)
print(type(img))
# as we can see the image is represented as a numpy array, with the intensity
# of the light in each pixel, from 0 to 255
print(img)
print(img.shape)
# we can see that it is a 1485x990 pixel image
# if we use the colored version we have one extra dimension, so each pixel has
# RGB values associated to it, so it would be a 1485x990x3 array

# we can resize the image to whatever values we want using the resize method
# to mantain the aspect ratio we are getting the shape from the image and
# scaling it by half
resized_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

# we can view the image with the imshow method and set to be displayed for
# a specific amount of time with the waitKey method associated with destroyAllWindows
# method
cv2.imshow("Galaxy", resized_image)
cv2.waitKey(4000)
cv2.destroyAllWindows()

# lets write the resized image to a new jpg file using the imwrite method
cv2.imwrite('resized_galaxy.jpg', resized_image)
