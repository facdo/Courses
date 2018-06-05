""" Classes:
        * DataManip: loading, preparing and viewing the data for classification.
        * TfModel: applying the neural network algorithm for classifying the data
"""

import os
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import transform
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

class DataManip():

    train_data_dir = ""
    test_data_dir = ""

    def __init__(self, root_data_path):
        """ Initialize the data directory, specified by the root_data_path.
        """
        self.train_data_dir = os.path.join(root_data_path, "TrafficSign/Training")
        self.test_data_dir = os.path.join(root_data_path, "TrafficSign/Testing")
    
    def load_data(self, data_set = "train"):
        """ Loads the dataset from the x_data_dir path, where x is the data_set argument which can be
            either "train" (default) or "test".
            Returns a tuple consisting of two arrays, one of images and the other of the corresponding labels
                for those images.
        """
        if data_set == "train":
            data_dir = self.train_data_dir
        else:
            data_dir = self.test_data_dir

        dir_list = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
        labels, images = [], []
        for d in dir_list:
            label_dir = os.path.join(data_dir, d)
            file_names = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith('.ppm')]
            for f in file_names:
                images.append(imread(f))
                labels.append(int(d))

        return (np.array(images), np.array(labels))

    def format_data(self, data, size=(28,28), gray_scale=True):
        """ Reshape and convert to grayscale.
        """
        result_imgs = np.array([transform.resize(img, size) for img in data])
        if gray_scale:
            result_imgs = rgb2gray(result_imgs)
        return result_imgs


    def view_data(self, data, plot_type='label_hist', n_images = 4, n_cols = 4):
        """ Plot the data according to the specified plot type, which can be "label_hist", "rnd_sample" or "image_mtx".
        """
        if plot_type == 'label_hist':
            plt.hist(data, bins=62)
        elif plot_type == "rnd_sample":
            # choose n_images randomly from the image data to display
            sample_images = np.array([data[rnd_index] for rnd_index in 
                                        np.random.choice(np.arange(data.shape[0]), size=n_images)])
                                                                        
            # sample_images = np.random.choice(data, size=n_images)
            for i in np.arange(len(sample_images)):
                plt.subplot(n_images//n_cols+1, n_cols, i+1)
                plt.axis("off")
                plt.title("Shape: {}".format(sample_images[i].shape))
                plt.imshow(sample_images[i])
                plt.subplots_adjust(wspace=0.5, hspace=0.5)
        elif plot_type == "image_mtx":
            # it is expected that the data variable contains two arrays, one for the images
            # and the other for the labels
            images, labels = data
            plt.figure(figsize=(12,12))
            # iterate through all unique labels
            for i, label in enumerate(set(labels)):
                # pick a random image corresponding to that label
                sample_image = np.random.choice(images[labels==label]) 
                plt.subplot(8, 8, i+1)
                plt.axis("off")
                plt.title("Label: {} - {}".format(label, np.count_nonzero(labels==label)), fontsize=8)
                plt.imshow(sample_image)
                plt.subplots_adjust(wspace=0.3, hspace=0.3)
        else:
            print("please input a valid plot_type.")
            return
        plt.show()
        

class TfModel():
    """ Deep learning model configuration
    """
    def __init__(self, img_size = (28,28), n_labels = 62):
        # placehoder for the data
        self.x = tf.placeholder(dtype = tf.float32, shape = [None, *img_size])
        self.y = tf.placeholder(dtype = tf.int32, shape = [None])

        # Flatten the input data
        img_flat = tf.contrib.layers.flatten(self.x)

        # Fully connected layer
        self.logits = tf.contrib.layers.fully_connected(img_flat, n_labels, tf.nn.relu)

        # define a loss function
        self.loss = tf.reduce_mean(tf.nn.sparce_softmax_cross_entropy_with_logits(labels = self.y, 
                                                                                  logits = self.logits))
        # define an optimizer
        self.train_op = tf.train.AdamOptimizer(learning_rate = 0.001).minimize(self.loss)

        # Convert logits to label indexes
        self.correct_pred = tf.argmax(self.logits, 1)

        # define an accuracy metric
        self.accuracy = tf.reduce_mean(tf.cast(self.correct_pred, tf.float32))


# # Initialization example
root_dir = r"C:\Users\20006083\OneDrive - UNITEC SEMICONDUTORES SA\Felipe Oliveira\Code_Dev\Datasets"
data_handle = DataManip(root_dir)
images, labels = data_handle.load_data()
# resize and convert to grayscale
format_images = data_handle.format_data(images)


# # Example on the three different types of plots in the view_data method:
# data_handle.view_data(labels)
# data_handle.view_data(images, plot_type="rnd_sample", n_images=9, n_cols=3)
# data_handle.view_data(format_images, plot_type="rnd_sample", n_images=9, n_cols=3)
data_handle.view_data([images, labels], plot_type="image_mtx")

    