import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
import numpy as np

# Define the input data
inputs = [1, 2, 3]

# Create an input layer with one feature
input_layer = tf.keras.layers.Input(shape=(1,))
x = Dense(1)(input_layer)

# Add a dropout layer to prevent overfitting
output = Dropout(0.5)(x)

print(output)
