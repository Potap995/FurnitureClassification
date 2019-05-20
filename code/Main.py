import sys
import os
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import numpy as np
import Models as model
class MyApp:
    def __init__(self, window):
        self.window = window
        self.configur_window()

    def loadImgClick(self):
        self.imgName = tk.filedialog.askopenfilename(filetypes=[("Images","*.png *.jpg")])
        if (self.imgName == ""):
            return
        img = Image.open(self.imgName)
        img.thumbnail((self.canvas.winfo_width(),self.canvas.winfo_height()), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.canvas.create_image(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, image=self.img ,anchor="c")

    def loadModelClick(self):
        self.ansCanvas.delete("all")
        self.chartCanvas.delete("all")
        modelPath = tk.filedialog.askopenfilename(filetypes=[("Models", "*.h5")])
        if modelPath == "":
            return
        _ , filename = os.path.split(modelPath)
        modelName , _ = os.path.splitext(filename)
        self.predictor.loadModel(modelName, modelPath)
        models = list(self.modelCombobox['values'])
        models.append(modelName)
        self.modelCombobox['values'] = models


    def predictClick(self):
        self.ansCanvas.delete("all")

        if self.imgName == "":
            self.ansCanvas.create_text(10, 10, anchor="nw", text="Load an image", font="Times 11")
            return

        if self.modelCombobox.get() == "":
            self.ansCanvas.create_text(10, 10, anchor="nw", text="Select model", font="Times 11")
            return

        predict = self.predictor.predict(self.modelCombobox.get(), self.imgName)
        ind_max = np.argmax(predict)

        self.ansCanvas.create_text(10, 10, anchor="nw", text=self.classes[ind_max].upper(), font="Times 12")

        self.chartCanvas.delete("all")
        for i in range(len(predict)):
            self.chartCanvas.create_text(10, 10 + i*45, anchor="nw", text=self.classes[i], font="Times 11")
            self.chartCanvas.create_rectangle(10, 30 + i*45, 10 + predict[i] * 150, 50 + i*45, fill="blue")


    def configur_window(self):
        self.window.title("Furniture")
        self.window.geometry("1000x620")
        self.window.resizable(False, False)

        self.canvas = tk.Canvas(self.window, heigh=600, width=800, bd=2, relief="ridge", bg="white")
        self.canvas.pack(side="left")

        self.modelFrame = tk.LabelFrame(text="Model")
        self.modelFrame.pack(side="top", fill="x")
        self.modelCombobox = ttk.Combobox(self.modelFrame, state="readonly")
        self.modelCombobox['values'] = ["MobileNet"]
        self.modelCombobox.pack(side="top", fill="x", pady=10)
        self.loadModelButton = tk.Button(self.modelFrame, heigh=2, width=24, text="Load Model",
                                       command=lambda: MyApp.loadModelClick(self))
        self.loadModelButton.pack(side="top", fill="x", pady=5)

        self.modelImage = tk.LabelFrame(text="Image")
        self.modelImage.pack(side="top", fill="x")
        self.loadImgButton = tk.Button(self.modelImage, heigh=2, width=24, text="Load Image", command= lambda :MyApp.loadImgClick(self))
        self.loadImgButton.pack(side="top", fill="x", pady=0)
        self.predictButton = tk.Button(self.modelImage, heigh=2, width=24, text="Predict", command= lambda :MyApp.predictClick(self))
        self.predictButton.pack(side="top", fill="x", pady=2)

        self.modelAnswer = tk.LabelFrame(text="Answer")
        self.modelAnswer.pack(side="top", fill="x")
        self.ansCanvas = tk.Canvas(self.modelAnswer, heigh=30, bd=2, relief="ridge", bg="white")
        self.ansCanvas.pack(side="top", fill="x", pady=5)
        self.chartCanvas = tk.Canvas(self.modelAnswer, heigh=200, bd=2, relief="ridge", bg="white")
        self.chartCanvas.pack(side="top", fill="x", pady=0)

        self.provar = tk.IntVar()
        self.provar.set(0)
        self.bar = ttk.Progressbar(self.window, variable=self.provar)
        self.bar.pack(side="top", fill="x")

    def loadResurses(self):
        self.imgName = ""
        self.predictor = model.Predictor(self)
        self.predictor.loadModel("MobileNet", "models/MobileNet.h5")
        self.classes = ["chair", "couch", "plant", "table"]





window = tk.Tk()

myApp = MyApp(window)
window.after(100, myApp.loadResurses)
window.mainloop()
sys.exit()
