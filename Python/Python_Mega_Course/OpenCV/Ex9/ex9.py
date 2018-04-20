# Coding Exercise 9 - Batch Image Resizing
# Write a script that resizes all images in a directory to 100x100.
import cv2, os

# get the list of files in the project directory
file_list = os.listdir()
# iterates through all files
for f in file_list:
    # check the extension
    _, ext = os.path.splitext(f)
    if ext == '.jpg':
        # reads the image
        img = cv2.imread(f, 1)
        # overides the file with a resized version of the image
        cv2.imwrite(f, cv2.resize(img, (100,100)))

# proposed solution
# import cv2
# import glob
#
# images=glob.glob("*.jpg")
#
# for image in images:
#     img=cv2.imread(image,0)
#     re=cv2.resize(img,(100,100))
#     cv2.imshow("Hey",re)
#     cv2.waitKey(500)
#     cv2.destroyAllWindows()
#     cv2.imwrite("resized_"+image,re)
