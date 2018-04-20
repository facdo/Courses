# Section 10 - Numpy
# 81 - What is Numpy?
# Exemple in image processing
# images can be stored as array of numbers representing the color and intensity
# for each pixel, which is the idexed position for that intensity value
# We can represent images by lists, but that is not very efficient and ocupies
# a lot of space in memory
# A way around that is to use the numpy package
# import numpy as np
# # two dimensional array example
# n=np.arange(27).reshape(3,9)
# print(n)
# # 3D array example
# n=n.reshape(3,3,3)
# print(n)
#
# # we can create a numpy array from a python listdir
# A = np.array([1,2,3,4,5,5,6,7])
# print(A, type(A))

# 83 - Images to Numpy and Vice-Versa
import cv2
import numpy as np
# the second argument can be 0, for grayscale images, and 1, for colored bgr images
# blue, green and red
im_g=cv2.imread('4x4_cool.jpg', 0)
# it saves it as a numpy array
print(im_g)
# the intesity value is stored from 0 (black) and 255 (white)
# if we use the colored version we would have a 3D array, each one for the
# intensity of blue, green and red respectively
# we can write images from numpy array using the imwrite method
cv2.imwrite('4x4_grey.png', im_g)

# 84 - Numpy Indexing, Slice and Iterating
# almost the same as lists, with the multidimensional aspect being Address
# with multiple ranges, one for each dimension, separated by commas ','
print(im_g[0:2, 0:2])
print(im_g[::3,::3])

#

cv2.imwrite('4x4_mod.png',im_g[:,::-1])

# not part of the course
# simple encrypt and decrip an image
import random
sf_idx = np.arange(im_g.shape[0])
random.shuffle(sf_idx)
enc_img = np.zeros(im_g.shape, dtype=np.int)
for i in range(len(sf_idx)):
    enc_img[i]=im_g[sf_idx[i]]

# writes the encrypted image
cv2.imwrite('4x4_encrypted.png', enc_img)

# decrypts the image
rec_img = np.zeros(enc_img.shape, dtype=np.int)
for i in range(len(sf_idx)):
    rec_img[sf_idx[i]]=enc_img[i]

# saves the recovered image
cv2.imwrite('4x4_recover.png', rec_img)

# how to iterate through columns
# we can use the transpose method
for col in im_g.T[:10]:
    print(col)

# 85 - Stacking and Splitting
# to concatenate two arrays, or to create multiple arrays from one
# there are two ways of stackig, horizontal, in which the concatenated arrat
# will be stacked as columns, so N rows A and B must be equal
A = np.arange(24).reshape(4,6)
B = array[el+24 for el in A]
C = np.hstack((A,B))
print(C)
# or vertical array, in which the elements will be concatenated as rows, so N
# columns A and B must be equal
D = np.vstack((A,B))
print(D)
# Similarly, there are two kids of array spliting, horizontal and vertical
# the number of divisions must be an integer
# for instance, if the array has 5 columns, you cant horizontaly split it in
# to 3 arrays using this method
a_1, a_2 = np.hsplit(A, 2)
b_1, b_2 = np.vsplit(B,2)
# it returns a list of arrays
