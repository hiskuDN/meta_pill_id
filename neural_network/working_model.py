import pickle
from neural_network.conv_net import createModel
from neural_network.create_dataset import dataset
from sklearn.metrics import confusion_matrix
import tensorflow as tf
import numpy as np
import os

def load_pretrained_model():
    checkpoint_path = "neural_network/training_1/cp.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)

    test_x=[]
    train_x=[]
    test_y=[]
    train_y=[]

    pickle_in=open('neural_network/train_x.pickle','rb')
    train_x=pickle.load(pickle_in)

    pickle_in=open('neural_network/train_y.pickle','rb')
    train_y=pickle.load(pickle_in)

    model=createModel(train_x)
    model.load_weights(checkpoint_path)

    
    return model

def evaluate_model(model):
    pickle_in=open('neural_network/test_x.pickle','rb')
    test_x=pickle.load(pickle_in)

    pickle_in=open('neural_network/test_y.pickle','rb')
    test_y=pickle.load(pickle_in)
    model.evaluate(test_x,test_y)
    ypr=model.predict(test_x)
    yprr = np.argmax(ypr, axis=1)
    print(confusion_matrix(test_y, yprr))


