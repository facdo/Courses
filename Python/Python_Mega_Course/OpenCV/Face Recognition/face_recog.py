# Section 18
# 148 - Face Detection

# based on the .xml file that contains features to help detect faces in an image
# it is a hardcascade file, specific for frontal face detection
# There are many hardcascade files used for detection of different patterns in
# images. We can get those from the opencv github page
# It was created with machine learn training algorithms, with a large database
# set of classified images

# the alrgorithm uses window sweep, changing the window size and searching for
# the features described in the hardcascade file

import cv2

# we will create a cascade classifier object
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# load the image that we want to do the face detection
img = cv2.imread('photo.jpg')
# it is better to work with grayscale images
# so we will use the cvtColor converter method to create a grayscale version of
# our image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# the classifier will return the coordinates from the first pixel in the face
# and also the height and width, so we can draw a rectangle in the face

# the detecMultiScale method is used to have different sizes windows scanning
# the image, so it doesn't matter the size of the face that we are trying to detect
# the scaleFactor argument dictates how the different size window will progress
# So it will decrease the image size by 5% in each iteraction. The smaller the
# value the higher the accuraccy
faces = face_classifier.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=10)
print(type(faces))
print(faces)
# so, faces is just an array defining the first pixel, the height and width of
# the face
# row 83, column 155, 382x382

# we can draw a retange in the image now
for x, y, w, h in faces:
    # openCV makes it easy for us with the rectangle method
    # we will define the color and linewidth as well
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

# now we can display our image
cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# we can crop our image with the values defined by the face rectangle
# it will only get one face
x, y, w, h in faces[0,:]
crop_face = cv2.imwrite('crop_face.jpg', img[y:y+h,x:x+w,:])
