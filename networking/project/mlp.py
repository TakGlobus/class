
import numpy as np
import tensorflow as tf

from tensorflow.python.keras.layers import *                                                    
from tensorflow.python.keras.models import Model

# build model
class model_class:

  def __init__(self, net_name):
    self.net_name = net_name

  def build(self, imgs):
    x = Dense(512, activation='relu')(imgs)  # fully-connected layer with 128 units and ReLU activation
    x = Dense(128, activation='relu')(x)
    preds = Dense(10, activation='softmax')(x) 

    return preds

  
