from skimage.io import imread
from skimage.transform import resize
import numpy as np
import tensorflow as tf
from keras import backend as ker_bac
from keras.models import load_model

config = tf.ConfigProto()
config.gpu_options.allow_growth = True  # Don't pre-allocate memory; allocate as-needed
sess = tf.Session(config=config)
ker_bac.tensorflow_backend.set_session(sess)

class Predictor:
    models = dict()

    def __init__(self, App):
        self.App = App

    def loadModel(self, name, path):
        self.App.ansCanvas.create_text(10, 10, anchor="nw", text="Model is loading...", font="Times 11")
        self.App.provar.set(50)
        self.App.window.update()
        self.models[name] = load_model(path)
        self.App.provar.set(100)
        self.App.ansCanvas.delete("all")
        self.App.ansCanvas.create_text(10, 10, anchor="nw", text="Model has been loaded", font="Times 10")
        self.App.window.update()

    def predict(self, modelName, fileName):
        global graph
        graph = tf.get_default_graph()

        myImg = resize(imread(fileName)[:, :, :3], (224, 224), anti_aliasing=True)
        myImg = np.reshape(myImg, [1, 224, 224, 3])
        with graph.as_default():
            ans = self.models[modelName].predict(myImg)
        return ans[0]
