from keras import backend as K
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense, Dropout
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator

IMG_CHANNELS = 3
IMG_ROWS = 150
IMG_COLS = 150

BATCH_SIZE = 256
NB_EPOCH = 100
NB_CLASSES = 1

N_FLATTEN = 128
N_POOLING_1 = 4

OPTIMIZER = Adam()

def model_v1():
    model = Sequential()

    model.add(Conv2D(32, 
            kernel_size = 3, 
            padding='same',
            input_shape=(IMG_ROWS, IMG_COLS, IMG_CHANNELS)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(N_POOLING_1,N_POOLING_1))
    model.add(Dropout(0.25))

    model.add(Conv2D(32, 
            kernel_size = 3, 
            padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(N_POOLING_1,N_POOLING_1))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(N_FLATTEN))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(NB_CLASSES))
    model.add(Activation('softmax'))

    model.summary()

    model.compile(
        loss='binary_crossentropy', 
        optimizer=OPTIMIZER, 
        metrics=['accuracy'])
    
    return model

    