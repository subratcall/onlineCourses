from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
import matplotlib.pyplot as plt

class LeNet:
    @staticmethod
    def build(input_shape, classes):
        model = Sequential()
        model.add(Conv2D(
            filters = 20, 
            kernel_size = 5,
            padding ="same",
            input_shape = input_shape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(
            pool_size=(2,2),
            strides=(2,2)))
        model.add(Conv2D(
            filters=50,
            kernel_size = 5,
            border_mode = "same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(
            pool_size=(2,2),
            strides=(2,2)))
        
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))

        model.add(Dense(500))
        model.add(Activation("relu"))
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        return model

