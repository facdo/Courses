""" Preparation, test and dev code. Not part of the main programm.
"""

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x1 = tf.constant([1,2,3,4])
x2 = tf.constant([1,4,7,12])

result = tf.multiply(x1, x2)

with tf.Session() as sess:

    print(sess.run(result))


