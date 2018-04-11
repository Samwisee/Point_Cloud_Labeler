

# Imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

print('Hello World')

# Convolution Layer 1
conv1 = tf.layers.conv2d(
    inputs=input_layer,
    filters=32,
    kernel_size=[5, 5],
    padding="same",
    activation=tf.nn.relu)

# Max-pooling Layer 1
pool1 = tf.layers.max_pooling2d(
    inputs=conv1, 
    pool_size=[2, 2], 
    strides=2)

# Convolution Layer 2
conv2 = tf.layers.conv2d(
    inputs=pool1,
    filters=64,
    kernel_size=[5, 5],
    padding="same",
    activation=tf.nn.relu)

# Max-pooling Layer 2
pool2 = tf.layers.max_pooling2d(
    inputs=conv1, 
    pool_size=[2, 2], 
    strides=2)

# ???  
pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])

# Dense Layer
dense = tf.layers.dense(
    inputs=pool2_flat, 
    units=1024, 
    activation=tf.nn.relu)

