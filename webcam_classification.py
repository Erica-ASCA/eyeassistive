# %%
import dlib
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow import keras
import tensorflow as tf

# %%
model = load_model('my_model')

# %%
predictor = dlib.shape_predictor('shape_68.dat')
detector = dlib.get_frontal_face_detector()

# %%
#model.summary()

# %%
def class_names(number):
    if number == 0:
        return "Center"
    elif number == 1:
        return "Up"
    elif number == 2:
        return "Down"
    elif number == 3:
        return "Right"
    elif number == 4:
        return "Left"
    elif number == 5:
        return "Closed"
    else:
        return "Unknown"


# %%

def generate_predictions(camera):
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    #print(rects)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
    try:
        shape
    except NameError:
        return "Unknown"
    x_eye_points = [shape.part(x).x for x in range(37, 42)]
    y_eye_points = [shape.part(x).y for x in range(37, 42)]
    padding = 12
    maxx = max(x_eye_points)
    minx = min(x_eye_points)
    maxy = max(y_eye_points)
    miny = min(y_eye_points)
    crop_image = frame[miny-padding:maxy +
                        padding, minx-padding:maxx+padding]
    resize = cv2.resize(crop_image, (24, 24))
    #resize = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    #resize = cv2.flip(resize,1)
    #cv2.imshow("Output", resize)
    resize = np.expand_dims(resize, axis=0)
    predicted = model.predict(resize)
    predicted_class = np.argmax(predicted)
    return (class_names(predicted_class))

# %%
#cap = cv2.VideoCapture(0)
#while True:
#    print(generate_predictions(cap))


